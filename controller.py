"""

    CONTROLLER CACHE:
        CONNECTS THE BACK-END (lib) WITH THE FRONT-END (Interface)

    CALLABLE METHODS BY THE UI

"""

from PySide6.QtWidgets import (
    QDialog, QLabel, QVBoxLayout, QDialogButtonBox, QMessageBox,
    QComboBox, QTableWidget
)

import os
from json import load as jsonLoad
import lib.move as Move
import lib.delete as Delete
from Interface.modules.ui_settings import UiSettings
# from Interface.environment import Table


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
    PROCESS_FILE: str = DATA_PATH + "Process.json"
    TRASH_CONTENT_FILE = f"{TRASH_PATH}content.json"

    FILE_REMOVER = Delete.File()
    FOLDER_REMOVER = Delete.Folder()

    def show_dialog(self, msg: str,  mode: str = "I", is_dialog: bool = True) -> bool:
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

    def remove_file(self, file_path: str) -> None | str:
        self.FILE_REMOVER.remove(file_path)

    def remove_folder(self, folder_path: str, folder_name: str) -> None | str:
        self.FOLDER_REMOVER.remove(folder_path, folder_name)

    def restore_removed_content(self, destination: str) -> None:
        return self.FILE_REMOVER.restore(destination)

class Page:
    """
        ## SHARED PAGE WIDGETS 
            ACCESSIBLE TO ALL CHILDREN USE THE SHARED VAR `SharedPages`
    """

    ui = None
    widgets = None

    def __init__(self) -> None:
        pass

    def set_widgets(self, widgets, ui) -> None:
        self.widgets = widgets
        self.ui = ui

    def change(self, btn, btn_name, page_widgets):
        """
            DIRECTLY CHANGE THE CURRENT PAGE FROM THE MAIN MENU UI
        """

        UiSettings.resetStyle(self, btn_name)
        btn.setStyleSheet(UiSettings.selectMenu(btn.styleSheet()))
        self.widgets.stackedWidget.setCurrentWidget(page_widgets)

    def change_indirect(self, page):
        """
            * CHANGE THE CURRENT PAGE FROM THE SEARCH PAGE 
            * FILL THE TABLE DATA BASED ON THE SEARCH PROCESS FOUND DATA
        """

        # fmt: off
        search_type = self.widgets.search_widgets.findChild(QComboBox, "searchTypeComboBox").currentText()

        match page:
            case "delete_page":
                self.widgets.delete_page_btn.click()
                label:  QLabel = self.widgets.delete_widgets.findChild(QLabel, "totalRecordsLabel")
                table:  QTableWidget = self.widgets.delete_widgets.findChild(QTableWidget, "tableWidget")

                # STORE SEARCH TYPE IN THE HIDDEN LABEL FOR DELETING METHOD 
                self.widgets.delete_widgets.findChild(QLabel, "searchTypeHiddenLabel").setText(search_type)

        data = jsonLoad(open(Controller.PROCESS_FILE))
        label.setText(str(len(data)))
        self.widgets.delete_widgets.table.set_data(data)
        table.set_data(data)
        # table.render(table)
        # table.fill()
        # fmt: on

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


# ONE OBJECT SHARED - TO EXCHANGE SAME OBJECT/WIDGETS ACCROSS MULTI SCREENS
SharedPages = Page()
