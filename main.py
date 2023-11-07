"""
====================================================================================================
    MAIN UI CREATED BY   : WANDERSON M.PIMENTA  (https://github.com/Wanderson-Magalhaes)
    EDITED/ENHANCED BY   : OFFICIALAHMED        (https://github.com/OfficialAhmed)
====================================================================================================
"""

# BUILT-INS
import json
import os
import sys
import platform

# QT / PYSIDE FRAMEWORK
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

# CUSTOME WIDGETS STYLING
from Interface.modules.ui_main import *
from Interface.modules.ui_settings import *


# FIX Problem for High DPI and Scale above 100%
os.environ["QT_FONT_DPI"] = "96"


class MainWindow(QMainWindow):

    widgets = None

    def __init__(self):
        QMainWindow.__init__(self)


        # SET AS GLOBAL WIDGETS
        self.ui = Ui()
        self.ui.setupUi(self)
        # global widgets
        self.widgets = self.ui

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        self.ui.EENABLE_CUSTOM_TITLE_BAR = True if platform.system() == "Windows" else False
        

        self.setWindowTitle(
            "File Engine"
        )

        self.widgets.titleRightInfo.setText(
            "File Management & Automation Tool"
        )

        # SET UI DEFINITIONS
        UiSettings.uiDefinitions(self)

        # LEFT MENUS
        self.widgets.home_page.clicked.connect(self.change_page)
        self.widgets.delete_page.clicked.connect(self.change_page)
        self.widgets.move_page.clicked.connect(self.change_page)
        self.widgets.rename_page.clicked.connect(self.change_page)
        self.widgets.lookup_page.clicked.connect(self.change_page)

        # TOGGLE MENU
        self.widgets.toggleButton.clicked.connect(
            lambda: UiSettings.toggleMenu(self, True)
        )

        # EXTRA LEFT MENU
        self.widgets.toggleLeftBox.clicked.connect(
            lambda: UiSettings.toggleLeftBox(self, True)
        )

        self.widgets.extraCloseColumnBtn.clicked.connect(
            lambda: UiSettings.toggleLeftBox(self, True)
        )

        # EXTRA RIGHT MENU
        self.widgets.moreBtn.clicked.connect(
            lambda: UiSettings.toggleRightBox(self, True)
        )

        self.show()

        default_settings = self.get_settings()
        
        # APPLY THEME - DARK IS THE DEFAULT
        if default_settings.get("is_light_theme"):
            UiSettings.theme(self, True)

        # SET HOME PAGE AND SELECT MENU
        self.widgets.stackedWidget.setCurrentWidget(
            self.widgets.home_widgets
        )
        self.widgets.home_page.setStyleSheet(
            UiSettings.selectMenu(
                self.widgets.home_page.styleSheet()
            )
        )

    def change_page(self):
        """
            BUTTONS CLICK
        """

        btn = self.sender()
        btn_name = btn.objectName()

        UiSettings.resetStyle(self, btn_name)
        btn.setStyleSheet(UiSettings.selectMenu(btn.styleSheet()))

        match btn_name:
            case "home_page":      page = self.widgets.home_widgets
            case "delete_page":    page = self.widgets.delete_widgets
            case "move_page":      page = self.widgets.new_page
            case "rename_page":    page = self.widgets.new_page
            case "lookup_page":    page = self.widgets.new_page

        self.widgets.stackedWidget.setCurrentWidget(page)

    def resizeEvent(self, event):
        """
            RESIZE EVENTS
        """

        # Update Size Grips
        UiSettings.resize_grips(self)

    def mousePressEvent(self, event):
        """
            MOUSE CLICK EVENTS
        """

        # GET CURRENT POSITION AS QPointF
        qpointf = event.globalPosition()

        # CONVERT QPointF TO QPoint
        self.dragPos = QPoint(
            int(qpointf.x()),
            int(qpointf.y())
        )

    def get_settings(self) -> dict:

        path = "data/settings/"
        file = "default.json"

        if not os.path.exists(path):
            os.makedirs(path)

        # MAKE SURE FILE EXISTS BEFORE MOVING ON
        if os.path.exists(path + file):
            return json.load(open(path + file))

        # DEFAULT SETTINGS ON CREATE
        data = {
            "is_light_theme": False,
        }

        json.dump(data, open(path + file, "w+"))

        return data


if __name__ == "__main__":

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())
