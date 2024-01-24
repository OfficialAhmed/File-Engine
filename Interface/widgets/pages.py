
from PySide6.QtWidgets import QLabel, QComboBox

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
                table = tables["DELETE"]

                self.widgets.delete_page_btn.click()
                label:  QLabel = self.widgets.delete_widgets.findChild(QLabel, "totalRecordsLabel")

                # STORE SEARCH TYPE IN THE HIDDEN LABEL FOR DELETING METHOD 
                self.widgets.delete_widgets.findChild(QLabel, "searchTypeHiddenLabel").setText(search_type)
            
            case "rename_page":
                table = tables["RENAME"]
                self.widgets.rename_page_btn.click()

                label:  QLabel = self.widgets.rename_widgets.findChild(QLabel, "totalRecordsLabel")
                self.widgets.delete_widgets.findChild(QLabel, "searchTypeHiddenLabel").setText(search_type)

        # TAKE OUT THE CHECKED ITEMS TO THE SELECTED TABLE
        selected_data = {}
        searched = tables["SEARCH"]

        for row in range(searched.table.rowCount()):
            if searched.table.cellWidget(row, 3).isChecked():
                file_name = searched.table.item(row, 0).text()
                selected_data[file_name] = searched.data.get(file_name)

        table.fill(selected_data)
        label.setText(str(len(selected_data)))
        # fmt: on


# ONE OBJECT SHARED - TO EXCHANGE SAME OBJECT/WIDGETS ACROSS MULTI PAGES
shared_pages = Page()
