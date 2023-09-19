# UI Created BY: WANDERSON M.PIMENTA

import sys
import os
import platform

# IMPORT / GUI AND MODULES AND WIDGETS
from Interface.modules import *
from Interface.widgets import *


os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
widgets = None

class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        Settings.ENABLE_CUSTOM_TITLE_BAR = True if platform.system() == "Windows" else False

        # APP NAME
        title = "File Engine"
        description = "File management & automation tool"

        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        widgets.toggleButton.clicked.connect(
            lambda: UIFunctions.toggleMenu(self, True)
        )

        # SET UI DEFINITIONS
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # widgets.stackedWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK

        # LEFT MENUS
        widgets.home_page.clicked.connect(self.buttonClick)
        widgets.delete_page.clicked.connect(self.buttonClick)
        widgets.move_page.clicked.connect(self.buttonClick)
        widgets.rename_page.clicked.connect(self.buttonClick)
        widgets.lookup_page.clicked.connect(self.buttonClick)

        # EXTRA LEFT MENU
        widgets.toggleLeftBox.clicked.connect(
            lambda: UIFunctions.toggleLeftBox(self, True)
        )
        widgets.extraCloseColumnBtn.clicked.connect(
            lambda: UIFunctions.toggleLeftBox(self, True)
        )

        # EXTRA RIGHT MENU
        widgets.moreBtn.clicked.connect(
            lambda: UIFunctions.toggleRightBox(self, True)
        )

        # SHOW APP
        self.show()

        # SET CUSTOM THEME
        useCustomTheme = False
        themeFile = "themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.home_page.setStyleSheet(UIFunctions.selectMenu(widgets.home_page.styleSheet()))


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
                widgets.stackedWidget.setCurrentWidget(widgets.home)
                UIFunctions.resetStyle(self, btn_name)
                btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

            # SHOW DELETE PAGE
            case "delete_page":
                widgets.stackedWidget.setCurrentWidget(widgets.widgets)
                UIFunctions.resetStyle(self, btn_name)
                btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

            # SHOW NEW PAGE
            case "move_page":
                widgets.stackedWidget.setCurrentWidget(widgets.new_page) # SET PAGE
                UIFunctions.resetStyle(self, btn_name) # RESET ANOTHERS BUTTONS SELECTED
                btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

            case "rename_page":
                widgets.stackedWidget.setCurrentWidget(widgets.new_page) # SET PAGE
                UIFunctions.resetStyle(self, btn_name) 
                btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

            case "lookup_page":
                widgets.stackedWidget.setCurrentWidget(widgets.new_page) 
                UIFunctions.resetStyle(self, btn_name) 
                btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # PRINT BTN NAME
        print(f'Button "{btn_name}" pressed!')


    def resizeEvent(self, event):
        """
            RESIZE EVENTS
        """

        # Update Size Grips
        UIFunctions.resize_grips(self)


    def mousePressEvent(self, event):
        """
            MOUSE CLICK EVENTS
        """

        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        match event.buttons():

            case Qt.LeftButton:
                print('Mouse click: LEFT CLICK')

            case Qt.RightButton:
                print('Mouse click: RIGHT CLICK')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())
