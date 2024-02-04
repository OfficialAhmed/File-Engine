"""
    
    # READ-ONLY LIBRARY
    
        - NO CUSTOM LIBRARIES IMPORTED HERE TO AVOID CONFLICTS AND RECIRCLE IMPORTING ISSUES
    
"""

import os
from PySide6.QtWidgets import (
    QDialog, QLabel, QVBoxLayout, QDialogButtonBox, QMessageBox
)

APP_VER = "1.3.0"

class Path:

    def __init__(self) -> None:
        self.RESOURCES_PATH = "frontend/"
        self.ROOT_PATH:  str = os.getcwd() + "\\"
        self.DATA_PATH:  str = self.ROOT_PATH + "data\\"
        self.TRASH_PATH: str = self.DATA_PATH + "trash\\"
        self.CACHE_FILE: str = self.DATA_PATH + "Cache.json"
        self.TRASH_CONTENT_FILE = f"{self.TRASH_PATH}content.json"


class Dialog:

    def __init__(self):
        self.widget = None

    def __get_response(self, msg: str,  mode: str = "I", is_dialog: bool = True) -> bool:
        
        # A FIX: CANNOT USE QDIALOG BEFORE INIT THE QAPPLICATION
        if not self.widget:
            self.widget = QDialog()     # CREATE OBJECT ONCE
        
        layout = QVBoxLayout()
        self.widget.setLayout(layout)
        self.label = QLabel()

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

            self.options.rejected.connect(self.widget.reject)
            self.options.accepted.connect(self.widget.accept)
            layout.addWidget(self.label)
            layout.addWidget(self.options)
            self.label.setText(msg.upper())
            self.widget.setWindowTitle(title)

            # RETURN USER PERMISSION
            return True if self.widget.exec() else False

        # INFORMATIONAL BASED DIALOG. NO OPTIONS OTHER THAN ACCEPT
        msg_box = QMessageBox()
        msg_box.setIcon(icon)
        msg_box.setWindowTitle(title)
        msg_box.setText(msg.upper())

        return True if msg_box.exec() else False

    def show(self, msg: str,  mode: str = "I", is_dialog: bool = True) -> bool:
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

        return self.__get_response(
            msg, mode, is_dialog
        )
