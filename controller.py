"""

    CONTROLLER CACHE:
        CONNECTS THE BACK-END (lib) WITH THE FRONT-END (Interface)

    CALLABLE METHODS BY THE UI

"""

from PySide6.QtWidgets import QDialog, QLabel, QVBoxLayout, QDialogButtonBox, QMessageBox

import os
import lib.move as Move
import lib.find as Finder
import lib.delete as Delete


class Controller:
    """
        ### UI Common methods and static variables
        Called by the `ui_delete`
            * static vars called by self in the init, else use getters
    """

    ROOT_PATH:  str = os.getcwd() + "\\"
    DATA_PATH:  str = ROOT_PATH + "data\\"

    TRASH_PATH: str = DATA_PATH + "trash\\"
    CACHE_FILE: str = DATA_PATH + "Cache.json"
    TRASH_CONTENT_FILE = f"{TRASH_PATH}content.json"

    FILE_FINDER = Finder.File()
    FOLDER_FINDER = Finder.Folder()

    FILE_REMOVER = Delete.File()
    FOLDER_REMOVER = Delete.Folder()

    def show_dialog(self, msg: str,  mode: str = "I", is_dialog: bool = True):
        """
        #### RENDER A WINDOW FOR INFO/PERMISSION
            PARAMS:
            * `msg`        : MESSAGE TO DISPLAY
            * `mode`       : ONE CHAR TO DISPLAY THE CORRECT ICON & FOR WINDOW TITLE
                - `I`nformation 
                - `W`arning
                - `C`ritical 
                - `Q`uestion
            * `is_dialog`  : TYPE OF THE DIALOG
                - `FALSE`  : OK        DIALOG
                - `TRUE`   : OK/CANCEL DIALOG
            RETURNS BOOL 
        """

        return DialogWindow().get_response(
            msg, mode, is_dialog
        )

    """
    /////////////////////////////////////////////////
                    FINDER METHODS
    //////////////////////////////////////////////////////
    """

    def update_finder_param(self, path: str, is_recursive: bool) -> None:
        """
            Variables set from UI after rendering
        """

        self.FILE_FINDER.set_path(path)
        self.FILE_FINDER.set_recursive(is_recursive)

        self.FOLDER_FINDER.set_path(path)
        self.FOLDER_FINDER.set_recursive(is_recursive)

    def get_files_by_name(self, name: str) -> dict:
        return self.FILE_FINDER.find("NAME", name)

    def get_folders_by_name(self, name: str) -> dict:
        return self.FOLDER_FINDER.find("NAME", name)

    def get_files_by_pattern(self, pattern: str) -> dict:
        return self.FILE_FINDER.find("PATTERN", pattern)

    def get_folders_by_pattern(self, pattern: str) -> dict:
        return self.FOLDER_FINDER.find("PATTERN", pattern)

    def get_files_by_extension(self, extension: str) -> dict:
        return self.FILE_FINDER.find("EXTENSION", extension)

    """
    /////////////////////////////////////////////////////
                    REMOVER METHODS
    ///////////////////////////////////////////
    """

    def update_remover_param(self) -> None:
        """
            Set when remover object init
        """

        self.FILE_REMOVER.set_remover_param(
            self.TRASH_CONTENT_FILE,
            self.TRASH_PATH
        )
        self.FOLDER_REMOVER.set_remover_param(
            self.TRASH_CONTENT_FILE,
            self.TRASH_PATH
        )

    def empty_trash(self) -> None:
        self.FILE_REMOVER.empty_trash()
        
    def remove_file(self, file_path: str) -> None:
        self.FILE_REMOVER.remove(file_path)

    def remove_folder(self, folder_path: str, folder_name: str) -> None:
        self.FOLDER_REMOVER.remove(folder_path, folder_name)

    def restore_removed_content(self, destination: str) -> int:
        return self.FILE_REMOVER.restore(destination)

    def total_content_removed(self) -> int:
        """
            Get total num files/folders removed and reset it to `0`
            for the next iteration
        """

        total = self.FILE_REMOVER.get_removed_content_count() + \
            self.FOLDER_REMOVER.get_removed_content_count()

        self.FILE_REMOVER.reset_removed_content_count()
        self.FOLDER_REMOVER.reset_removed_content_count()

        return total


class DialogWindow(QDialog):

    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.label = QLabel()

    def get_response(self, msg: str,  mode: str = "I", is_dialog: bool = True) -> bool:

        self.setLayout(self.layout)

        match mode.upper():
            case "I":
                title = "INFORMATION"
                icon = QMessageBox.Information

            case "W":
                title = "WARNING"
                icon = QMessageBox.Warning

            case "C":
                title = "CRITICAL"
                icon = QMessageBox.Critical

            case "Q":
                title = "QUESTION"
                icon = QMessageBox.Question

            case _:
                icon = QMessageBox.Information
                title = mode.upper()

        if is_dialog:

            # RENDER A DIALOG WINDOW WITH OK|CANCEL OPTIONS
            self.options = QDialogButtonBox(
                QDialogButtonBox.Ok | QDialogButtonBox.Cancel
            )

            self.options.rejected.connect(self.reject)
            self.options.accepted.connect(self.accept)
            self.layout.addWidget(self.label)
            self.layout.addWidget(self.options)
            self.label.setText(msg.upper())
            self.setWindowTitle(title)

            # RETURN USER PERMISSION
            return True if self.exec() else False

        # INFORMATIONAL BASED DIALOG. NO OPTIONS OTHER THAN ACCEPT
        msg_box = QMessageBox()
        msg_box.setIcon(icon)
        msg_box.setWindowTitle(title)
        msg_box.setText(msg.upper())

        return True if msg_box.exec() else False
