"""
    ### HANDLES THE LEFT SIDEBAR OF THE MAIN WINDOW (PAGES)
        USED BY MAIN.PY TO RECIEVE ONCLICK-CHANGE AT ANY TIME
"""

import pathlib
from PySide6.QtWidgets import QLabel, QWidget

from frontend.modules.settings import UiSettings
from environment import tables
from constants import Path


class View:
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

        match page:

            case "delete_page":
                table = tables["DELETE"]

                self.widgets.delete_page_btn.click()
                widget:  QWidget = self.widgets.delete_widgets

            case "rename_page":
                table = tables["RENAME"]

                self.widgets.rename_page_btn.click()
                widget:  QWidget = self.widgets.rename_widgets

            case "move_page":
                table = tables["MOVE"]

                self.widgets.move_page_btn.click()
                widget:  QWidget = self.widgets.move_widgets

            case _:
                print("change indirect - unhandled page clicked!")
                return

        # TAKE OUT THE CHECKED ITEMS TO THE SELECTED TABLE
        selected_data = {}
        searched = tables["SEARCH"]

        for row in range(searched.table.rowCount()):
            if searched.table.cellWidget(row, 3).isChecked():
                file_name = searched.table.item(row, 0).text()
                file_root = searched.table.item(row, 1).text()
                key = pathlib.Path(f"{file_root}//{file_name}")
                selected_data[key] = searched.data.get(key)

        table.fill(selected_data)

        # SET TOTAL RECORDS
        widget.findChild(QLabel, "totalRecordsLabel").setText(str(len(selected_data)))

        # fmt: on


# ONE OBJECT SHARED - TO EXCHANGE SAME OBJECT/WIDGETS ACROSS MULTI PAGES
shared_views = View()
