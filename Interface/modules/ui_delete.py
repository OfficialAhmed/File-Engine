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
        lookupType:            QPushButton,
        currentPath:           QLineEdit,
        lookupFormat:          QLineEdit,
        lookupInput:           QCheckBox,
        isRecursive:           QLineEdit,
        startBtn:              QComboBox
    ):
        """
        Set current window widgets from 'UI' class
        """
        self.startBtn:         QPushButton = startBtn
        self.lookupType:       QComboBox = lookupType
        self.lookupInput:      QLineEdit = lookupInput
        self.isRecursive:      QCheckBox = isRecursive
        self.lookupFormat:     QComboBox = lookupFormat
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

    def get_data(self) -> (dict, bool):
        """
        ### Begin lookup process. 
            * Deactivate all btns and reactivate upon end of process 
        """

        input: str = self.lookupInput.text()
        type: str = self.lookupType.currentText()
        format: str = self.lookupFormat.currentText()
        is_recursive: bool = self.isRecursive.isChecked()

        # UPDATE THE FINDER PARAMETERS
        self.controller.update_finder_param(
            self.path_input,
            is_recursive,
        )

        data = {}

        # TERMINATE IF EITHER INPUTS ARE EMPTY
        if not input or not self.path_input:
            self.controller.show_dialog(
                "SEARCH INPUT IS EMPTY!",
                "w",
                is_dialog=False
            )

            return (data, True)                 # FAILED = True

        # TERMINATE IF ENTERED PATH CANNOT BE FOUND
        if not os.path.exists(self.currentPathInput.text()):
            self.controller.show_dialog(
                "FOLDER DOESN'T EXIST. DOUBLE CHECK THE ENTERED PATH",
                "w",
                is_dialog=False
            )

            return (data, True)                 # FAILED = True

        try:
            # SEARCH BY SELECTED FORMAT
            if type == "FILES":
                match format:
                    case "NAME":
                        data = self.controller.get_files_by_name(input)

                    case "EXTENSION":
                        data = self.controller.get_files_by_extension(input)

                    case "PATTERN":
                        data = self.controller.get_files_by_pattern(input)

            elif type == "FOLDERS":
                match format:
                    case "NAME":
                        data = self.controller.get_folders_by_name(input)

                    case "PATTERN":
                        data = self.controller.get_folders_by_pattern(input)

            return (data, False)

        except Exception as e:
            self.controller.show_dialog(
                f"UNKNOWN ERROR OCCURED | {str(e)}",
                "c",
                is_dialog=False
            )

            return (data, True)                 # FAILED = True


class Ui(Mediator):

    def __init__(self) -> None:
        super().__init__()

        self.data = {}
        self.checkboxes = []
        self.table_headers = (
            "FILE | FOLDER",
            "SOURCE",
            "SIZE (MB)",
            "SELECT / DESELECT"
        )

    def generate_table(self):
        """
            GENERATE THE TABLE USING THE SELF.DATA
        """

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
                        row_index,                      # ROW INDEX
                        3,                              # LAST COLUMN
                        checkbox                        # ITEM
                    )

                    self.checkboxes.append(checkbox)

        # RESIZE COLUMNS - BASED ON CONTENT SIZE
        for col_index in range(self.table_layout.columnCount()):
            self.table_layout.resizeColumnToContents(col_index)

    def start_lookup_clicked(self):

        if self.controller.show_dialog(
            "WOULD YOU LIKE TO START THE SEARCHING PROCESS?",
            "ARE YOU SURE?"
        ):

            # CACHE USER INPUTS
            self.export_cache()

            # SEARCH PROCESS
            self.startBtn.setEnabled(False)
            self.data, is_failed = self.get_data()
            self.startBtn.setEnabled(True)

            # THE PROCESS FAILED TO FETCH DATA. A MESSAGE HAS BEEN SHOWN TO THE USER.
            if is_failed:
                return None

            # PATH EXISTED BUT NO FILES HAVE BEEN FOUND
            if not self.data:
                self.init_table()

                self.controller.show_dialog(
                    "NO DATA HAS BEEN FOUND!",          # MESSAGE
                    "ITEMS CANNOT BE FOUND!",           # WINDOW TITLE
                    is_dialog=False                     # FALSE = INFORMATIONAL
                )
                return None

            self.generate_table()

    def delete_content_clicked(self):

        # IF USER DID NOT ACCEPT DELETE PROCESS, TERMINATE
        if not self.controller.show_dialog(
            "ARE YOU SURE YOU WANT TO *REMOVE* THE SELECTED FILES?",
            "ARE YOU SURE?"
        ):
            return None

        # RESET PROGRESS BAR
        self.progressBar.update(0)

        files_to_remove = []
        self.rows_to_remove = []

        # FLAG SELECTED TABLE ITEMS
        for indx, cb in enumerate(self.checkboxes):

            # IF CHECKBOX SELECTED
            if cb.isChecked():

                # FETCH DATA FROM TABLE
                file = self.table_layout.item(
                    indx, 0                                 # EACH ROW, 1ST COLUMN
                ).text()

                root = self.table_layout.item(
                    indx, 1                                 # EACH ROW, 2ND COLUMN
                ).text()

                files_to_remove.append(f"{root}//{file}")
                self.rows_to_remove.append(indx)

        # DELETE FILES WITH THREADS
        future_process = DeleteWorker(
            files_to_remove,
            self.lookupType.currentText()
        )

        # UPDATE PROGRESS BAR
        future_process.progress_signal.connect(
            self.progressBar.update
        )

        # DELETE ROWS FROM THE UI
        future_process.remove_rows_signal.connect(
            self.remove_table_rows
        )

        # SUCCESSFULL ITEMS REMOVAL MESSAGE
        future_process.is_success.connect(
            self.removing_process_state
        )

        # UNSUCCESSFULL ITEMS REMOVAL MESSAGE
        future_process.is_fail.connect(
            lambda error: self.controller.show_dialog(
                f"SOMTHING WENT WRONG WHILE REMOVING | ERROR <{error}>",
                "C",
                False
            )
        )

        future_process.run()

    def restore_files_clicked(self) -> None:

        # PROMPT USER
        if not self.controller.show_dialog(
            "ARE YOU SURE YOU WANT TO *RESTORE* PREVIOUSLY REMOVED ITEMS?",
            "ARE YOU SURE?"
        ):
            return None

        try:

            trash_file = self.controller.TRASH_CONTENT_FILE

            # FILE MUST EXIST AND NOT EMPTY, ELSE TERMINATE PROCESS
            if not os.path.exists(trash_file) or not os.path.getsize(trash_file) > 0:

                self.controller.show_dialog(
                    f"CANNOT FIND DELETED FILES.",
                    "I",
                    False
                )

                return None

            # FETCH CONTENT RESTORE DATA
            data: dict = json.load(open(trash_file))

            # RESTORE FILES WITH THREADS
            future_process = RestoreWorker(data)

            # UPDATE PROGRESS BAR WITH THE VALUE RETURNED BY THE SIGNAL
            future_process.progress_signal.connect(
                self.progressBar.update
            )

            # SUCCESSFULL ITEMS REMOVAL MESSAGE
            future_process.is_success.connect(
                self.removing_process_state
            )

            # UNSUCCESSFULL ITEMS REMOVAL MESSAGE
            future_process.is_fail.connect(
                lambda error: self.controller.show_dialog(
                    f"SOMTHING WENT WRONG WHILE RESTORING | ERROR <{error}>",
                    "C",
                    False
                )
            )

            future_process.run()

        except Exception as e:

            self.controller.show_dialog(
                f"CANNOT READ RESTORE FILE. ERROR| {e}",
                "C",
                is_dialog=False
            )
            return None

    def export_process_clicked(self) -> None:
        """
        EXPORT CURRENT DATA FOR LATER USE (FOR THE LOADING PROCESS)
        """

        # IF NO DATA HAS BEEN FOUND, RETURN
        if not self.data:
            self.controller.show_dialog(
                f"TO EXPORT THE CURRENT PROCESS, YOU NEED TO START THE PROCESS FIRST!",
                "I",
                is_dialog=False
            )

            return None

        # GET FILE DESTINATION
        folder_path = self.common_functions.get_path()
        path = f"{folder_path}\\{self.common_functions.get_timestamp()}.json"

        if folder_path:

            with open(path, "w") as file:
                json.dump(self.data, file)

            # CHECK IF FILE EXPORTED SUCCESSFULLY
            if os.path.exists(path) and os.path.getsize(path) > 0:
                self.controller.show_dialog(
                    f"PROCESS EXPORTED SUCCESSFULLY!",
                    "I",
                    is_dialog=False
                )

            else:
                self.controller.show_dialog(
                    f"SOMETHING WENT WRONG! PROCESS WASN'T EXPORTED. PLEASE TRY AGAIN!",
                    "C",
                    is_dialog=False
                )

    def import_process_clicked(self) -> None:
        """
            OVERWRITE THE DATA FROM A JSON FILE GENERATED BY THE SAVE PROCESS
            THEN POPULATE THE DATA ONTO A NEW GENERATED TABLE
        """
        self.data = json.load(open(self.common_functions.get_path("json")))
        self.generate_table()

    def removing_process_state(self, state: bool):

        if state:
            self.controller.show_dialog(
                f"SUCCESSFULY REMOVED ALL ITEM(S)",
                "OPERATION SUCCESSFULL",
                False
            )

        else:
            self.controller.show_dialog(
                f"SOME FILE(S) WEREN'T REMOVED SUCCESSFULY",
                "OPERATION NOT FULLY SUCCESSFULL",
                False
            )

    def init_table(self, rows=1, columns=4):
        """
        Render a new table widget with headers
        """

        total_rows = rows
        total_columns = columns

        # CLEAR PREVIOUS ROWS
        self.checkboxes.clear()
        self.table_layout.setRowCount(0)

        self.table_layout.setRowCount(total_rows)
        self.table_layout.setColumnCount(total_columns)

        # RENDER TABLE HEADERS
        self.table_layout.setHorizontalHeaderLabels(self.table_headers)

        self.retranslateTableHeaders()

    def table_header_clicked(self, header_section: int) -> None:
        """
        ### ON TABLE HEADER CLICK 

            Zero-indexed header
            * On click header `0` `1` `2` -> re-render checkboxes
            * On click header `3`         -> (De)Select Checkboxes
        """

        if header_section == 3:

            # SELECT/DESELCT ALL CHECKBOXES
            for checkbox in self.checkboxes:
                checkbox.toggle()

        else:

            # RE-RENDER TABLE CHECKBOXES TO REARRANGE THEM BASED ON THE NEW SORT
            total_checkboxes = len(self.checkboxes)
            self.checkboxes.clear()

            for row_indx in range(total_checkboxes):

                checkbox = QCheckBox()
                checkbox.setChecked(False)

                self.table_layout.setCellWidget(
                    row_indx,                            # ROW INDEX
                    3,                                   # LAST COLUMN
                    checkbox                             # ITEM
                )

                self.checkboxes.append(checkbox)

    def remove_table_rows(self) -> None:
        """
            DELETE ALL CHECKED ROWS AFTER REMOVING THE FILES
        """

        if not self.rows_to_remove:
            self.controller.show_dialog(
                "NO DATA HAS BEEN SELECTED", is_dialog=False
            )
            return None

        # REMOVE SELECTED CHECKBOXES
        for row in reversed(self.rows_to_remove):
            self.table_layout.removeRow(row)
            self.checkboxes.pop(row)

    def retranslateTableHeaders(self):

        for col, txt in enumerate(self.table_headers):

            header_item = QTableWidgetItem(
                QCoreApplication.translate("MainWindow", txt)
            )

            self.table_layout.setHorizontalHeaderItem(col, header_item)

    def render_page(self):
        self.widgets = QWidget()

        """
        ===================================================================
                        SET WIDGETS (SENSITIVE LAYOUT)
        ===================================================================
        """
        self.first_layout = QGridLayout()
        self.third_layout = QGridLayout()
        self.second_layout = QGridLayout()

        self.verticalLayout = QVBoxLayout(self.widgets)
        self.frame_content_wid_3 = QFrame(self.widgets)

        self.PageTitle_label = QLabel(self.frame_content_wid_3)
        self.LookupType_comboBox = QComboBox(self.frame_content_wid_3)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_content_wid_3)

        self.frame_content_wid_4 = QFrame(self.widgets)
        self.currentPath_lineEdit = QLineEdit(self.frame_content_wid_4)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_content_wid_4)
        self.browseCurrentPath_btn = QPushButton(self.frame_content_wid_4)

        self.frame_content_wid_2 = QFrame(self.widgets)
        self.LookuByTitle_label = QLabel(self.frame_content_wid_2)
        self.startLookup_btn = QPushButton(self.frame_content_wid_2)
        self.isRecursive_checkBox = QCheckBox(self.frame_content_wid_2)
        self.lookupInput_lineEdit = QLineEdit(self.frame_content_wid_2)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_content_wid_2)
        self.lookupFormat_comboBox = QComboBox(self.frame_content_wid_2)

        self.row_1 = QFrame(self.widgets)
        self.verticalLayout_16 = QVBoxLayout(self.row_1)

        self.row_3 = QFrame(self.widgets)
        self.horizontalLayout_12 = QHBoxLayout(self.row_3)

        self.first_layout.addWidget(self.PageTitle_label, 0, 0, 1, 1)
        self.first_layout.addWidget(self.LookupType_comboBox, 1, 0, 1, 1)
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.first_layout.addItem(self.horizontalSpacer, 1, 1, 1, 1)
        self.horizontalLayout_11.addLayout(self.first_layout)
        self.verticalLayout.addWidget(self.frame_content_wid_3)
        self.verticalLayout.addWidget(self.row_1)
        self.second_layout.addWidget(self.currentPath_lineEdit, 0, 1, 1, 1)
        self.second_layout.addWidget(self.browseCurrentPath_btn, 0, 2, 1, 1)
        self.horizontalLayout_13.addLayout(self.second_layout)
        self.verticalLayout.addWidget(self.frame_content_wid_4)
        self.third_layout.addWidget(self.lookupInput_lineEdit, 1, 1, 1, 1)
        self.third_layout.addWidget(self.startLookup_btn, 1, 2, 1, 1)
        self.third_layout.addWidget(self.lookupFormat_comboBox, 1, 0, 1, 1)
        self.third_layout.addWidget(self.isRecursive_checkBox, 2, 0, 1, 1)

        self.LookuByTitle_label.setLineWidth(1)
        self.LookuByTitle_label.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter
        )

        self.LookupType_comboBox.setFrame(True)
        self.lookupFormat_comboBox.setFrame(True)

        self.isRecursive_checkBox.setChecked(True)

        self.startLookup_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.browseCurrentPath_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.third_layout.addWidget(self.LookuByTitle_label, 0, 0, 1, 1)
        self.horizontalLayout_10.addLayout(self.third_layout)
        self.verticalLayout.addWidget(self.frame_content_wid_2)

        self.verticalLayout.setSpacing(10)
        self.verticalLayout_16.setSpacing(0)
        self.horizontalLayout_12.setSpacing(0)

        """
        ===================================================================
                                SET FRAMINGS
        ===================================================================
        """
        self.row_3.setMinimumSize(QSize(0, 150))
        self.startLookup_btn.setMinimumSize(QSize(150, 30))
        self.currentPath_lineEdit.setMinimumSize(QSize(0, 30))
        self.lookupInput_lineEdit.setMinimumSize(QSize(0, 30))
        self.browseCurrentPath_btn.setMinimumSize(QSize(150, 30))

        self.row_3.setFrameShadow(QFrame.Raised)
        self.row_1.setFrameShadow(QFrame.Raised)
        self.frame_content_wid_2.setFrameShadow(QFrame.Raised)
        self.frame_content_wid_3.setFrameShadow(QFrame.Raised)
        self.frame_content_wid_4.setFrameShadow(QFrame.Raised)

        self.row_1.setFrameShape(QFrame.StyledPanel)
        self.row_3.setFrameShape(QFrame.StyledPanel)
        self.frame_content_wid_3.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_4.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_2.setFrameShape(QFrame.NoFrame)

        self.LookupType_comboBox.setAutoFillBackground(False)
        self.isRecursive_checkBox.setAutoFillBackground(False)
        self.lookupFormat_comboBox.setAutoFillBackground(False)

        """
        ===================================================================
                                SET MARGINS
        ===================================================================
        """
        self.third_layout.setContentsMargins(-1, -1, -1, 0)
        self.second_layout.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)

        """
        ===================================================================
                                SET FONTS
        ===================================================================
        """
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)

        self.startLookup_btn.setFont(font)
        self.PageTitle_label.setFont(font)
        self.LookupType_comboBox.setFont(font)
        self.browseCurrentPath_btn.setFont(font)
        self.lookupFormat_comboBox.setFont(font)

        """
        ===================================================================
                                TABLE CONTENT
        ===================================================================
        """
        self.table_layout = QTableWidget(self.row_3)

        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            self.table_layout.sizePolicy().hasHeightForWidth()
        )
        self.table_layout.setSizePolicy(sizePolicy3)

        self.init_table()

        """
        ===================================================================
                           PALLETE AND BRUSHES
        ===================================================================
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

        self.delete_btn = QPushButton(self.row_3)
        self.restore_btn = QPushButton(self.row_3)
        self.export_btn = QPushButton(self.row_3)
        self.import_btn = QPushButton(self.row_3)

        # BUTTONS DESIGN
        btns = {
            "delete_btn": self.delete_btn,
            "restore_btn": self.restore_btn,
            "export_btn": self.export_btn,
            "import_btn": self.import_btn
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
            self.startLookup_btn
        )

        """
        ===================================================================
                            SET STYLESHEET
        ===================================================================
        """

        self.LookupType_comboBox.setStyleSheet(
            self.html.get_bg_color("dark blue")
        )
        self.currentPath_lineEdit.setStyleSheet(
            self.html.get_bg_color("dark blue")
        )
        self.browseCurrentPath_btn.setStyleSheet(
            self.html.get_bg_color("lightblue")
        )
        self.lookupInput_lineEdit.setStyleSheet(
            self.html.get_bg_color("dark blue")
        )
        self.startLookup_btn.setStyleSheet(
            self.html.get_bg_color("lightblue")
        )
        self.lookupFormat_comboBox.setStyleSheet(
            self.html.get_bg_color("dark blue")
        )
        self.LookuByTitle_label.setStyleSheet(
            "color: rgb(113, 126, 149)"
        )

        """
        ===================================================================
                           SET OBJECT NAMES
        ===================================================================
        """
        self.row_1.setObjectName("row_1")
        self.row_3.setObjectName("row_3")
        self.widgets.setObjectName("widgets")
        self.table_layout.setObjectName("table_layout")
        self.first_layout.setObjectName("first_layout")
        self.third_layout.setObjectName("third_layout")
        self.second_layout.setObjectName("second_layout")
        self.verticalLayout.setObjectName("verticalLayout")
        self.startLookup_btn.setObjectName("startLookup_btn")
        self.PageTitle_label.setObjectName("PageTitle_label")
        self.optionBtns_layout.setObjectName("optionBtns_layout")
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.LookuByTitle_label.setObjectName("LookuByTitle_label")
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.frame_content_wid_2.setObjectName("frame_content_wid_2")
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.frame_content_wid_3.setObjectName("frame_content_wid_3")
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.LookupType_comboBox.setObjectName("LookupType_comboBox")
        self.frame_content_wid_4.setObjectName("frame_content_wid_4")
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.isRecursive_checkBox.setObjectName("isRecursive_checkBox")
        self.currentPath_lineEdit.setObjectName("currentPath_lineEdit")
        self.browseCurrentPath_btn.setObjectName("browseCurrentPath_btn")
        self.lookupFormat_comboBox.setObjectName("currentLookupBy_comboBox")
        self.lookupInput_lineEdit.setObjectName("currentLookupInput_lineEdit")

        self.retranslateUi()

        """
        ===================================================================
                        RENDER PAGE ICONS
        ===================================================================
        """
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
            self.import_btn, "file upload", size
        )
        self.common_functions.set_icon(
            self.export_btn, "file download", size
        )

        """
        ===================================================================
                        BUTTONS & EVENT/SIGNAL
        ===================================================================
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
                self.common_functions.get_path(),
                False
            )
        )

        self.startLookup_btn.clicked.connect(
            lambda: self.start_lookup_clicked()
        )

        self.delete_btn.clicked.connect(
            lambda: self.delete_content_clicked()
        )

        self.export_btn.clicked.connect(
            lambda: self.export_process_clicked()
        )

        self.import_btn.clicked.connect(
            lambda: self.import_process_clicked()
        )

        self.restore_btn.clicked.connect(
            lambda: self.restore_files_clicked()
        )

        self.LookupType_comboBox.currentTextChanged.connect(
            lambda: self.change_lookup_format()
        )

        # ON TABLE-HEADER CLICK
        self.table_layout.horizontalHeader().sectionClicked.connect(
            self.table_header_clicked
        )

        return self.widgets


    def retranslateUi(self):
        """
        TRANSLATE UI TEXT
        """

        """
        ===================================================================
                        COMOBOXES ITEMS
        ===================================================================
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
        ===================================================================
                        SET TEXT / TOOL TIPS
        ===================================================================
        """

        data = {
            self.delete_btn:           ("DELETE", "Delete All Selected Items"),
            self.restore_btn:          ("RESTORE", "Restore Last Deleted Process"),
            self.export_btn:           ("EXPORT", "Store Current Lookup"),
            self.import_btn:           ("IMPORT", "Load Previous Lookup"),
            self.startLookup_btn:      ("START", "Start Lookup Process"),
            self.isRecursive_checkBox: ("RECURSIVE", "Find Files Recursively Through The Selected Path"),
        }

        for widget, info in data.items():
            widget.setText(QCoreApplication.translate(
                "MainWindow", info[0], None
            )
            )
            widget.setToolTip(QCoreApplication.translate(
                "MainWindow", info[1], None
            )
            )

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
                "MainWindow", "Enter the path here", None
            )
        )
        self.browseCurrentPath_btn.setText(
            QCoreApplication.translate(
                "MainWindow", "OPEN", None
            )
        )
        self.lookupInput_lineEdit.setPlaceholderText(
            QCoreApplication.translate(
                "MainWindow", "Enter your input", None
            )
        )
        self.LookuByTitle_label.setText(
            QCoreApplication.translate(
                "MainWindow", "LOOKUP BY", None
            )
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
