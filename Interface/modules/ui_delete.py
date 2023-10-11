"""

    Delete page UI / logic

    PARENT CLASS: Model
        CHILD CLASS: Controller
            CHILD CLASS: Ui

"""

import json
import os
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from Interface.environment import *
from controller import Controller


class Model:
    """
    ### SHARABLE OBJECTS AND METHODS
        ACCESSIBLE BY BOTH CONTROLLER & UI
    """

    def __init__(self) -> None:

        self.html = Html()
        self.constant = Constant()
        self.controller = Controller()
        self.controller.update_remover_param()

        self.common_functions = Common()
        self.progressBar = ProgressBar()

        self.path_input = ""
        self.cache_file = self.controller.CACHE_FILE


class Mediator(Model):
    """
    ### MAINLY UI FUNCTIONALITY/INTERACTIONS
        ACCESSIBLE BY UI ONLY
    """

    def __init__(self) -> None:
        super().__init__()

        # CREATE DATA FOLDER IF NOT FOUND
        if not os.path.exists("data"):
            os.mkdir(self.controller.DATA_PATH)

    def set_controller_widgets(
        self,
        lookupType:   QPushButton,
        currentPath:  QComboBox,
        lookupFormat: QLineEdit,
        lookupInput:  QCheckBox,
        isRecursive:  QLineEdit,
        startBtn:     QComboBox,
        tableLayout:  QTableWidget
    ):
        """
        Set current window widgets from 'UI' class
        """
        self.startBtn:     QPushButton = startBtn
        self.lookupType:   QComboBox = lookupType
        self.lookupInput:  QLineEdit = lookupInput
        self.isRecursive:  QCheckBox = isRecursive
        self.lookupFormat: QComboBox = lookupFormat
        self.tableLayout:  QTableWidget = tableLayout
        self.currentPathInput: QLineEdit = currentPath

    def import_cache(self) -> None:

        # IF CACHE FOUND
        if os.path.exists(self.controller.CACHE_FILE):
            cache: dict = json.load(open(self.cache_file)).get("delete page")

            self.lookupInput.setText(cache.get("lookupInput"))
            self.isRecursive.setChecked(cache.get("IsRecursive"))
            self.currentPathInput.setText(cache.get("currentPath"))
            self.lookupType.setCurrentText(cache.get("lookupType"))

            self.path_input = cache.get("currentPath")

            # UPDATE LOOKUP FORMAT ACCORDING TO THE CACHED LOOKUP TYPE
            self.change_lookup_format()

            self.lookupFormat.setCurrentText(cache.get("lookupFormat"))

    def export_cache(self) -> None:

        # TODO: CHECK IF BOTH CACHES ARE THE SAME, SKIP EXPORTING - NO NEED TO WASTE TIME IN WRITING
        cache = {}

        # IF CACHE FOUND
        if os.path.exists(self.cache_file):
            cache: dict = json.load(open(self.cache_file))

        search = self.lookupInput.text()
        path = self.currentPathInput.text()
        lu_type = self.lookupType.currentText()
        recursive = self.isRecursive.isChecked()
        lu_frmt = self.lookupFormat.currentText()

        cache["delete page"] = {
            "lookupType":   lu_type,
            "currentPath":  path,
            "lookupFormat": lu_frmt,
            "lookupInput":  search,
            "IsRecursive":  recursive,
        }

        with open(self.cache_file, "w+") as file:
            json.dump(cache, file)

    def set_user_path(
        self, path: str,
        is_changed_manually: bool
    ) -> None:
        """
        Update user path input
        """

        # RESET USER PATH
        if not path:
            self.path_input = ""
            return

        self.path_input = path

        if not is_changed_manually:
            self.currentPathInput.setText(path)

    def change_lookup_format(self) -> None:
        """
        Change lookup format options according to the lookup type
        """

        current_type = self.lookupType.currentText()

        # REMOVE ALL TYPES
        self.lookupFormat.clear()

        # GENERATE NEW TYPES
        new_formats = (
            "NAME",
            "PATTERN"
        )

        # ADD THE OPTION 'EXTENSION' IF 'FILES' SELECTED
        if current_type == "FILES":
            new_formats = (
                "NAME",
                "PATTERN",
                "EXTENSION"
            )

        for format in new_formats:
            self.lookupFormat.addItem(format)

    def get_data(self) -> dict:
        """
        ### Begin lookup process. 
            * Deactivate the btn and reactivate it afterwards
        """

        self.startBtn.setEnabled(False)

        input: str = self.lookupInput.text()
        type: str = self.lookupType.currentText()
        format: str = self.lookupFormat.currentText()
        is_recursive: bool = self.isRecursive.isChecked()

        # UPDATE THE FINDER PARAMETERS
        self.controller.update_finder_param(
            self.path_input,
            is_recursive,
        )

        try:
            # BOTH INPUTS REQUIRED
            if not input or not self.path_input:
                print("Empty search input")

            else:
                # SEARCH BY SELECTED FORMAT
                if type == "FILES":
                    match format:
                        case "NAME":
                            return self.controller.get_files_by_name(input)

                        case "EXTENSION":
                            return self.controller.get_files_by_extension(input)

                        case "PATTERN":
                            return self.controller.get_files_by_pattern(input)

                elif type == "FOLDERS":
                    match format:
                        case "NAME":
                            return self.controller.get_folders_by_name(input)

                        case "PATTERN":
                            return self.controller.get_folders_by_pattern(input)

        except Exception as e:
            print(str(e))
            return {}

        finally:
            self.startBtn.setEnabled(True)


class Ui(Mediator):

    def __init__(self) -> None:
        super().__init__()

        self.data = []
        self.checkboxes = []
        self.table_headers = (
            "FILE | FOLDER",
            "SOURCE",
            "SIZE (MB)",
            "SELECT ALL"
        )

        self.thread = None

    def start_lookup_clicked(self):

        if self.controller.show_dialog(
            "WOULD YOU LIKE TO START THE SEARCHING PROCESS?",
            "ARE YOU SURE?"
        ):

            # CACHE USER INPUTS
            self.export_cache()

            # SEARCH PROCESS
            self.data = self.get_data()

            # SET FOUND DATA
            self.update_table()

    def delete_content_clicked(self):

        # IF USER DID NOT ACCEPT DELETE PROCESS, TERMINATE
        if not self.controller.show_dialog(
            "ARE YOU SURE YOU WANT TO *REMOVE* THE SELECTED FILES?",
            "ARE YOU SURE?"
        ):
            return None

        if self.thread is None or not self.thread.isRunning():

            # RESET PROGRESS BAR
            self.progressBar.update(0)

            # DELETE FILES WITH THREADS
            self.thread = DeleteWorker(
                self.data,
                self.checkboxes,
                self.lookupType.currentText()
            )

            # UPDATE PROGRESS BAR
            self.thread.update_progress_signal.connect(
                self.progressBar.update
            )

            # DELETE ROWS FROM THE UI
            self.thread.removed_rows_signal.connect(
                self.remove_deleted_rows
            )

            # SUCCESSFULL REMOVAL ITEMS MESSAGE
            self.thread.is_file_signal.connect(
                lambda is_file: self.controller.show_dialog(
                    f"SUCCESSFULY REMOVED <{self.controller.total_content_removed(is_file)}> ITEM(S)",
                    "OPERATION SUCCESSFULL",
                    is_dialog=False
                )
            )

            self.thread.start()

    def remove_deleted_rows(self, data: list) -> None:
        """
            DELETE ALL ROWS CHECKED AFTER REMOVING THE FILES
        """

        if not data:
            self.controller.show_dialog(
                "NO DATA HAS BEEN SELECTED", is_dialog=False
            )
            return None

        # REMOVE SELECTED CHECKBOXES
        for row in reversed(data):
            self.checkboxes.pop(row)

        # REMOVE ROWS CONTAIN FILES SELECTED
        # START FROM LAST ROW TO AVOID ROW-SHIFTING ISSUE
        for row in reversed(data):
            self.tableLayout.removeRow(row)

        # REINDEX DATA - TO RETRIEVE DATA FROM DICT BY INDEX
        new_data = {}
        for index, value in enumerate(self.data.values()):
            new_data[index] = value
        self.data = new_data

    def restore_files_clicked(self) -> None:

        # PROMPT USER
        if not self.controller.show_dialog(
            "ARE YOU SURE YOU WANT TO *RESTORE* PREVIOUSLY REMOVED ITEMS?",
            "ARE YOU SURE?"
        ):
            return None
        
        # SUCCESSFULL RESTORATION
        self.controller.show_dialog(
            f"SUCCESSFULLY RESTORED <{self.controller.restore_removed_content()}> ITEM(S)", 
            "OPERATION SUCCESSFULL",
            is_dialog=False
        )

    def save_process_clicked(self) -> None:
        # TODO: IMPLEMENT FUNCTION
        pass

    def load_process_clicked(self) -> None:
        # TODO: IMPLEMENT FUNCTION
        pass

    def init_table(self, rows=1, columns=4):
        """
        Render a new table widget with headers
        """

        total_rows = rows
        total_columns = columns

        # CLEAR PREVIOUS ROWS
        self.checkboxes = []
        self.table_layout.setRowCount(0)

        self.table_layout.setRowCount(total_rows)
        self.table_layout.setColumnCount(total_columns)

        # RENDER TABLE HEADERS
        self.table_layout.setHorizontalHeaderLabels(self.table_headers)

        self.retranslateTableHeaders()

    def update_table(self) -> None:
        """
        Display new data on the table
        """

        # RENDER EMPTY TABLE, IF NOTHING FOUND
        if not self.data:
            self.init_table()
            print("no data has been found")
            return

        data = self.data.values()

        # RENDER TABLE HEADERS
        self.init_table(len(data))

        # POPULATE THE TABLE WITH DATA
        for row_index, row_data in enumerate(data):

            for col_index, (_, value) in enumerate(row_data.items()):

                item = QTableWidgetItem(str(value))
                self.table_layout.setItem(row_index, col_index, item)

                # RENDER CHECK ITEMS FOR EACH TABLE-ROW
                if col_index == 2:

                    checkbox = QCheckBox()
                    checkbox.setChecked(True)

                    self.table_layout.setCellWidget(
                        row_index,
                        col_index + 1,
                        checkbox
                    )

                    self.checkboxes.append(checkbox)

        # RESIZE COLUMNS - BASED ON CONTENT SIZE
        for col_index in range(self.table_layout.columnCount()):
            self.table_layout.resizeColumnToContents(col_index)

    def toggle_checkboxes(self, header_section: int) -> None:
        """
        ### TOGGLE THE CHECKBOXES FOR EACH TABLE ITEM
            * Checkboxes column = 3 (zero-indexed)
        """

        if header_section == 3:
            for checkbox in self.checkboxes:
                checkbox.toggle()

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
            self.LookupType_comboBox:   ("FILES", "FOLDERS"),
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
            self.delete_btn:           ("DELETE", "Delete All Selected Items"),
            self.restore_btn:          ("RESTORE", "Restore Last Deleted Process"),
            self.save_btn:             ("SAVE", "Store Current Lookup"),
            self.load_btn:             ("LOAD", "Load Previous Lookup"),
            self.startLookup_btn:      ("START", "Start Lookup Process"),
            self.isRecursive_checkBox: ("RECURSIVE", "Find Files Recursively Through The Selected Path"),
        }

        for widget, info in data.items():
            widget.setText(QCoreApplication.translate(
                "MainWindow", info[0], None))
            widget.setToolTip(QCoreApplication.translate(
                "MainWindow", info[1], None))

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
            QCoreApplication.translate(
                "MainWindow", "Enter the path here", None)
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

        # SET CACHED DATA
        self.import_cache()

    def render_page_icons(self):

        size = (20, 20)

        self.common_functions.set_icon(
            self.browseCurrentPath_btn, "folder_outline", size
        )
        self.common_functions.set_icon(
            self.startLookup_btn, "start", size
        )
        self.common_functions.set_icon(
            self.delete_btn, "delete sign", size
        )
        self.common_functions.set_icon(
            self.restore_btn, "restore file", size
        )
        self.common_functions.set_icon(
            self.load_btn, "file upload", size
        )
        self.common_functions.set_icon(
            self.save_btn, "file download", size
        )

    def render_page(self):
        self.widgets = QWidget()

        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)

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
        self.LookupType_comboBox.setStyleSheet(
            self.html.get_bg_color("dark blue"))
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
        self.currentPath_lineEdit.setStyleSheet(
            self.html.get_bg_color("dark blue"))

        self.second_layout.addWidget(self.currentPath_lineEdit, 0, 1, 1, 1)

        self.browseCurrentPath_btn = QPushButton(self.frame_content_wid_4)
        self.browseCurrentPath_btn.setObjectName("browseCurrentPath_btn")
        self.browseCurrentPath_btn.setMinimumSize(QSize(150, 30))
        self.browseCurrentPath_btn.setFont(font)
        self.browseCurrentPath_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.browseCurrentPath_btn.setStyleSheet(
            self.html.get_bg_color("lightblue"))

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
        self.lookupInput_lineEdit.setStyleSheet(
            self.html.get_bg_color("dark blue"))

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
        self.lookupFormat_comboBox.setStyleSheet(
            self.html.get_bg_color("dark blue"))
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

        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)

        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)

        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)

        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)

        self.table_layout.setFrameShape(QFrame.NoFrame)
        self.table_layout.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.table_layout.setSizeAdjustPolicy(
            QAbstractScrollArea.AdjustToContents)
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

        # BUTTONS DESIGN
        btns = {
            "delete_btn": self.delete_btn,
            "restore_btn": self.restore_btn,
            "save_btn": self.save_btn,
            "load_btn": self.load_btn
        }

        for btn_name, btn in btns.items():
            btn.setObjectName(btn_name)
            btn.setMinimumSize(QSize(150, 30))
            btn.setStyleSheet(self.html.get_bg_color("lightblue"))
            btn.setCursor(QCursor(Qt.PointingHandCursor))
            btn.setFont(font)

            self.optionBtns_layout.addWidget(btn)

        self.horizontalLayout_12.addLayout(self.optionBtns_layout)
        self.verticalLayout.addWidget(self.row_3)

        # STORE WIDGETS IN CONTROLLER
        # To eliminate the need of params in each func call from the controller
        # Pass all widgets required for controller methods here
        self.set_controller_widgets(
            self.LookupType_comboBox,
            self.currentPath_lineEdit,
            self.lookupFormat_comboBox,
            self.lookupInput_lineEdit,
            self.isRecursive_checkBox,
            self.startLookup_btn,
            self.table_layout
        )

        self.retranslateUi()
        self.render_page_icons()

        """
        ////////////////////////////////////////////////
                BUTTONS & EVENT/SIGNAL
        ////////////////////////////////////////////////
        """

        # MANUALY ENTERED PATH
        self.currentPath_lineEdit.textChanged.connect(
            lambda: self.set_user_path(
                self.currentPath_lineEdit.text(),
                True
            )
        )

        self.browseCurrentPath_btn.clicked.connect(
            lambda: self.set_user_path(
                self.common_functions.get_user_path(),
                False
            )
        )

        self.startLookup_btn.clicked.connect(
            lambda: self.start_lookup_clicked()
        )

        self.delete_btn.clicked.connect(
            lambda: self.delete_content_clicked()
        )

        self.save_btn.clicked.connect(
            lambda: self.save_process_clicked()
        )

        self.load_btn.clicked.connect(
            lambda: self.load_process_clicked()
        )

        self.restore_btn.clicked.connect(
            lambda: self.restore_files_clicked()
        )

        self.LookupType_comboBox.currentTextChanged.connect(
            lambda: self.change_lookup_format()
        )

        # ON TABLE-HEADER CLICK
        self.table_layout.horizontalHeader().sectionClicked.connect(
            self.toggle_checkboxes
        )

        return self.widgets
