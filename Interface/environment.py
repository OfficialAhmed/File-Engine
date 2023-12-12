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

import concurrent.futures

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from datetime import datetime
from controller import Controller
import os, json

class Common:
    """
        COMMON METHODS BETWEEN FEATURES
    """

    def __init__(self) -> None:
        self.constant = Constant()
        
        self.html = Html()
        self.constant = Constant()
        self.controller = Controller()
        self.progressBar = ProgressBar()
        self.controller.update_remover_param()

        self.path_input = ""
        self.cache_file = self.controller.CACHE_FILE

        # CREATE DATA FOLDER IF NOT FOUND
        if not os.path.exists("data"):
            os.mkdir(self.controller.DATA_PATH)

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

    def import_cache(self) -> None:

        # IF CACHE FOUND
        if os.path.exists(self.controller.CACHE_FILE):
            cache: dict = json.load(open(self.cache_file)).get("delete page")

            self.lookupInput.setText(cache.get("lookupInput"))
            self.isRecursive.setChecked(cache.get("IsRecursive"))
            self.currentPathInput.setText(cache.get("currentPath"))
            self.lookupType.setCurrentText(cache.get("lookupType"))

            self.path_input = cache.get("currentPath")

            # UPDATE LOOKUP FORMAT ACCORDING TO THE CACHED LOOKUP TYPE
            self.change_lookup_format()

            self.lookupFormat.setCurrentText(cache.get("lookupFormat"))

    def export_cache(self) -> None:

        # TODO: CHECK IF BOTH CACHES ARE THE SAME, SKIP EXPORTING - NO NEED TO WASTE TIME IN WRITING
        cache = {}

        # IF CACHE FOUND
        if os.path.exists(self.cache_file):
            cache: dict = json.load(open(self.cache_file))

        search = self.lookupInput.text()
        path = self.currentPathInput.text()
        lu_type = self.lookupType.currentText()
        recursive = self.isRecursive.isChecked()
        lu_frmt = self.lookupFormat.currentText()

        cache["delete page"] = {
            "lookupType":   lu_type,
            "currentPath":  path,
            "lookupFormat": lu_frmt,
            "lookupInput":  search,
            "IsRecursive":  recursive,
        }

        with open(self.cache_file, "w+") as file:
            json.dump(cache, file)

    def set_user_path(
        self, path: str,
        is_changed_manually: bool
    ) -> None:
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

    def change_lookup_format(self) -> None:
        """
        Change lookup format options according to the lookup type
        """

        current_type = self.lookupType.currentText()

        # REMOVE ALL TYPES
        self.lookupFormat.clear()

        # GENERATE NEW TYPES
        new_formats = (
            "NAME",
            "PATTERN"
        )

        # ADD THE OPTION 'EXTENSION' IF 'FILES' SELECTED
        if current_type == "FILES":
            new_formats = (
                "NAME",
                "PATTERN",
                "EXTENSION"
            )

        for format in new_formats:
            self.lookupFormat.addItem(format)

    def get_data(self) -> (dict, bool):
        """
        ### Begin lookup process. 
            * Deactivate all btns and reactivate upon end of process 
        """

        input: str = self.lookupInput.text()
        type: str = self.lookupType.currentText()
        format: str = self.lookupFormat.currentText()
        is_recursive: bool = self.isRecursive.isChecked()

        # UPDATE THE FINDER PARAMETERS
        self.controller.update_finder_param(
            self.path_input,
            is_recursive,
        )

        data = {}

        # TERMINATE IF EITHER INPUTS ARE EMPTY
        if not input or not self.path_input:
            self.controller.show_dialog(
                "SEARCH INPUT IS EMPTY!",
                "w",
                is_dialog=False
            )

            return (data, True)                 # FAILED = True

        # TERMINATE IF ENTERED PATH CANNOT BE FOUND
        if not os.path.exists(self.currentPathInput.text()):
            self.controller.show_dialog(
                "FOLDER DOESN'T EXIST. DOUBLE CHECK THE ENTERED PATH",
                "w",
                is_dialog=False
            )

            return (data, True)                 # FAILED = True

        try:
            # SEARCH BY SELECTED FORMAT
            if type == "FILES":
                match format:
                    case "NAME":
                        data = self.controller.get_files_by_name(input)

                    case "EXTENSION":
                        data = self.controller.get_files_by_extension(input)

                    case "PATTERN":
                        data = self.controller.get_files_by_pattern(input)

            elif type == "FOLDERS":
                match format:
                    case "NAME":
                        data = self.controller.get_folders_by_name(input)

                    case "PATTERN":
                        data = self.controller.get_folders_by_pattern(input)

            return (data, False)

        except Exception as e:
            self.controller.show_dialog(
                f"UNKNOWN ERROR OCCURED | {str(e)}",
                "c",
                is_dialog=False
            )

            return (data, True)                 # FAILED = True


    def set_icon(self, widget: QWidget, name: str, size=(18, 18)) -> str:

        widget.setIcon(
            QIcon(f"{self.constant.get_resources_path()}icons/{name}.svg")
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

    def get_progress_unit(
        self,
        total_files: int,
    ) -> float:
        """
            Calculates the shunk to progress in percentage
        """

        return 100 / total_files

    def get_timestamp(self):
        return datetime.now().strftime("%d-%m-%Y %H_%M_%S")


class Constant:

    _RESOURCES_PATH = ":/images/images/"

    @classmethod
    def get_resources_path(self):
        return self._RESOURCES_PATH


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

    def get_rgb_color(self, name: str) -> tuple[int, int, int]:
        return tuple(int(x) for x in self.color.get(name).split(", "))

    def title_span_tag(self, text: str, clr: str = "#ff79c6", f_size: str = "12") -> str:
        return f'<span style="font-size:{f_size}pt; font-weight:600; color:{clr}">{text}</span>'

    def get_credits_page(self) -> str:
        return \
            '<body style="font-family:"Segoe UI"; font-size:10pt; font-weight:400; font-style:normal">\n' +\
            self.p_start +\
            self.title_span_tag(
                "CREDITS"
            ) + self.p_end +\
            self.title_span_tag(
                "MAIN UI DESIGN : Wanderson M. Pimenta", "#ffffff", "9"
            ) + self.p_end +\
            self.title_span_tag(
                "DRACULA THEME: Zeno Rocha", "#ffffff", "9"
            ) + self.p_end +\
            self.title_span_tag(
                "LICENSE"
            ) + self.p_end +\
            self.title_span_tag(
                "https://github.com/OfficialAhmed/File-Engine/blob/main/LICENSE", "#bd93f9", "9"
            ) + self.p_end +\
            self.title_span_tag(
                "DEVELOPER"
            ) + self.p_end +\
            self.title_span_tag(
                "@OfficialAhmed0", "#ffffff", "9"
            ) + self.p_end +\
            self.title_span_tag(
                "GitHub"
            ) + self.p_end +\
            self.title_span_tag(
                "https://github.com/OfficialAhmed/File-Engine", "#bd93f9", "9"
            )+"</p>"


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


"""

====================================================================
        CONCURRENT TECHNIQUES HANDELED IN SEPERATE THREADS
====================================================================

    MEMORY SHARED BETWEEN THREADS USING SIGNALS AND EMITTED UPON SET / READY
    
    * USE SIGNALS TO SHARE DATA BETWEEN THREADS

"""


class Worker(QObject):

    # SIGNALS TO COMMUNICATE TO THE MAIN THREAD
    is_fail = Signal(str)
    is_success = Signal(bool)
    progress_signal = Signal(float)


class DeleteWorker(Worker):
    """
        DELETE FILES IN SEPERATE THREADs FROM THE UI CONCURRENTLY

        - Inherits `QObject` for a thread-safe communicate with the main thread
        through signals with Qt framework
    """

    remove_rows_signal = Signal()

    def __init__(self, files: list, lookup_type: str) -> None:
        super().__init__()
        self.files = files
        self.lookup_type = lookup_type

        self.controller = Controller()

    def process(self, path: str) -> None:

        if self.lookup_type == "FOLDERS":
            # IF NOT EMPTY, ERROR HAS OCCURED
            if self.controller.remove_folder(path, path[:path.rfind("\\")]):
                return False
            return True

        else:
            # IF NOT EMPTY, ERROR HAS OCCURED
            if self.controller.remove_file(path):
                return False
            return True

    def run(self) -> None:
        """
            WORK DECOMPOSITION - SUBTASKS
        """

        try:

            is_all_removed = True

            # 'max_workers' SET TO MAX AVAILABLE CPU CORES
            with concurrent.futures.ThreadPoolExecutor(max_workers=None) as executor:
                futures = [
                    executor.submit(self.process, file)
                    for file in self.files
                ]

                # PROGRESS BAR CALCULATIONS
                completed = 0
                total_files = len(self.files)

                # UPDATE THE PROGRESS BAR, UPON EACH FINISHED PROCESS
                for future in concurrent.futures.as_completed(futures):
                    if future.result():
                        is_all_removed = False

                    completed += 1
                    progress = completed / total_files
                    self.progress_signal.emit(progress)

            # REMOVE ROWS & INVOKE PROCESS SUCESSFUL METHOD
            self.remove_rows_signal.emit()
            self.is_success.emit(is_all_removed)

        except Exception as e:
            self.is_fail.emit(str(e))


class RestoreWorker(Worker):

    def __init__(self, data: dict) -> None:
        super().__init__()

        self.data = data
        self.controller = Controller()

    def process(self, dest_with_filename: str) -> None:

        self.controller.restore_removed_content(
            dest_with_filename
        )

    def run(self) -> None:

        completed = 0
        self.progress_signal.emit(0)

        try:

            is_all_removed = True

            with concurrent.futures.ThreadPoolExecutor(max_workers=None) as executor:
                futures = [
                    executor.submit(self.process, file)
                    for file in self.data.values()
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

            self.controller.empty_trash()
            self.is_success.emit(is_all_removed)

        except Exception as error:
            self.is_fail.emit(str(error))
