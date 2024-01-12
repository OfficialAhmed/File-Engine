
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

        selected_data = {index: tables["SEARCH"].data.get(index) for index, cb in enumerate(tables["SEARCH"].checkboxes) if cb.isChecked()}
            
        match page:
            case "delete_page":
                table = tables["DELETE"]
                
                self.widgets.delete_page_btn.click()
                label:  QLabel = self.widgets.delete_widgets.findChild(QLabel, "totalRecordsLabel")
                
                # STORE SEARCH TYPE IN THE HIDDEN LABEL FOR DELETING METHOD 
                self.widgets.delete_widgets.findChild(QLabel, "searchTypeHiddenLabel").setText(search_type)

        table.fill(selected_data)
        label.setText(str(len(selected_data)))
        
        # fmt: on


# ONE OBJECT SHARED - TO EXCHANGE SAME OBJECT/WIDGETS ACCROSS MULTI SCREENS
SharedPages = Page()
