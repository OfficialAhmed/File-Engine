"""

============================================================
                SHARED UI CLASSES 
============================================================

    - COMMON USED UI FUNCTIONS
        
        * CLASS `Common`        ->  CONTAIN COMMON UI METHODS
        * CLASS `Constant`      ->  CONTAIN UI CONSTANTS 
        * CLASS `Html`          ->  CONTAIN UI HTML
    ________________________________________________________
    
    - SHARED UI WIDGETS BETWEEN DIFFERENT PAGES
    
        * CLASS `ProgressBar`   ->  SHARED PROGRESSBAR WIDGET
        
    ________________________________________________________
    
    - MULTI THREADING TASKS
    
        * (PARENT) CLASS `Worker`           ->  WORKERS PARENT - HOLD SIGNALS AND COMMON METHODS
            * (CHILD) CLASS `DeleteWorker`  ->  DELETES A LIST OF ITEMS IN PARALLEL
            * (CHILD) CLASS `RestoreWorker` ->  RESTORE A LIST OF ITEMS IN PARALLEL
    
"""

from time import time
from PySide6.QtCore import QSize, QCoreApplication, Signal, QObject
from PySide6.QtGui import QIcon, QPalette, QBrush, QColor, Qt
from PySide6.QtWidgets import (
    QAbstractItemView, QAbstractScrollArea, QFrame, QCheckBox, QTableWidget,
    QWidget, QLineEdit, QComboBox, QPushButton, QFileDialog, QProgressBar, QTableWidgetItem, QLabel
)

from constants import Path, Dialog
from datetime import datetime
from constants import APP_VER

import os
import json
import lib.move as Move
import lib.rename as Rename
import concurrent.futures


class Common:
    """
        COMMON METHODS BETWEEN FEATURES
    """

    def __init__(self) -> None:
        self.html = Html()
        self.dialog = Dialog()
        self.progressBar = ProgressBar()

        self.data = {}

        self.path_input = ""
        self.cache_file = Path.CACHE_FILE

        # CREATE DATA FOLDER IF NOT FOUND
        if not os.path.exists("data"):
            os.mkdir(Path.DATA_PATH)

    def set_controller_widgets(
        self,
        lookupType:            QPushButton,
        currentPath:           QLineEdit,
        lookupFormat:          QLineEdit,
        lookupInput:           QCheckBox,
        isRecursive:           QLineEdit,
        startBtn:              QComboBox
    ):
        """
        Set current window widgets from 'UI' class
        """
        self.startBtn:         QPushButton = startBtn
        self.lookupType:       QComboBox = lookupType
        self.lookupInput:      QLineEdit = lookupInput
        self.isRecursive:      QCheckBox = isRecursive
        self.lookupFormat:     QComboBox = lookupFormat
        self.currentPathInput: QLineEdit = currentPath

    def set_user_path(self, path: str, is_changed_manually: bool) -> None:
        """
        Update user path input
        """

        # RESET USER PATH
        if not path:
            self.path_input = ""
            return

        self.path_input = path

        if not is_changed_manually:
            self.currentPathInput.setText(path)

    def set_icon(self, widget: QWidget, name: str, size=(18, 18)) -> str:

        widget.setIcon(
            QIcon(f"{Path.RESOURCES_PATH}icons/{name}.svg")
        )

        widget.setIconSize(QSize(*size))

    def get_path(self, file_extension="") -> str | None:
        """
            ### RENDER A WINDOW TO GET FILE/FOLDER PATH 

            - IF EXTENSION PROVIDED GET `FILE`, ELSE GET `FOLDER` PATH 
        """

        # ALLOW ONE FILE OF THE GIVEN EXTENSION
        if file_extension:
            path, _ = QFileDialog.getOpenFileName(
                None,
                "PICK A FILE TO CONTINUE",
                "",                                     # PATH ON-WINDOW RENDER
                f"*.{file_extension}",
                options=QFileDialog.Options(),
            )

        # ALLOW FOLDER PATH ONLY
        else:
            path = QFileDialog.getExistingDirectory(
                None,
                "PICK A FOLDER TO CONTINUE",
                "",                                     # PATH ON-WINDOW RENDER
                options=QFileDialog.Options(),
            )

        return path if path else None


class Html:

    COLOR: dict = {
        "dark blue": "33, 37, 43",
        "light blue": "52, 59, 72",
        "dracula pink": "255, 121, 198",
        "dracula purple": "189, 147, 249"
    }

    def __init__(self) -> None:

        self.color = self.COLOR
        self.p_start = '<p align="center" style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">'
        self.p_end = f"</p>{self.p_start}"

    def get_bg_color(self, name: str) -> str:
        return f"background-color: rgb({self.color.get(name)})"

    def get_text_color(self, name: str) -> str:
        return f"color: rgb({self.COLOR.get(name)})"

    def title_span_tag(self, text: str, clr: str = "#ff79c6", f_size: str = "12") -> str:
        return f'<span style="font-size:{f_size}pt; font-weight:600; color:{clr}">{text}</span>'

    def get_credits_page(self) -> str:
        return \
            '<body style="font-family:"Segoe UI"; font-size:10pt; font-weight:400; font-style:normal">\n' +\
            self.p_start + self.title_span_tag("CREDITS") + \
            self.p_end + self.title_span_tag("MAIN UI DESIGN : Wanderson M. Pimenta", "#ffffff", "9") +\
            self.p_end + self.title_span_tag("DRACULA THEME: Zeno Rocha", "#ffffff", "9") +\
            self.p_end + self.title_span_tag("LICENSE") +\
            self.p_end + self.title_span_tag("https://github.com/OfficialAhmed/File-Engine/blob/main/LICENSE", "#bd93f9", "9") +\
            self.p_end + self.title_span_tag("DEVELOPER") +\
            self.p_end + self.title_span_tag("@OfficialAhmed0", "#ffffff", "9") +\
            self.p_end + self.title_span_tag("GitHub") +\
            self.p_end + self.title_span_tag("https://github.com/OfficialAhmed/File-Engine", "#bd93f9", "9") +\
            "</p>"


class ProgressBar:

    # STORE GLOABLY FOR ALL CHILDREN
    progressBar = None

    def update(self, progress: int):
        num = int(progress * 100)
        ProgressBar.progressBar.setValue(num)

    def set_widget(self, widget: QProgressBar):
        """
            #### Called after the progressbar widget rendered 
            * ONE TIME CALL METHOD
            * Widget will be stored in class for reference
        """
        ProgressBar.progressBar = widget


class Table:

    table_headers = (
        "FILE | FOLDER",
        "SOURCE",
        "SIZE (MB)",
        "SELECTED"
    )

    def __init__(self) -> None:
        self.dialog = Dialog()
        self.checkboxes: list[QCheckBox] = []
        self.data_type = "FILES"

        self.last_invoke_time = 0
        self.totalRecordsLabel: QLabel | None = None
        self.data = None

    def set_total_records_widget(self, widget: QLabel):
        self.totalRecordsLabel = widget

    def render(self, tableWidget: QTableWidget, rows=1, columns=4):
        """
            ## RENDER TABLE WITH THE HEADERS ONLY BY DEFAULT
                - CALLED ONCE, AFTER CREATING THE TABLE WIDGET
        """

        self.table = tableWidget

        self.set_specs()

        # CLEAR PREVIOUS ROWS
        self.checkboxes.clear()
        tableWidget.setRowCount(0)

        tableWidget.setRowCount(rows)
        tableWidget.setColumnCount(columns)

        # RENDER TABLE HEADERS
        tableWidget.setHorizontalHeaderLabels(self.table_headers)

        # ON HEADER CLICK
        tableWidget.horizontalHeader().sectionClicked.connect(
            self.header_clicked
        )

        self.retranslate_headers()

    def set_specs(self):

        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.SolidPattern)

        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)

        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)

        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)

        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)

        self.table.setFrameShape(QFrame.NoFrame)
        self.table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setSelectionMode(QAbstractItemView.NoSelection)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setShowGrid(True)
        self.table.setGridStyle(Qt.SolidLine)
        self.table.setSortingEnabled(True)
        self.table.horizontalHeader().setVisible(True)
        self.table.horizontalHeader().setCascadingSectionResizes(True)
        self.table.horizontalHeader().setDefaultSectionSize(200)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setVisible(False)
        self.table.verticalHeader().setCascadingSectionResizes(True)
        self.table.verticalHeader().setHighlightSections(False)
        self.table.verticalHeader().setStretchLastSection(False)

    def fill(self, data: dict):
        """
            SETS THE DATA FOR THE CURRENT ACCESSED OBJECT AND POPULATES THE TABLE WITH THAT
            - THIS SHOULD BE CALLED BEFORE CALLING ANY METHOD THAT REQUIRES THE DATA
        """

        self.data = data
        data = data.values()

        # RENDER TABLE HEADERS
        self.render(
            self.table, len(data)
        ) if self.data else self.render(
            self.table
        )

        # POPULATE THE TABLE WITH DATA
        for row_index, row_data in enumerate(data):

            for col_index, (_, value) in enumerate(row_data.items()):

                item = QTableWidgetItem(str(value))
                self.table.setItem(row_index, col_index, item)

                # RENDER CHECK ITEMS FOR EACH TABLE-ROW
                if col_index == 2:

                    checkbox = QCheckBox()
                    checkbox.setChecked(True)

                    self.table.setCellWidget(
                        row_index,                      # ROW INDEX
                        3,                              # LAST COLUMN
                        checkbox                        # ITEM
                    )

                    self.checkboxes.append(checkbox)

        # RESIZE COLUMNS - BASED ON CONTENT SIZE
        for col_index in range(self.table.columnCount()):
            self.table.resizeColumnToContents(col_index)

    def retranslate_headers(self):

        for col, txt in enumerate(self.table_headers):

            header_item = QTableWidgetItem(
                QCoreApplication.translate("MainWindow", txt)
            )

            self.table.setHorizontalHeaderItem(col, header_item)

    def header_clicked(self, header_section: int) -> None:
        """
        ### ON TABLE HEADER CLICK 

            Zero-indexed header
            * On click header `0` `1` `2` -> re-render checkboxes
            * On click header `3`         -> (De)Select Checkboxes
        """

        if header_section == 3:

            # A FIX TO RESTRICT MULTIPLE METHOD INVOKES: A BUG RELATED TO SECTIONCLICK
            if time() - self.last_invoke_time >= 0.08:

                # SELECT/DESELCT ALL CHECKBOXES
                for checkbox in self.checkboxes:
                    checkbox.toggle()

        else:

            # RE-RENDER TABLE CHECKBOXES TO REARRANGE THEM BASED ON THE NEW SORT
            total_checkboxes = len(self.checkboxes)
            self.checkboxes.clear()

            for row_indx in range(total_checkboxes):

                checkbox = QCheckBox()
                checkbox.setChecked(False)

                self.table.setCellWidget(
                    row_indx,                            # ROW INDEX
                    3,                                   # LAST COLUMN
                    checkbox                             # ITEM
                )

                self.checkboxes.append(checkbox)

        self.last_invoke_time = time()

    def remove_rows(self, rows: list, total_entries_label: QLabel) -> None:
        """
            DELETE ALL CHECKED ROWS AFTER REMOVING THE FILES
        """

        if not rows:
            self.dialog.show(
                "NO DATA HAS BEEN SELECTED", is_dialog=False
            )
            return None

        # REMOVE SELECTED CHECKBOXES
        for row in reversed(rows):
            self.table.removeRow(row)
            self.checkboxes.pop(row)

        total_entries_label.setText(str(len(self.checkboxes)))

    def get_path(self, file_extension="") -> str | None:
        """
            ### RENDER A WINDOW TO GET FILE/FOLDER PATH 

            - IF EXTENSION PROVIDED GET `FILE`, ELSE GET `FOLDER` PATH 
        """

        # ALLOW ONE FILE OF THE GIVEN EXTENSION
        if file_extension:
            path, _ = QFileDialog.getOpenFileName(
                None,
                "PICK A FILE TO CONTINUE",
                "",                                     # PATH ON-WINDOW RENDER
                f"*.{file_extension}",
                options=QFileDialog.Options(),
            )

        # ALLOW FOLDER PATH ONLY
        else:
            path = QFileDialog.getExistingDirectory(
                None,
                "PICK A FOLDER TO CONTINUE",
                "",                                     # PATH ON-WINDOW RENDER
                options=QFileDialog.Options(),
            )

        return path if path else None

    def export_process_clicked(self) -> None:
        """
        EXPORT CURRENT DATA FOR LATER USE (FOR THE LOADING PROCESS)
        """

        # IF NO DATA HAS BEEN FOUND, RETURN
        if not self.data:
            self.dialog.show(
                f"NOTHING TO EXPORT! PLEASE START THE SEARCH PROCESS FIRST",
                "I",
                is_dialog=False
            )

            return None

        # GET FILE DESTINATION
        folder_path = self.get_path()
        path = f"{folder_path}\\{datetime.now().strftime('%d-%m-%Y %H_%M_%S')}.json"

        if folder_path:

            with open(path, "w") as file:
                json.dump(
                    {
                        "data": self.data,
                        "meta": {"TITLE": "File Engine", "V": APP_VER}
                    },
                    file
                )

            # CHECK IF FILE EXPORTED SUCCESSFULLY
            if os.path.exists(path) and os.path.getsize(path) > 0:
                self.dialog.show(
                    f"PROCESS EXPORTED SUCCESSFULLY!",
                    "I",
                    is_dialog=False
                )

            else:
                self.dialog.show(
                    f"SOMETHING WENT WRONG! PROCESS WASN'T EXPORTED. PLEASE TRY AGAIN!",
                    "C",
                    is_dialog=False
                )

    def import_process_clicked(self) -> None:
        """
            OVERWRITE THE DATA FROM A JSON FILE GENERATED BY THE EXPORT METHOD
            THEN POPULATE THE DATA ONTO A NEW GENERATED TABLE
        """

        file = self.get_path("json")

        if not file:
            return None

        memory: dict = json.load(open(file))

        # READ ONLY FILE ENGINE EXPORTED JSON
        if "meta" in memory and "data" in memory:
            if memory.get("meta").get("TITLE") == "File Engine":
                self.data = memory.get("data")
                self.totalRecordsLabel.setText(str(len(self.data)))
                self.fill(self.data)
                return None

        # COULDN'T READ JSON
        self.dialog.show(
            f"INVALID PROCESS FILE.",
            "I",
            is_dialog=False
        )


# TABLES ACCESSABLE ANY WHERE AFTER IMPORTING
tables = {
    "SEARCH": Table(),
    "DELETE": Table(),
    "RENAME": Table(),
    "MOVE": Table()
}


"""

====================================================================
        CONCURRENT TECHNIQUES HANDELED IN SEPERATE THREADS
====================================================================

    MEMORY SHARED BETWEEN THREADS USING SIGNALS AND EMITTED UPON SET / READY
    
    * USE SIGNALS TO SHARE DATA BETWEEN THREADS

"""


class Worker(QObject):

    # SIGNALS TO COMMUNICATE TO THE MAIN THREAD
    failed_signal = Signal(str)
    progress_signal = Signal(float)
    is_success_signal = Signal(bool)

    def __init__(self) -> None:
        super().__init__()

        self.FILE_MOVER = Move.File()
        self.FOLDER_MOVER = Move.Folder()

    def empty_trash(self) -> None:
        self.FILE_MOVER.empty_trash()


class MoveWorker(Worker):
    """
        MVOE FILES IN SEPERATE THREADs FROM THE UI CONCURRENTLY

        - Inherits `QObject` for a thread-safe communicate with the main thread
        through signals with Qt framework
    """

    remove_rows_signal = Signal()

    def __init__(self, files: list, lookup_type: str) -> None:
        super().__init__()

        self.files = files
        self.lookup_type = lookup_type

    def process(self, path: str) -> bool:

        if self.lookup_type == "FOLDERS":
            if self.FOLDER_MOVER.move(path, self.dest_folder):
                return False
        else:
            if self.FILE_MOVER.move(path, self.dest_folder):
                return False

        return True

    def run(self, dest_folder="trash", method="delete") -> None:
        """
            #### START TO SUBTASK 

                `dest_folder` THE FOLDER TO WHICH THE FILES ARE GOING TO BE MOVED INTO. `DEFAULT: TRASH`
        """

        self.dest_folder = dest_folder

        if self.files:

            if method == "delete":
                self.FILE_MOVER.set_mover_param(
                    Path.TRASH_CONTENT_FILE,
                    Path.TRASH_PATH,
                    method
                )

                self.FOLDER_MOVER.set_mover_param(
                    Path.TRASH_CONTENT_FILE,
                    Path.TRASH_PATH,
                    method
                )

            else:
                self.FILE_MOVER.set_mover_param(
                    content_file_path=Path.MOVED_CONTENT_FILE,
                    method=method
                )

                self.FOLDER_MOVER.set_mover_param(
                    content_file_path=Path.MOVED_CONTENT_FILE,
                    method=method
                )

            try:

                # 'max_workers' SET TO MAX AVAILABLE CPU CORES
                with concurrent.futures.ThreadPoolExecutor(max_workers=None) as executor:
                    tasks = [
                        executor.submit(self.process, file)
                        for file in self.files
                    ]

                    # PROGRESS BAR CALCULATIONS
                    completed = 0
                    total_files = len(self.files)
                    is_moved_all = True

                    # UPDATE THE PROGRESS BAR, UPON EACH FINISHED PROCESS
                    for task in concurrent.futures.as_completed(tasks):

                        if not task.result():
                            is_moved_all = False

                        completed += 1
                        progress = completed / total_files
                        self.progress_signal.emit(progress)

                    # REMOVE TABLE ROWS & INVOKE PROCESS SUCESSFUL METHOD
                    self.remove_rows_signal.emit()
                    self.is_success_signal.emit(is_moved_all)

            except Exception as e:
                self.failed_signal.emit(str(e))


class RestoreWorker(Worker):

    def __init__(self, data: dict) -> None:
        super().__init__()

        self.data = data

    def process(self, src, dest) -> None:

        if self.restore_method == "deleted":
            self.FILE_MOVER.restore_deleted(src)
        else:
            self.FILE_MOVER.restore_moved(src, dest)
        self.FILE_MOVER.moved_content.clear()

    def restore(self, restore_method: str) -> None:

        self.restore_method = restore_method

        completed = 0
        self.progress_signal.emit(0)

        try:

            is_all_removed = True

            with concurrent.futures.ThreadPoolExecutor(max_workers=None) as executor:
                futures = [
                    executor.submit(self.process, src, dest)
                    for dest, src in self.data.items()
                ]

                # PROGRESS BAR CALCULATIONS
                completed = 0
                total_data = len(self.data)

                # UPDATE THE PROGRESS BAR, UPON EACH FINISHED PROCESS
                for future in concurrent.futures.as_completed(futures):

                    if future.result():
                        is_all_removed = False

                    completed += 1
                    progress = completed / total_data
                    self.progress_signal.emit(progress)

            if self.restore_method == "deleted":
                self.empty_trash()
            self.is_success_signal.emit(is_all_removed)

        except Exception as error:
            self.failed_signal.emit(str(error))


class RenameWorker(Worker):

    remove_rows_signal = Signal()

    def __init__(self, files: list, renaming_algo: str, renaming_method: str, custom_value: str) -> None:
        super().__init__()

        self.files = files
        self.renaming_algo = renaming_algo
        self.renaming_method = renaming_method
        self.data_type = tables["RENAME"].data_type     # FILES OR FOLDERS

        self.FILE_RENAME = Rename.File()
        self.FOLDER_RENAME = Rename.Folder()

        self.FILE_RENAME._set_renaming_param(
            content_file_path=Path.TRASH_CONTENT_FILE,
            trash_folder_path=Path.TRASH_PATH,
            renaming_method=renaming_method,
            renaming_algo=renaming_algo,
            custom_val=custom_value,
            files=files
        )

        self.FOLDER_RENAME._set_renaming_param(
            content_file_path=Path.TRASH_CONTENT_FILE,
            trash_folder_path=Path.TRASH_PATH,
            renaming_method=renaming_method,
            renaming_algo=renaming_algo,
            custom_val=custom_value,
            files=files
        )

        # CONVERT STR TO INT IF ITS A DIGIT
        self.custom_value = int(custom_value) if custom_value.isdigit() else 0

    def process(self, path: tuple) -> bool:
        """ 
            RENAMING FILES METHOD INVOKED BY THE THREADS 
        """

        try:
            os.rename(path[0], path[1])
            return True
        except:
            return False

    def run(self) -> None:

        if self.files:

            try:

                handler: Rename.File | Rename.Folder = self.FILE_RENAME if self.data_type == "FILES" else self.FOLDER_RENAME

                match self.renaming_algo:
                    case "BULK":
                        new_titles = handler.get_bulk_titles()
                    case "TIMESTAMP":
                        new_titles = handler.get_timestamp_titles()

                # 'max_workers' SET TO MAX AVAILABLE CPU CORES
                with concurrent.futures.ThreadPoolExecutor(max_workers=None) as executor:
                    tasks = [
                        executor.submit(self.process, titles)
                        for titles in new_titles
                    ]

                    # PROGRESS BAR CALCULATIONS
                    completed = 0
                    total_titles = len(new_titles)
                    is_renamed_all = True

                    # UPDATE THE PROGRESS BAR, UPON EACH FINISHED PROCESS
                    for task in concurrent.futures.as_completed(tasks):

                        if not task.result():
                            is_renamed_all = False

                        completed += 1
                        progress = completed / total_titles
                        self.progress_signal.emit(progress)

                    # REMOVE ROWS & INVOKE PROCESS SUCESSFUL METHOD
                    self.remove_rows_signal.emit()
                    self.is_success_signal.emit(is_renamed_all)

            except Exception as e:
                self.failed_signal.emit(str(e))
