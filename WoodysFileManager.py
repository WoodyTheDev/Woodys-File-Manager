import sys
import traceback
import os
import shutil
import subprocess
import ctypes

# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler

from WoodysFileWatcher import WoodysFileWatcher

from PySide6.QtCore import Qt, QSize, QCoreApplication, QRunnable, Slot, Signal, QObject, QThreadPool
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QTableWidgetItem, QTableWidget, QTreeWidgetItem, QLabel,
    QPushButton, QWidget, QHBoxLayout, QComboBox, QAbstractItemView)
from PySide6.QtGui import QCursor, QFont, QIcon, QBrush, QPalette, QColor
from spinner import WaitingSpinner
from WoodysFileManager_ui import Ui_MainWindow
from FileCollection import FileCollection


class WoodysFileManager(QMainWindow, Ui_MainWindow):
    file_collection: FileCollection
    search_path = ""
    subcategory_widgets = []
    spinner = None

    def __init__(self):
        def init_table_widget_column_sizes():
            # displayFilesTableWidget
            self.displayFilesTableWidget.setColumnWidth(0, 400)
            self.displayFilesTableWidget.setColumnWidth(1, 100)
            self.displayFilesTableWidget.setColumnWidth(2, 200)
            self.displayFilesTableWidget.setColumnWidth(3, 95)
            # unsortedFilesTableWidget
            self.unsortedFilesTableWidget.setColumnWidth(0, 400)
            self.unsortedFilesTableWidget.setColumnWidth(1, 100)
            self.unsortedFilesTableWidget.setColumnWidth(2, 200)
            self.unsortedFilesTableWidget.setColumnWidth(3, 95)

        super().__init__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        myappid = 'woodythedev.woodysfilemanager.1'  # arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        self.setWindowIcon(QIcon(u":/images/icon/woody-the-dev.svg"))
        self.setupUi(self)
        init_table_widget_column_sizes()

    def init_display_files_page(self):
        self.exactPathCheckBox.setChecked(True)
        self.refresh_category_tree()

    def init_sort_files_page(self):
        self.refreshUnsortedFilesTable()
        self.insert_category_comboBox(
            self.file_collection.path_to_user_files, self.categoryComboBox)

    def init_spinner(self):
        self.spinner = WaitingSpinner(
                parent=self.page_5,
                roundness=100.0,
                fade=88.73,
                radius=25,
                lines=84,
                line_length=12,
                line_width=8,
                speed=0.9100000000000001,
                color=QColor(84, 159, 176)
            )
        self.spinner.start()
        
    def init_file_collection(self, progress_callback):
        self.file_collection = FileCollection(self.windowTitle())
        WoodysFileWatcher(self).run()

    def finished_file_collection(self):
        self.mainStackedWidget.setCurrentIndex(0)
        self.supportStackedWidget.setCurrentIndex(0)
        self.init_display_files_page()
        self.init_sort_files_page()
        self.spinner.stop()

    def insert_category_comboBox(self, top_category, comboBox: QComboBox):
        main_categories = self.file_collection.dir_tree[top_category]
        for category in main_categories:
            comboBox.addItem(category, category)

    # ToDo: refresh category disappears sometimes when folder is added/changed through file explorer.
    def refresh_category_tree(self):
        self.file_collection.refresh_dir_tree()
        # Add children recursive

        def add_children(node: QTreeWidgetItem, key):
            for child in self.file_collection.dir_tree[key]:
                child_node = QTreeWidgetItem([child])
                child_key = key + os.path.sep + child
                child_node.setData(0, Qt.ItemDataRole.UserRole, child_key)
                node.addChild(child_node)
                add_children(child_node, child_key)

        key = self.file_collection.path_to_user_files
        root = QTreeWidgetItem([os.path.basename(key)])
        root.setData(0, Qt.ItemDataRole.UserRole, key)
        add_children(root, key)
        self.categoryTreeWidget.clear()
        self.categoryTreeWidget.addTopLevelItem(root)
        self.categoryTreeWidget.resizeColumnToContents(0)

        # ToDo: bugfix so that expand works with watcher/file explorer too.
        # logs error but works with sort button.
        # QBasicTimer::start: QBasicTimer can only be used with threads started with QThread.
        # Further error when tried with QTimer.
        # QObject: Cannot create children for a parent that is in a different thread.
        # (Parent is WoodysFileManager(0x1b9aff98560), parent's thread is QThread(0x1b9af2ea9d0), current thread is QThread(0x1b9b07eda20)
        root.setExpanded(True)

    def refresh_table_widget(self, results, table_widget: QTableWidget):
        table_widget.setRowCount(0)
        for hit in results:
            rowPosition = table_widget.rowCount()
            table_widget.insertRow(rowPosition)
            file_name_item = QTableWidgetItem(hit["file_name"])
            file_name_item.setData(
                Qt.ItemDataRole.UserRole, hit["path_with_file_name"])
            table_widget.setItem(
                rowPosition, 0, file_name_item)
            file_size_item = QTableWidgetItem(str(hit["file_size"]) + " KB")
            file_size_item.setTextAlignment(Qt.AlignTrailing | Qt.AlignVCenter)
            table_widget.setItem(
                rowPosition, 1, file_size_item)
            table_widget.setItem(
                rowPosition, 2, QTableWidgetItem(hit["file_type"]))
            table_widget.setItem(
                rowPosition, 3, QTableWidgetItem(hit["last_modified"].isoformat(
                    sep=" ", timespec="seconds")))

    def search(self):
        return self.file_collection.search(
            self.search_path,
            self.searchLineEdit.text(),
            self.exactPathCheckBox.checkState() == Qt.CheckState.Unchecked)

    def search_and_display_files(self):
        self.refresh_table_widget(
            self.search(), self.displayFilesTableWidget)

    def refreshUnsortedFilesTable(self):
        self.refresh_table_widget(self.file_collection.search(
            "", "", True), self.unsortedFilesTableWidget)

    def get_unsorted_files_table_scroll_positions(self):
        scroll_positions = {}
        scroll_positions["x"] = self.unsortedFilesTableWidget.horizontalScrollBar(
        ).value()
        scroll_positions["y"] = self.unsortedFilesTableWidget.verticalScrollBar(
        ).value()
        return scroll_positions

    def get_display_files_table_scroll_positions(self):
        scroll_positions = {}
        scroll_positions["x"] = self.displayFilesTableWidget.horizontalScrollBar(
        ).value()
        scroll_positions["y"] = self.displayFilesTableWidget.verticalScrollBar(
        ).value()
        return scroll_positions

    # camelCase cause QT Designer uses it like that

    # Window Slots
    def onWindowCloseClicked(self):
        self.close()

    def onWindowMinimizeClicked(self):
        self.showMinimized()

    def mousePressEvent(self, event):
        self.current_position = self.mapToGlobal(event.position())

    def mouseMoveEvent(self, event):
        new_position = self.mapToGlobal(event.position())
        movement = new_position - self.current_position
        self.setGeometry(
            self.mapToGlobal(movement).x(),
            self.mapToGlobal(movement).y(),
            self.width(),
            self.height()
        )
        self.current_position = new_position

    # Navigation Slots
    def onUnsortOverviewClicked(self):
        self.mainStackedWidget.setCurrentIndex(2)
        self.supportStackedWidget.setCurrentIndex(2)

        styleSheet = self.overviewButton.styleSheet()

        styleSheet = styleSheet.replace(
            "padding-right: 3px;", "padding-right: 0px;")
        styleSheet = styleSheet.replace(
            "border-left: 3px solid rgb(84, 159, 176);", "border-left: 0px solid rgb(84, 159, 176);")
        self.overviewButton.setStyleSheet(styleSheet)

        styleSheet = self.unsortOverviewButton.styleSheet()
        styleSheet = styleSheet.replace(
            "padding-right: 0px;", "padding-right: 3px;")
        styleSheet = styleSheet.replace(
            "border-left: 0px solid rgb(84, 159, 176);", "border-left: 3px solid rgb(84, 159, 176);")
        self.unsortOverviewButton.setStyleSheet(styleSheet)

    def onOverviewClicked(self):
        self.mainStackedWidget.setCurrentIndex(0)
        self.supportStackedWidget.setCurrentIndex(0)

        styleSheet = self.overviewButton.styleSheet()
        styleSheet = styleSheet.replace(
            "padding-right: 0px;", "padding-right: 3px;")
        styleSheet = styleSheet.replace(
            "border-left: 0px solid rgb(84, 159, 176);", "border-left: 3px solid rgb(84, 159, 176);")

        self.overviewButton.setStyleSheet(styleSheet)

        styleSheet = self.unsortOverviewButton.styleSheet()
        styleSheet = styleSheet.replace(
            "padding-right: 3px;", "padding-right: 0px;")
        styleSheet = styleSheet.replace(
            "border-left: 3px solid rgb(84, 159, 176);", "border-left: 0px solid rgb(84, 159, 176);")
        self.unsortOverviewButton.setStyleSheet(styleSheet)

    # Action Slots
    def onFileItemDoubleClicked(self, item):
        # Check if Windows or Unix
        if os.name == "nt":
            os.startfile(item.data(Qt.ItemDataRole.UserRole))
        else:
            subprocess.call(["xdg-open", item.data(Qt.ItemDataRole.UserRole)])

    def onSearchClicked(self):
        self.search_and_display_files()

    def onSearchLineEnterPressed(self):
        self.search_and_display_files()

    def onCategoryTreeCurrentItemChange(self, item):
        self.search_path = item.data(0, Qt.ItemDataRole.UserRole)
        self.searchLineEdit.setText("")
        self.search_and_display_files()

    def onExactPathCheckBoxStateChange(self, state):
        self.search_and_display_files()

    def onUnsortedFilesTableSelectionChange(self):
        # Set first selected filename to textEdit
        selected_rows = self.unsortedFilesTableWidget.selectionModel().selectedRows()
        if len(selected_rows) > 0:
            model = self.unsortedFilesTableWidget.model()
            self.sortFilenameLineEdit.setText(model.data(selected_rows[0]))
            # If more than 1 selected row then enable all files checkbox
            if len(selected_rows) > 1:
                self.allFilesCheckBox.setEnabled(True)
            else:
                self.allFilesCheckBox.setEnabled(False)

    def reselect_remaining_rows_unsorted_files_table(self, selected_rows):
        # Reselect remaining rows
        if len(selected_rows) > 1:
            selected_rows.pop()
            self.unsortedFilesTableWidget.setSelectionMode(
                QAbstractItemView.MultiSelection)
            for row in selected_rows:
                self.unsortedFilesTableWidget.selectRow(row.row())
            self.unsortedFilesTableWidget.setSelectionMode(
                QAbstractItemView.ExtendedSelection)

    def onFileSortClicked(self):
        selected_rows = self.unsortedFilesTableWidget.selectionModel().selectedRows()
        if len(selected_rows) > 0:
            # Determine destination path from categories
            dest_path = self.file_collection.path_to_user_files + \
                os.path.sep + self.categoryComboBox.currentText()
            for i, sub_category in enumerate(self.subcategory_widgets):
                sub_category_text = sub_category.findChild(
                    QComboBox, u"subcategoryComboBox_" + str(i + 1)).currentText()
                if sub_category_text != "":
                    dest_path = dest_path + os.path.sep + sub_category_text
            # Make directories if dest_path does not exist
            # if os.path.exists(dest_path) == False:
            os.makedirs(dest_path, exist_ok=True)

            # Move file to new destination, update index and refresh table
            model = self.unsortedFilesTableWidget.model()
            # All selected files in one go
            if self.allFilesCheckBox.checkState() == Qt.CheckState.Checked:
                for row in selected_rows:
                    source_path = model.data(row, Qt.ItemDataRole.UserRole)
                    dest_file_path = dest_path + os.path.sep + model.data(row)
                    shutil.move(source_path, dest_file_path)
            # First selected file
            else:
                row = selected_rows[0]
                source_path = model.data(row, Qt.ItemDataRole.UserRole)
                file_name = self.sortFilenameLineEdit.text()
                file_name_split = os.path.splitext(file_name)
                # If user typed no extension then use old extension
                if file_name_split[1] == "":
                    file_name = file_name + os.path.splitext(source_path)[1]
                dest_file_path = dest_path + os.path.sep + file_name
                shutil.move(source_path, dest_file_path)

    def onAddSubcategoryClicked(self):
        self.add_subcategory_selection()

    def onMinusSubcategoryClicked(self, widget: QWidget):
        frame_height = self.frame_category_choosing.height()
        label_plus_widget_height = 65
        for i in reversed(range(len(self.subcategory_widgets))):
            subcategory_widget = self.subcategory_widgets[i]
            self.frame_category_choosing.findChild(
                QLabel, u"subcategoryLabel_" + str(i + 1)).deleteLater()
            self.subcategory_widgets.remove(subcategory_widget)
            subcategory_widget.deleteLater()
            # Resize scrollarea
            frame_height = frame_height - label_plus_widget_height
            if frame_height < 260:
                self.categoryScrollArea.setFixedHeight(frame_height)
            if subcategory_widget == widget:
                break

    # Utility slots
    def onCategoryTreeExpandToggle(self, item):
        self.categoryTreeWidget.resizeColumnToContents(0)

    # GUI
    def add_subcategory_selection(self):
        # Create subcategory label
        subcategory_label = QLabel(self.frame_category_choosing)
        subcategory_label.setObjectName(
            u"subcategoryLabel_" + str(len(self.subcategory_widgets) + 1))
        font = QFont()
        font.setPointSize(12)
        subcategory_label.setFont(font)
        subcategory_label.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        subcategory_label.setText(QCoreApplication.translate(
            "MainWindow", u"Unterkategorie " + str(len(self.subcategory_widgets) + 1), None))

        # Add subcategory label to frame/scrollarea
        self.frame_category_choosing.layout().addWidget(subcategory_label)

        # Create subcategory widget
        widget_subcategory = QWidget(self.frame_category_choosing)
        widget_subcategory.setObjectName(
            u"widget_" + str(len(self.subcategory_widgets) + 1))
        horizontal_layout = QHBoxLayout(widget_subcategory)
        horizontal_layout.setObjectName(
            u"subcategoryHorizontalLayout_" + str(len(self.subcategory_widgets) + 1))
        horizontal_layout.setContentsMargins(0, 0, 0, 0)

        # Create combobox
        subcategory_comboBox = QComboBox(widget_subcategory)
        subcategory_comboBox.setObjectName(
            u"subcategoryComboBox_" + str(len(self.subcategory_widgets) + 1))
        subcategory_comboBox.setMinimumSize(QSize(189, 32))
        subcategory_comboBox.setMaximumSize(QSize(189, 32))
        subcategory_comboBox.setIconSize(QSize(32, 32))
        subcategory_comboBox.setEditable(True)
        subcategory_comboBox.setContentsMargins(0, 0, 0, 0)

        # Insert data into combobox if previous has data
        top_category = self.categoryComboBox.currentData(
            Qt.ItemDataRole.UserRole)
        if top_category != "":
            top_category = self.file_collection.path_to_user_files + os.path.sep + top_category
            for i, sub_category in enumerate(self.subcategory_widgets):
                previous_subcategory_combobox = sub_category.findChild(
                    QComboBox, u"subcategoryComboBox_" + str(i + 1))
                subcategory_combobox_data = previous_subcategory_combobox.currentData(
                    Qt.ItemDataRole.UserRole)
                if subcategory_combobox_data is not None and subcategory_combobox_data != "":
                    top_category = top_category + os.path.sep + subcategory_combobox_data
            self.insert_category_comboBox(top_category, subcategory_comboBox)

        # Add combobox to widget
        horizontal_layout.addWidget(subcategory_comboBox)

        # Create minus button
        minus_push_button = QPushButton(widget_subcategory)
        minus_push_button.setObjectName(
            u"subcategoryMinusPushButton_" + str(len(self.subcategory_widgets) + 1))
        minus_push_button.setMaximumSize(QSize(32, 32))
        minus_push_button.setCursor(QCursor(Qt.PointingHandCursor))
        minus_push_button.setStyleSheet(u"QPushButton {\n"
                                        "	background-color: rgba(84,159,176,0);\n"
                                        "}")
        icon = QIcon()
        icon.addFile(u"icon/minus-solid.svg",
                     QSize(), QIcon.Normal, QIcon.Off)
        minus_push_button.setIcon(icon)
        minus_push_button.setIconSize(QSize(24, 24))

        minus_push_button.clicked.connect(
            lambda: self.onMinusSubcategoryClicked(widget_subcategory))

        # Add button to widget
        horizontal_layout.addWidget(minus_push_button)

        # Add widget to frame/scrollarea
        self.frame_category_choosing.layout().addWidget(
            widget_subcategory, 0, Qt.AlignLeft)

        # Resize scrollarea
        label_plus_widget_height = 65
        new_scroll_area_height = self.categoryScrollArea.height() + label_plus_widget_height
        if new_scroll_area_height > 260:
            new_scroll_area_height = 260
        self.categoryScrollArea.setFixedHeight(new_scroll_area_height)

        # Add widget to list variable
        self.subcategory_widgets.append(widget_subcategory)

class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data

    error
        tuple (exctype, value, traceback.format_exc() )

    result
        object data returned from processing, anything

    progress
        int indicating % progress

    '''
    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(int)




class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        # Add the callback to our kwargs
        self.kwargs['progress_callback'] = self.signals.progress

    @Slot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''

        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done

if __name__ == '__main__':
    app = QApplication(sys.argv)
    file_manager = WoodysFileManager()
    file_manager.show()
    file_manager.init_spinner()
    threadpool = QThreadPool()
    worker = Worker(file_manager.init_file_collection)
    worker.signals.finished.connect(file_manager.finished_file_collection)
    threadpool.start(worker)
    app.exec()
        