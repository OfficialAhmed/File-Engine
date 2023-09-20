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



class Constant:

    _RESOURCES_PATH = ":/images/images/"


    @classmethod
    def get_resources_path(self):
        return self._RESOURCES_PATH
    
