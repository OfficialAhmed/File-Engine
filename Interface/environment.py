"""

============================================================
                SHARED UI CLASSES 
============================================================

    - COMMON USED UI FUNCTIONS
        
        * CLASS `Common`       ->  CONTAIN COMMON UI METHODS
        * CLASS `Constant`     ->  CONTAIN UI CONSTANTS 
        * CLASS `Html`         ->  CONTAIN UI HTML
    ________________________________________________________
    
    - SHARED UI WIDGETS BETWEEN DIFFERENT PAGES
    
        * CLASS `ProgressBar`  ->  SHARED PROGRESSBAR WIDGET
        
    ________________________________________________________
    
    - MULTI THREADING TASKS
    
        * CLASS `DeleteWorker` ->  DELETES A LIST OF FILES IN PARALLEL
    
"""

import concurrent.futures

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from controller import Controller


class Common:

    def __init__(self) -> None:
        self.constant = Constant()

    def set_icon(self, widget: QWidget, name: str, size=(18, 18)) -> str:

        widget.setIcon(
            QIcon(f"{self.constant.get_resources_path()}icons/{name}.svg")
        )

        widget.setIconSize(QSize(*size))

    def get_user_path(self) -> str | None:
        """
        Render a window to select the path
        """

        options = QFileDialog.Options()
        dialog = QFileDialog()
        dialog.setOptions(options)

        path = QFileDialog.getExistingDirectory(
            None,
            "PICK A FOLDER TO CONTINUE",
            "",  # PATH ON-WINDOW RENDER
            options=options,
        )

        # RETURN THE DIRECTORY PATH, OTHERWISE RETURN NONE
        return path if path else None

    def get_progress_unit(
        self,
        total_files: int,
    ) -> float:
        """
            Calculates the shunk to progress in percentage
        """

        return 100 / total_files


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

    def get_bg_color(self, name: str) -> str:
        return f"background-color: rgb({self.color.get(name)})"

    def get_rgb_color(self, name: str) -> tuple[int, int, int]:
        return tuple(int(x) for x in self.color.get(name).split(", "))


class ProgressBar:

    # STORE GLOABLY FOR ALL CHILDREN
    progressBar = None

    def update(self, progress: int):
        self.progressBar.setValue(int(progress * 100))

    def set_widget(self, widget: QProgressBar):
        """
            #### Called after the progressbar widget rendered 
            * ONE TIME CALL METHOD
            * Widget will be stored in class for reference
        """
        self.progressBar = widget
        ProgressBar.progressBar = widget  # Reference


"""

============================================================
    MULTI-THREADING TECHNIQUES HANDELED BY QT FRAMEWORK
============================================================

    MEMORY SHARED BETWEEN THREADS USING SIGNALS AND EMITTED UPON SET / READY
    
    * ALL CLASSES INHERIT 'QThread'
    * ALL CLASSES HAS 'Run' METHOD -> AUTO INVOKED
    
    * USE SIGNALS TO SHARE MEM BY EMITTING IT 

"""


# class DeleteWorker(QThread):
#     """
#         DELETE FILES IN A SEPERATE THREAD FROM THE UI
#     """

# SIGNALS TO COMMUNICATE TO THE MAIN THREAD
# is_file_signal = Signal()
# removed_rows_signal = Signal(list)
# update_progress_signal = Signal(float)

# def __init__(self, data: dict, checkboxes: list, lookup_type: str):
#     super().__init__()

#     self.data = data
#     self.checkboxes = checkboxes
#     self.lookup_type = lookup_type

#     self.controller = Controller()

#     print(f"Files: {self.data}")

# def run(self):
#     """
#         AUTOMATICALLY INVOKED WHEN thread.start() IS CALLED
#     """

#     removed_rows = []
#     total_items = len(self.data)
#     completed_items = 0

#     for index, checkbox in enumerate(self.checkboxes):

#         # REMOVE CHECKED ITEMS FROM THE TABLE
#         if checkbox.isChecked():

#             data: dict = self.data.get(index)
#             content_root = data.get("root")

#             if self.lookup_type == "FOLDERS":

#                 folder = data.get("folder")

#                 self.controller.remove_folder(
#                     f"{content_root}\\{folder}",
#                     folder
#                 )

#             else:

#                 file = data.get("file")

#                 self.controller.remove_file(
#                     f"{content_root}\\{file}"
#                 )

#             print(f"Deleted...{data}")
#             removed_rows.append(index)
#             self.data.pop(index)

#         # UPDATE PROGRESS BAR BY EMITING THE SIGNAL IN THE MAIN THREAD
#         completed_items += 1
#         progress = completed_items / total_items
#         self.update_progress_signal.emit(progress)

#     # SIGNAL A LIST OF REMOVED ROWS TO REMOVE THEM FROM THE UI
#     self.removed_rows_signal.emit(removed_rows)
#     self.is_file_signal.emit()

class DeleteWorker(QObject):

    is_file_signal = Signal()
    progress_signal = Signal(float)
    removed_rows_signal = Signal(list)

    def __init__(self, data: dict, checkboxes: list, lookup_type: str, max_threads=2):
        super().__init__()
        self.data = data
        self.checkboxes = checkboxes
        self.max_threads = max_threads
        self.lookup_type = lookup_type

        self.controller = Controller()

    def process(self, path: str):

        if self.lookup_type == "FOLDERS":
            self.controller.remove_folder(path, path[:path.rfind("\\")])
            print(f"Deleting {path}")

        else:
            self.controller.remove_file(path)
            print(f"Deleting {path}")

    def run(self):

        self.files = []
        removed_rows = []
        self.progress_signal.emit(0)

        # GET SELECTED ITEMS FROM THE TABLE
        for indx, checkbox in enumerate(self.checkboxes):

            if checkbox.isChecked():

                file = self.data.get(indx).get("file")
                content_root = self.data.get(indx).get("root")
                self.files.append(f"{content_root}//{file}")
                removed_rows.append(indx)

        # RUN THE DELETING PROCESS IN PARALLEL
        # 'max_workers' SET TO MAX CPU CORES
        with concurrent.futures.ThreadPoolExecutor(max_workers=None) as executor:
            futures = [
                executor.submit(self.process, file)
                for file in self.files
            ]

            # PROGRESS BAR CALCULATIONS
            progress = 0
            completed = 0

            # UPDATE THE PROGRESS BAR, UPON EACH FINISHED PROCESS
            for _ in concurrent.futures.as_completed(futures):
                completed += 1
                progress += completed / len(self.files)
                self.progress_signal.emit(progress)

            self.progress_signal.emit(100)
        self.removed_rows_signal.emit(removed_rows)


class RestoreWorker(QThread):

    update_progress_signal = Signal(float)

    def __init__(self, data: dict) -> None:
        super().__init__()

        self.data = data
        self.controller = Controller()

    def run(self):

        completed = 0
        total_data = len(self.data)

        for (_, dest_with_filename) in self.data.items():

            self.controller.restore_removed_content(
                self.controller.TRASH_PATH,
                dest_with_filename
            )

            print(f"restored...{dest_with_filename}")

            # UPDATE PROGRESS BAR
            completed += 1
            progress = completed / total_data
            self.update_progress_signal.emit(progress)
