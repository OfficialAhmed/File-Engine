"""
====================================================================================================
    MAIN UI CREATED BY   : WANDERSON M.PIMENTA  (https://github.com/Wanderson-Magalhaes)
    EDITED/ENHANCED BY   : OFFICIALAHMED        (https://github.com/OfficialAhmed)
====================================================================================================
"""

# BUILT-INS
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

        # APP NAME
        title = "File Engine"
        description = "File management & automation tool"

        # APPLY TEXTS
        self.setWindowTitle(title)
        self.widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        self.widgets.toggleButton.clicked.connect(
            lambda: UiSettings.toggleMenu(self, True)
        )

        # SET UI DEFINITIONS
        UiSettings.uiDefinitions(self)

        # BUTTONS CLICK

        # LEFT MENUS
        self.widgets.home_page.clicked.connect(self.buttonClick)
        self.widgets.delete_page.clicked.connect(self.buttonClick)
        self.widgets.move_page.clicked.connect(self.buttonClick)
        self.widgets.rename_page.clicked.connect(self.buttonClick)
        self.widgets.lookup_page.clicked.connect(self.buttonClick)

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

        # SHOW APP
        self.show()

        # DEFAULT THEME = DARK
        # SET LIGHT THEME IF SETTING CHANGED
        is_light_theme = False
        light_theme = "Interface\\themes\\py_dracula_light.qss"

        # SET THEME
        if is_light_theme:
            # LOAD AND APPLY STYLE
            UiSettings.theme(self, light_theme, True)

        # SET HOME PAGE AND SELECT MENU
        self.widgets.stackedWidget.setCurrentWidget(
            self.widgets.home_widgets
        )
        self.widgets.home_page.setStyleSheet(
            UiSettings.selectMenu(
                self.widgets.home_page.styleSheet()
            )
        )

    def buttonClick(self):
        """
            BUTTONS CLICK
        """

        # GET BUTTON CLICKED
        btn = self.sender()
        btn_name = btn.objectName()

        match btn_name:

            # SHOW HOME PAGE
            case "home_page":
                self.widgets.stackedWidget.setCurrentWidget(
                    self.widgets.home_widgets
                )
                UiSettings.resetStyle(self, btn_name)
                btn.setStyleSheet(UiSettings.selectMenu(btn.styleSheet()))

            # SHOW DELETE PAGE
            case "delete_page":
                self.widgets.stackedWidget.setCurrentWidget(
                    self.widgets.delete_widgets
                )
                UiSettings.resetStyle(self, btn_name)
                btn.setStyleSheet(UiSettings.selectMenu(btn.styleSheet()))

            # SHOW NEW PAGE
            case "move_page":
                self.widgets.stackedWidget.setCurrentWidget(
                    self.widgets.new_page
                )

                UiSettings.resetStyle(self, btn_name)
                btn.setStyleSheet(
                    UiSettings.selectMenu(
                        btn.styleSheet()
                    )
                )

            case "rename_page":
                self.widgets.stackedWidget.setCurrentWidget(
                    self.widgets.new_page
                )
                UiSettings.resetStyle(self, btn_name)
                btn.setStyleSheet(UiSettings.selectMenu(btn.styleSheet()))

            case "lookup_page":
                self.widgets.stackedWidget.setCurrentWidget(
                    self.widgets.new_page
                )
                UiSettings.resetStyle(self, btn_name)
                btn.setStyleSheet(UiSettings.selectMenu(btn.styleSheet()))

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

        # SET DRAG POS WINDOW

        # GET CURRENT POSITION AS QPointF
        qpointf = event.globalPosition()

        # CONVERT QPointF TO QPoint
        self.dragPos = QPoint(
            int(qpointf.x()),
            int(qpointf.y())
        )


if __name__ == "__main__":

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())
