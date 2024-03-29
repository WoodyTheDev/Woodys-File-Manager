
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path

from PySide6.QtCore import Qt


class WoodysFileWatcher():
    file_manager = None

    class WoodysFileManagerHandler(FileSystemEventHandler):
        def __init__(self, file_manager):
            super().__init__()
            self.file_manager = file_manager

        # ToDo: update gui incremental
        # ToDo: fix refresh_category_tree
        def on_modified(self, event):
            if event.is_directory == False:
                # print(f"File {event.src_path} has been modified")
                self.file_manager.file_collection.update_doc_to_index(
                    event.src_path, event.src_path)
                self.refreshGUI(event.src_path)

        def on_moved(self, event):
            if event.is_directory == False:
                # print(f"File {event.src_path} has been moved to {
                #   event.dest_path}")
                self.file_manager.file_collection.update_doc_to_index(
                    event.src_path, event.dest_path)
                self.refreshGUI(event.src_path)
            # else:
                # print(f"Folder {event.src_path} has been moved to {
                #   event.dest_path}")
                # self.file_manager.refresh_category_tree()

        def on_created(self, event):
            if event.is_directory == False:
                # print(f"File {event.src_path} has been created")
                self.file_manager.file_collection.add_doc_to_index(
                    None, event.src_path).commit()
                self.refreshGUI(event.src_path)
            # else:
                # print(f"Folder {event.src_path} has been created")
                # self.file_manager.refresh_category_tree()

        def on_deleted(self, event):
            # toDo: why the heck is a folder checked as a file?
            if Path(event.src_path).is_dir() == False:
                # print(f"File {event.src_path} has been deleted")
                self.file_manager.file_collection.delete_doc_from_index(
                    event.src_path)
                self.refreshGUI(event.src_path)
            # else:
                # print(f"Folder {event.src_path} has been deleted")
                # self.file_manager.refresh_category_tree()

        # ToDo scroll to previous position after refresh
        def refreshGUI(self, src_path):
            if self.file_manager.search_path != "":
                current_display_files_path = self.file_manager.search_path
            else:
                current_display_files_path = self.file_manager.file_collection.path_to_user_files
            # Check if change is in current display files page
            if self.file_manager.allFilesCheckBox.checkState() == Qt.CheckState.Unchecked and\
                    str(Path(src_path).parent) == current_display_files_path or\
                    self.file_manager.allFilesCheckBox.checkState() == Qt.CheckState.Checked and\
                    current_display_files_path in str(Path(src_path).parent):
                # scroll_position = self.file_manager.get_display_files_table_scroll_positions()
                self.file_manager.search_and_display_files()
                # self.file_manager.displayFilesTableWidget.scroll(scroll_position["x"], scroll_position["y"])
            # Check if change is in unsorted files page
            if str(Path(src_path).parent) == self.file_manager.file_collection.path_to_user_files:
                # scroll_position = self.file_manager.get_unsorted_files_table_scroll_positions()
                selected_rows = self.file_manager.unsortedFilesTableWidget.selectionModel().selectedRows()
                self.file_manager.refreshUnsortedFilesTable()
                # self.file_manager.unsortedFilesTableWidget.scroll(scroll_position["x"], scroll_position["y"])
                self.file_manager.reselect_remaining_rows_unsorted_files_table(
                    selected_rows)

    class Watcher:
        def __init__(self, path, event_handler):
            self.path = path
            self.event_handler = event_handler

        def run(self):
            observer = Observer()
            observer.schedule(self.event_handler, self.path, recursive=True)
            observer.start()

    def __init__(self, file_manager):
        self.file_manager = file_manager

    def run(self):
        root_path = self.file_manager.file_collection.path_to_user_files
        self.Watcher(root_path, self.WoodysFileManagerHandler(
            self.file_manager)).run()
