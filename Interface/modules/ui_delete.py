"""

    PARENT CLASS: Model
        CHILD CLASS: Controller
            CHILD CLASS: Ui

"""

import json
import os
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from ..environment import Constant, Common, Html

from controller import Environment


class Model:
    """
    ### SHARABLE OBJECTS AND METHODS
        ACCESSIBLE BY BOTH CONTROLLER & UI
    """

    def __init__(self) -> None:
        self.html = Html()
        self.constant = Constant()
        self.environment = Environment()
        self.common_functions = Common()

        self.path_input = ""
        self.cache_file = self.environment.CACHE_FILE


class Controller(Model):
    """
    ### UI FUNCTIONALITY
        ACCESSIBLE BY UI ONLY

    """

    def import_cache(
        self,
        lookupType: QComboBox,
        currentPath: QLineEdit,
        lookupFormat: QComboBox,
        lookupInput: QLineEdit,
        isRecursive: QCheckBox,
    ) -> None:
        # CACHE FOUND
        if os.path.exists(self.environment.CACHE_FILE):
            cache: dict = json.load(open(self.cache_file)).get("delete page")

            lookupType.setCurrentText(cache.get("lookupType"))
            lookupFormat.setCurrentText(cache.get("lookupFormat"))
            currentPath.setText(cache.get("currentPath"))
            lookupInput.setText(cache.get("lookupInput"))
            isRecursive.setChecked(cache.get("IsRecursive"))

            self.path_input = cache.get("currentPath")

    def export_cache(
        self,
        lookupType: QComboBox,
        currentPath: QLineEdit,
        lookupFormat: QComboBox,
        lookupInput: QLineEdit,
        isRecursive: QCheckBox,
    ) -> None:
        cache: dict = {}

        # CACHE FOUND
        if os.path.exists(self.cache_file):
            cache: dict = json.load(open(self.cache_file))

        path = currentPath.text()
        search = lookupInput.text()
        lu_type = lookupType.currentText()
        lu_frmt = lookupFormat.currentText()
        recursive = isRecursive.isChecked()

        cache["delete page"] = {
            "lookupType": lu_type,
            "currentPath": path,
            "lookupFormat": lu_frmt,
            "lookupInput": search,
            "IsRecursive": recursive,
        }

        with open(self.cache_file, "w+") as file:
            json.dump(cache, file)

    def set_user_path(self, path: str, widget: QWidget | None = None):
        """
        Update user path input
        """

        # RESET USER PATH
        if not path:
            self.path_input = ""
            return

        self.path_input = path

        if widget:
            widget.setText(path)

    def change_lookup_format(
        self, lookup_type_widget: QWidget, lookup_format_widget: QWidget
    ) -> None:
        """
        Change lookup format options according to the lookup type
        """

        current_type = lookup_type_widget.currentText()
        total_formats = lookup_format_widget.count()

        # ADD THE OPTION 'EXTENSION' IF 'FILES' SELECTED
        if current_type == "FILES":
            if total_formats == 2:
                lookup_format_widget.addItem("EXTENSION")
                return

        if total_formats == 3:
            lookup_format_widget.removeItem(2)

    def get_data(
        self,
        start_widget: QWidget,
        format_input: QWidget,
        lookup_format_widget: QWidget,
        lookup_type_widget: QWidget,
        recursive_widget: QWidget,
    ) -> dict:
        """
        Begin lookup process. Deactivate the btn and reactivate it after
        """

        start_widget.setEnabled(False)

        type: str = lookup_type_widget.currentText()
        format: str = lookup_format_widget.currentText()
        format_input: str = format_input.text()
        is_recursive: bool = recursive_widget.isChecked()

        # UPDATE THE FINDER PARAMETERS
        self.environment.update_param(
            self.path_input,
            is_recursive,
        )

        try:
            # BOTH INPUTS REQUIRED
            if not format_input or not self.path_input:
                print("Empty search input")

            else:
                # SEARCH BY SELECTED FORMAT
                if type == "FILES":
                    match format:
                        case "NAME":
                            return self.environment.get_files_by_name(format_input)

                        case "EXTENSION":
                            return self.environment.get_files_by_extension(format_input)

                        case "PATTERN":
                            return self.environment.get_files_by_pattern(format_input)

                elif type == "FOLDERS":
                    match format:
                        case "NAME":
                            return self.environment.get_folders_by_name(format_input)

                        case "PATTERN":
                            return self.environment.get_folders_by_pattern(format_input)

        except Exception as e:
            print(str(e))
            return {}

        finally:
            start_widget.setEnabled(True)

    def delete_files_clicked(
        self, checkboxes: list[QCheckBox], data: dict[dict]
    ) -> None:
        non_checked = True

        for index, checkbox in enumerate(checkboxes):
            if checkbox.isChecked():
                print(data.get(index + 1))

                # TODO: DELETE FILE INPLEMENTATION HERE

                non_checked = False

        if non_checked:
            print("No item has been selected")


class Ui(Controller):
    def __init__(self) -> None:
        super().__init__()

        self.data = []
        self.checkboxes = []
        self.table_headers = ("FILE | FOLDER", "SOURCE", "SIZE (MB)", "SELECT ALL")

        # SIGNAL TO LIMIT TO ONE CLICK AT A TIME
        self.is_select_all_checkboxes_signal = False

    def start_lookup(self):
        # CACHE INPUTS
        self.export_cache(
            self.LookupType_comboBox,
            self.currentPath_lineEdit,
            self.lookupFormat_comboBox,
            self.lookupInput_lineEdit,
            self.isRecursive_checkBox,
        )

        self.checkboxes.clear()

        # SEARCH PROCESS
        self.data = self.get_data(
            self.startLookup_btn,
            self.lookupInput_lineEdit,
            self.lookupFormat_comboBox,
            self.LookupType_comboBox,
            self.isRecursive_checkBox,
        )

        self.update_table()

    def init_table(self, rows=1, columns=4):
        """
        Render a new table widget with headers
        """

        total_rows = rows
        total_columns = columns

        # CLEAR PREVIOUS ROWS
        self.table_layout.setRowCount(0)

        self.table_layout.setRowCount(total_rows)
        self.table_layout.setColumnCount(total_columns)

        font = QFont()
        font.setBold(True)

        # RENDER TABLE HEADERS
        self.table_layout.setHorizontalHeaderLabels(self.table_headers)

        self.table_layout.horizontalHeader().sectionClicked.connect(
            self.toggle_checkboxes
        )

        self.retranslateTableHeaders()

    def update_table(self) -> None:
        """
        Display new data on the table
        """

        if not self.data:
            print("no data has been found")
            return

        data = self.data.values()

        self.init_table(len(data))

        # Populate the table with new data
        for row_index, row_data in enumerate(data):
            for col_index, (_, value) in enumerate(row_data.items()):
                item = QTableWidgetItem(str(value))
                self.table_layout.setItem(row_index, col_index, item)

                # render check items for each table-row
                if col_index == 2:
                    self.table_layout.setItem(
                        row_index, col_index + 1, QTableWidgetItem()
                    )
                    checkbox = QCheckBox()
                    checkbox.setChecked(True)
                    self.table_layout.setCellWidget(row_index, col_index + 1, checkbox)

                    self.checkboxes.append(checkbox)

        # Resize columns based on their contents
        for col_index in range(self.table_layout.columnCount()):
            self.table_layout.resizeColumnToContents(col_index)

    def toggle_checkboxes(self, header_section: int) -> None:
        """
        ### TOGGLE THE CHECKBOXES FOR EACH TABLE ITEM
            - ISSUE: The function is called twice on one click
            - FIX: The signal is going to be checked twice on every click
                 and changes state to only allow one call to toggle the checkboxes

        """

        if not self.is_select_all_checkboxes_signal:
            if header_section == 3:
                for checkbox in self.checkboxes:
                    checkbox.toggle()

                self.is_select_all_checkboxes_signal = True

        else:
            # TURN THE SIGNAL BACK OFF FOR NEXT CLICK
            self.is_select_all_checkboxes_signal = False

    def retranslateTableHeaders(self):
        for col, txt in enumerate(self.table_headers):
            header_item = QTableWidgetItem(
                QCoreApplication.translate("MainWindow", txt)
            )
            self.table_layout.setHorizontalHeaderItem(col, header_item)

    def retranslateUi(self):
        """
        TRANSLATE UI TEXT
        """

        """
        ////////////////////////////////////////////////
                COMOBOXES ITEMS
        ////////////////////////////////////////////////
        """

        data = {
            self.LookupType_comboBox: ("FILES", "FOLDERS"),
            self.lookupFormat_comboBox: ("NAME", "PATTERN", "EXTENSION"),
        }

        for widget, info in data.items():
            for indx, text in enumerate(info):
                widget.addItem("")
                widget.setItemText(
                    indx, QCoreApplication.translate("MainWindow", text, None)
                )

        """
        ////////////////////////////////////////////////
                SET TEXT / TOOL TIPS
        ////////////////////////////////////////////////
        """

        data = {
            self.delete_btn: ("DELETE", "Delete All Selected Items"),
            self.restore_btn: ("RESTORE", "Restore Last Deleted Process"),
            self.save_btn: ("SAVE", "Store Current Lookup"),
            self.load_btn: ("LOAD", "Load Previous Lookup"),
            self.startLookup_btn: ("START", "Start Lookup Process"),
            self.isRecursive_checkBox: (
                "RECURSIVE",
                "Find Files Recursively Through The Selected Path",
            ),
        }

        for widget, info in data.items():
            widget.setText(QCoreApplication.translate("MainWindow", info[0], None))
            widget.setToolTip(QCoreApplication.translate("MainWindow", info[1], None))

        self.PageTitle_label.setText(
            QCoreApplication.translate("MainWindow", "DELETE", None)
        )

        self.currentPath_lineEdit.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "Enter the path where should the lookup process begin",
                None,
            )
        )
        self.currentPath_lineEdit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Enter the path here", None)
        )
        self.browseCurrentPath_btn.setText(
            QCoreApplication.translate("MainWindow", "OPEN", None)
        )
        self.lookupInput_lineEdit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Enter your input", None)
        )
        self.LookuByTitle_label.setText(
            QCoreApplication.translate("MainWindow", "LOOKUP BY", None)
        )

        """
        ////////////////////////////////////////////////
                TABLE CONTENT
        ////////////////////////////////////////////////
        """
        self.table_layout.setSortingEnabled(True)
        self.retranslateTableHeaders()

        """
        ////////////////////////////////////////////////
                SET CACHED DATA
        ////////////////////////////////////////////////
        """
        self.import_cache(
            self.LookupType_comboBox,
            self.currentPath_lineEdit,
            self.lookupFormat_comboBox,
            self.lookupInput_lineEdit,
            self.isRecursive_checkBox,
        )

    def render_page_icons(self):
        size = 20
        self.common_functions.set_icon(
            self.browseCurrentPath_btn, "folder_outline", (size, size)
        )
        self.common_functions.set_icon(self.startLookup_btn, "start", (size, size))
        self.common_functions.set_icon(self.delete_btn, "delete sign", (size, size))
        self.common_functions.set_icon(self.restore_btn, "restore file", (size, size))
        self.common_functions.set_icon(self.load_btn, "file upload", (size, size))
        self.common_functions.set_icon(self.save_btn, "file download", (size, size))

    def render_page(self):
        self.widgets = QWidget()

        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)

        self.widgets.setObjectName("widgets")
        self.verticalLayout = QVBoxLayout(self.widgets)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame_content_wid_3 = QFrame(self.widgets)
        self.frame_content_wid_3.setObjectName("frame_content_wid_3")
        self.frame_content_wid_3.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_content_wid_3)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.first_layout = QGridLayout()
        self.first_layout.setObjectName("first_layout")
        self.PageTitle_label = QLabel(self.frame_content_wid_3)
        self.PageTitle_label.setObjectName("PageTitle_label")
        self.PageTitle_label.setFont(font)

        self.first_layout.addWidget(self.PageTitle_label, 0, 0, 1, 1)

        self.LookupType_comboBox = QComboBox(self.frame_content_wid_3)
        self.LookupType_comboBox.setObjectName("LookupType_comboBox")
        self.LookupType_comboBox.setFont(font)
        self.LookupType_comboBox.setAutoFillBackground(False)
        self.LookupType_comboBox.setStyleSheet(self.html.get_bg_color("dark blue"))
        self.LookupType_comboBox.setFrame(True)

        self.first_layout.addWidget(self.LookupType_comboBox, 1, 0, 1, 1)
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )
        self.first_layout.addItem(self.horizontalSpacer, 1, 1, 1, 1)
        self.horizontalLayout_11.addLayout(self.first_layout)
        self.verticalLayout.addWidget(self.frame_content_wid_3)

        self.row_1 = QFrame(self.widgets)
        self.row_1.setObjectName("row_1")
        self.row_1.setFrameShape(QFrame.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.row_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.row_1)

        self.frame_content_wid_4 = QFrame(self.widgets)
        self.frame_content_wid_4.setObjectName("frame_content_wid_4")
        self.frame_content_wid_4.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_content_wid_4)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.second_layout = QGridLayout()
        self.second_layout.setObjectName("second_layout")
        self.second_layout.setContentsMargins(-1, -1, -1, 0)
        self.currentPath_lineEdit = QLineEdit(self.frame_content_wid_4)
        self.currentPath_lineEdit.setObjectName("currentPath_lineEdit")
        self.currentPath_lineEdit.setMinimumSize(QSize(0, 30))
        self.currentPath_lineEdit.setStyleSheet(self.html.get_bg_color("dark blue"))

        self.second_layout.addWidget(self.currentPath_lineEdit, 0, 1, 1, 1)

        self.browseCurrentPath_btn = QPushButton(self.frame_content_wid_4)
        self.browseCurrentPath_btn.setObjectName("browseCurrentPath_btn")
        self.browseCurrentPath_btn.setMinimumSize(QSize(150, 30))
        self.browseCurrentPath_btn.setFont(font)
        self.browseCurrentPath_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.browseCurrentPath_btn.setStyleSheet(self.html.get_bg_color("lightblue"))

        self.second_layout.addWidget(self.browseCurrentPath_btn, 0, 2, 1, 1)
        self.horizontalLayout_13.addLayout(self.second_layout)
        self.verticalLayout.addWidget(self.frame_content_wid_4)

        self.frame_content_wid_2 = QFrame(self.widgets)
        self.frame_content_wid_2.setObjectName("frame_content_wid_2")
        self.frame_content_wid_2.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_content_wid_2)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.third_layout = QGridLayout()
        self.third_layout.setObjectName("third_layout")
        self.third_layout.setContentsMargins(-1, -1, -1, 0)
        self.lookupInput_lineEdit = QLineEdit(self.frame_content_wid_2)
        self.lookupInput_lineEdit.setObjectName("currentLookupInput_lineEdit")
        self.lookupInput_lineEdit.setMinimumSize(QSize(0, 30))
        self.lookupInput_lineEdit.setStyleSheet(self.html.get_bg_color("dark blue"))

        self.third_layout.addWidget(self.lookupInput_lineEdit, 1, 1, 1, 1)

        self.startLookup_btn = QPushButton(self.frame_content_wid_2)
        self.startLookup_btn.setObjectName("startLookup_btn")
        self.startLookup_btn.setMinimumSize(QSize(150, 30))
        self.startLookup_btn.setFont(font)
        self.startLookup_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.startLookup_btn.setStyleSheet(self.html.get_bg_color("lightblue"))

        self.third_layout.addWidget(self.startLookup_btn, 1, 2, 1, 1)

        self.lookupFormat_comboBox = QComboBox(self.frame_content_wid_2)
        self.lookupFormat_comboBox.setObjectName("currentLookupBy_comboBox")
        self.lookupFormat_comboBox.setFont(font)
        self.lookupFormat_comboBox.setAutoFillBackground(False)
        self.lookupFormat_comboBox.setStyleSheet(self.html.get_bg_color("dark blue"))
        self.lookupFormat_comboBox.setFrame(True)

        self.third_layout.addWidget(self.lookupFormat_comboBox, 1, 0, 1, 1)

        self.isRecursive_checkBox = QCheckBox(self.frame_content_wid_2)
        self.isRecursive_checkBox.setObjectName("isRecursive_checkBox")
        self.isRecursive_checkBox.setAutoFillBackground(False)
        self.isRecursive_checkBox.setChecked(True)

        self.third_layout.addWidget(self.isRecursive_checkBox, 2, 0, 1, 1)

        self.LookuByTitle_label = QLabel(self.frame_content_wid_2)
        self.LookuByTitle_label.setObjectName("LookuByTitle_label")
        self.LookuByTitle_label.setStyleSheet("color: rgb(113, 126, 149)")
        self.LookuByTitle_label.setLineWidth(1)
        self.LookuByTitle_label.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter
        )

        self.third_layout.addWidget(self.LookuByTitle_label, 0, 0, 1, 1)
        self.horizontalLayout_10.addLayout(self.third_layout)
        self.verticalLayout.addWidget(self.frame_content_wid_2)

        self.row_3 = QFrame(self.widgets)
        self.row_3.setObjectName("row_3")
        self.row_3.setMinimumSize(QSize(0, 150))
        self.row_3.setFrameShape(QFrame.StyledPanel)
        self.row_3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_12 = QHBoxLayout(self.row_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)

        """
            ////////////////////////////////////////////////
                    TABLE CONTENT
            ////////////////////////////////////////////////
        """
        self.table_layout = QTableWidget(self.row_3)

        self.table_layout.setObjectName("table_layout")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            self.table_layout.sizePolicy().hasHeightForWidth()
        )
        self.table_layout.setSizePolicy(sizePolicy3)

        self.init_table()

        """
            ////////////////////////////////////////////////
                    PALLETE AND BRUSHES
            ////////////////////////////////////////////////
        """
        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)

        self.table_layout.setFrameShape(QFrame.NoFrame)
        self.table_layout.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.table_layout.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.table_layout.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_layout.setSelectionMode(QAbstractItemView.NoSelection)
        self.table_layout.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_layout.setShowGrid(True)
        self.table_layout.setGridStyle(Qt.SolidLine)
        self.table_layout.setSortingEnabled(True)
        self.table_layout.horizontalHeader().setVisible(True)
        self.table_layout.horizontalHeader().setCascadingSectionResizes(True)
        self.table_layout.horizontalHeader().setDefaultSectionSize(200)
        self.table_layout.horizontalHeader().setStretchLastSection(True)
        self.table_layout.verticalHeader().setVisible(False)
        self.table_layout.verticalHeader().setCascadingSectionResizes(True)
        self.table_layout.verticalHeader().setHighlightSections(False)
        self.table_layout.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_12.addWidget(self.table_layout)

        self.optionBtns_layout = QVBoxLayout()
        self.optionBtns_layout.setObjectName("optionBtns_layout")

        self.delete_btn = QPushButton(self.row_3)
        self.restore_btn = QPushButton(self.row_3)
        self.save_btn = QPushButton(self.row_3)
        self.load_btn = QPushButton(self.row_3)

        self.delete_btn.setObjectName("delete_btn")
        self.restore_btn.setObjectName("restore_btn")
        self.save_btn.setObjectName("save_btn")
        self.load_btn.setObjectName("load_btn")

        btns = (self.delete_btn, self.restore_btn, self.save_btn, self.load_btn)

        for btn in btns:
            btn.setMinimumSize(QSize(150, 30))
            btn.setStyleSheet(self.html.get_bg_color("lightblue"))
            btn.setCursor(QCursor(Qt.PointingHandCursor))
            btn.setFont(font)

            self.optionBtns_layout.addWidget(btn)

        self.horizontalLayout_12.addLayout(self.optionBtns_layout)
        self.verticalLayout.addWidget(self.row_3)

        self.retranslateUi()
        self.render_page_icons()

        """
        ////////////////////////////////////////////////
                BUTTONS  EVENTS/SIGNAL
        ////////////////////////////////////////////////
        """

        self.browseCurrentPath_btn.clicked.connect(
            lambda: self.set_user_path(
                self.common_functions.get_user_path(), self.currentPath_lineEdit
            )
        )

        self.currentPath_lineEdit.textChanged.connect(
            lambda: self.set_user_path(self.currentPath_lineEdit.text())
        )

        self.startLookup_btn.clicked.connect(lambda: self.start_lookup())

        self.isRecursive_checkBox.isChecked()

        self.LookupType_comboBox.currentTextChanged.connect(
            lambda: self.change_lookup_format(
                self.LookupType_comboBox, self.lookupFormat_comboBox
            )
        )

        self.delete_btn.clicked.connect(
            lambda: self.delete_files_clicked(self.checkboxes, self.data)
        )

        return self.widgets
