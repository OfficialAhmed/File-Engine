"""
    Parent class holds constant values 
    for the interface
"""

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Common:

    def __init__(self) -> None:
        self.constant = Constant()

    
    def set_icon(self, widget:QWidget, name:str, size=(18, 18)) -> str:

        widget.setIcon(
            QIcon(f"{self.constant.get_resources_path()}icons/{name}.svg") 
        )

        widget.setIconSize(QSize(*size))


    def get_user_path(self) -> str | None:
        """
        Render a window to select the path
        """
        options = QFileDialog.Options()
        # options |= QFileDialog.DontUseSheet
        dialog = QFileDialog()
        dialog.setOptions(options)
        # dialog.setDirectory()

        path = QFileDialog.getExistingDirectory(
            None,
            "PICK A FOLDER TO CONTINUE",
            "", # PATH ON WINDOW RENDER
            options=options,
        )

        # return the directory path, otherwise return None
        return path if path else None



class Constant:

    _RESOURCES_PATH = ":/images/images/"


    @classmethod
    def get_resources_path(self):
        return self._RESOURCES_PATH
    

class Html:

    COLOR:dict = {
        "dark blue": "33, 37, 43",
        "light blue": "52, 59, 72",
    }


    def __init__(self) -> None:
        
        self.color = self.COLOR


    def get_bg_color(self, name:str) -> str:
        return f"background-color: rgb({self.color.get(name)})"
