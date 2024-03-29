import os
import os.path
import userpaths
import magic


from datetime import datetime
from pathlib import Path

from typing import Tuple
from winreg import HKEYType, ConnectRegistry, HKEY_LOCAL_MACHINE, OpenKey, QueryValueEx

from whoosh import index
from whoosh.fields import SchemaClass, TEXT, ID, NUMERIC, DATETIME
from whoosh.qparser import QueryParser
from whoosh.query import And


class FileCollectionSchema(SchemaClass):
    path_with_file_name = ID(stored=True)
    path = TEXT(stored=True)
    file_name_with_extension = TEXT(stored=True)
    file_name = TEXT(stored=True)
    file_size = NUMERIC(stored=True)
    file_type = TEXT(stored=True)
    last_modified = DATETIME(stored=True)


# Windows application names from extension
class ExtensionQuery:
    def __init__(self):
        self.base: str = r"SOFTWARE\Classes"
        self.reg: HKEYType = ConnectRegistry(None, HKEY_LOCAL_MACHINE)

    def _get_value_from_class(self, class_str: str) -> str:
        path: str = fr"{self.base}\{class_str}"
        key: HKEYType = OpenKey(self.reg, path)
        value_tuple: Tuple[str, int] = QueryValueEx(key, "")
        return value_tuple[0]

    def get_application_name(self, ext: str) -> str:
        return self._get_value_from_class(self._get_value_from_class(ext))


class FileCollection():
    ix: index.FileIndex
    windows_file_type_determiner = ExtensionQuery()
    mime_type_determiner = magic.Magic(mime=True)
    path_to_user_index: str
    path_to_user_files: str
    dir_tree = {}
    file_paths = []

    def __init__(self, app_name):
        self.path_to_user_index = userpaths.get_local_appdata() + os.path.sep + app_name
        self.path_to_user_files = userpaths.get_my_documents()

        def set_paths(path):
            for root, dirs, filenames in os.walk(path):
                for filename in filenames:
                    self.file_paths.append(os.path.join(root, filename))

        def init_index():
            writer = self.ix.writer()
            for path in self.file_paths:
                self.add_doc_to_index(writer, path)
            writer.commit()

        def increment_index():
            # The set of all paths in the index
            indexed_paths = set()
            # The set of all paths we need to re-index
            to_index = set()

            with self.ix.searcher() as searcher:
                writer = self.ix.writer()

                # Loop over the stored fields in the index
                for fields in searcher.all_stored_fields():
                    indexed_path = fields['path_with_file_name']
                    indexed_paths.add(indexed_path)

                    if not os.path.exists(indexed_path):
                        # This file was deleted since it was indexed
                        writer.delete_by_term(
                            'path_with_file_name', indexed_path)

                    else:
                        # Check if this file was changed since it
                        # was indexed
                        indexed_time: datetime
                        indexed_time = fields['last_modified']
                        mtime = datetime.fromtimestamp(
                            os.path.getmtime(indexed_path)).timestamp()
                        if mtime > indexed_time.timestamp():
                            # The file has changed, delete it and add it to the list of
                            # files to reindex
                            writer.delete_by_term(
                                'path_with_file_name', indexed_path)
                            to_index.add(indexed_path)

                # Loop over the files in the filesystem
                # Assume we have a function that gathers the filenames of the
                # documents to be indexed
                for path in self.file_paths:
                    if path in to_index or path not in indexed_paths:
                        # This is either a file that's changed, or a new file
                        # that wasn't indexed before. So index it!
                        self.add_doc_to_index(writer, path)

            writer.commit()

        if not os.path.exists(self.path_to_user_index):
            os.mkdir(self.path_to_user_index)

        set_paths(self.path_to_user_files)
        if index.exists_in(self.path_to_user_index):
            self.ix = index.open_dir(self.path_to_user_index)
            increment_index()
        else:
            self.ix = index.create_in(
                self.path_to_user_index, FileCollectionSchema)
            init_index()

    def refresh_dir_tree(self):
        self.dir_tree.clear()
        for root, dirs, filenames in os.walk(self.path_to_user_files):
            self.dir_tree[root] = dirs

    def add_doc_to_index(self, writer, path):
        try:
            file_type_name = self.windows_file_type_determiner.get_application_name(
                os.path.splitext(path)[1])
        except:
            file_type_name = self.mime_type_determiner.from_file(path)

        if writer is None:
            writer = self.ix.writer()

        writer.add_document(
            path_with_file_name=path,
            path=str(Path(path).parent),
            file_name_with_extension=os.path.basename(path),
            file_name=os.path.splitext(os.path.basename(path))[0],
            file_size=os.path.getsize(path) / 1000,
            file_type=file_type_name,
            last_modified=datetime.fromtimestamp(os.path.getmtime(path)))
        return writer

    def update_doc_to_index(self, old_path, new_path):
        writer = self.ix.writer()
        # with self.ix.writer() as writer:
        writer.delete_by_term("path_with_file_name", old_path)
        self.add_doc_to_index(writer, new_path)
        writer.commit()

    def delete_doc_from_index(self, path):
        writer = self.ix.writer()
        # with self.ix.writer() as writer:
        writer.delete_by_term("path_with_file_name", path)
        writer.commit()

    def search(self, search_path, filename_search_value, is_exact_path_search):
        if search_path == self.path_to_user_files:
            search_path = ""

        hit_list = list()
        with self.ix.searcher() as searcher:
            if len(filename_search_value) > 0:
                file_name_parser = QueryParser(
                    "file_name_with_extension", schema=self.ix.schema)
                file_name_query = file_name_parser.parse(
                    "*" + filename_search_value + "*")

            if len(search_path) > 0:
                path_parser = QueryParser("path", schema=self.ix.schema)
                path_query = path_parser.parse(search_path)

            local_variables = locals()
            if "file_name_query" in local_variables and "path_query" in local_variables:
                final_query = And([file_name_query, path_query])
            elif "file_name_query" in local_variables:
                final_query = file_name_query
            elif "path_query" in local_variables:
                final_query = path_query
            else:
                search_path = self.path_to_user_files
                final_query = QueryParser(
                    "path", schema=self.ix.schema).parse("*")

            results = searcher.search(final_query, limit=None)
            for hit in results:
                if is_exact_path_search == True:
                    # exact search is probably not possible with whoosh so check manuely
                    if hit["path"] == search_path:
                        hit_list.append(dict(hit.items()))
                else:
                    hit_list.append(dict(hit.items()))
            return hit_list
