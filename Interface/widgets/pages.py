
from PySide6.QtWidgets import (
    QLabel, QComboBox, QTableWidget
)

from json import load as jsonLoad
from Interface.modules.ui_settings import UiSettings
from Interface.environment import tables
from Interface.constants import Path


class Page:
    """
        ## SHARED PAGE WIDGETS 
            ACCESSIBLE TO ALL CHILDREN USE THE SHARED VAR `SharedPages`
    """

    ui = None
    widgets = None

    def __init__(self) -> None:
        self.paths = Path()

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

        data = jsonLoad(open(self.paths.PROCESS_FILE))
        label.setText(str(len(data)))
        tables["DELETE"].set_data(data)
        print(data)
        
        # table.render(table)
        # table.fill()
        # fmt: on


# ONE OBJECT SHARED - TO EXCHANGE SAME OBJECT/WIDGETS ACCROSS MULTI SCREENS
SharedPages = Page()
