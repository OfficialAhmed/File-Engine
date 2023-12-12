
from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QSize, Qt
from PySide6.QtGui import QBrush, QColor, QCursor, QFont, QIcon, QPalette
from PySide6.QtWidgets import (
    QAbstractItemView, QAbstractScrollArea, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem, QTextEdit,
    QVBoxLayout, QWidget
)

import os
import json
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

            cache: dict = json.load(open(self.cache_file)).get("rename page")

            if cache:
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

    def rename_content_clicked(self):
        # TODO: CHANGE METHOD

        # IF USER DID NOT ACCEPT DELETE PROCESS, TERMINATE
        if not self.controller.show_dialog(
            "ARE YOU SURE YOU WANT TO *REMOVE* THE SELECTED FILES?",
            "ARE YOU SURE?"
        ):
            return None

        # RESET PROGRESS BAR
        self.progressBar.update(100)
        print("renaming process started...")

        # files_to_remove = []
        # self.rows_to_remove = []

        # FLAG SELECTED TABLE ITEMS
        # for indx, cb in enumerate(self.checkboxes):

        #     # IF CHECKBOX SELECTED
        #     if cb.isChecked():

        #         # FETCH DATA FROM TABLE
        #         file = self.table_layout.item(
        #             indx, 0                                 # EACH ROW, 1ST COLUMN
        #         ).text()

        #         root = self.table_layout.item(
        #             indx, 1                                 # EACH ROW, 2ND COLUMN
        #         ).text()

        #         files_to_remove.append(f"{root}//{file}")
        #         self.rows_to_remove.append(indx)

        # # DELETE FILES WITH THREADS
        # future_process = DeleteWorker(
        #     files_to_remove,
        #     self.lookupType.currentText()
        # )

        # # UPDATE PROGRESS BAR
        # future_process.progress_signal.connect(
        #     self.progressBar.update
        # )

        # # DELETE ROWS FROM THE UI
        # future_process.remove_rows_signal.connect(
        #     self.remove_table_rows
        # )

        # # SUCCESSFULL ITEMS REMOVAL MESSAGE
        # future_process.is_success.connect(
        #     self.removing_process_state
        # )

        # # UNSUCCESSFULL ITEMS REMOVAL MESSAGE
        # future_process.is_fail.connect(
        #     lambda error: self.controller.show_dialog(
        #         f"SOMTHING WENT WRONG WHILE REMOVING | ERROR <{error}>",
        #         "C",
        #         False
        #     )
        # )

        # future_process.run()

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
        # TODO: CHANGE METHOD

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
        self.second_layout = QGridLayout()
        self.third_layout = QGridLayout()

        self.row_3 = QFrame(self.widgets)
        self.table_layout = QTableWidget(self.row_3)
        self.frame_content_wid_3 = QFrame(self.widgets)
        self.frame_content_wid_2 = QFrame(self.widgets)
        self.frame_content_wid_4 = QFrame(self.widgets)

        self.verticalLayout = QVBoxLayout(self.widgets)
        self.PageTitle_label = QLabel(self.frame_content_wid_3)
        self.LookuByTitle_label = QLabel(self.frame_content_wid_2)
        self.startLookup_btn = QPushButton(self.frame_content_wid_2)
        self.renameBy_comboBox = QComboBox(self.frame_content_wid_4)
        self.renameBy2_comboBox = QComboBox(self.frame_content_wid_4)
        self.LookupType_comboBox = QComboBox(self.frame_content_wid_3)
        self.lookupInput_lineEdit = QLineEdit(self.frame_content_wid_2)
        self.isRecursive_checkBox = QCheckBox(self.frame_content_wid_2)
        self.renameValue_lineEdit = QLineEdit(self.frame_content_wid_4)
        self.currentPath_lineEdit = QLineEdit(self.frame_content_wid_3)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_content_wid_3)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_content_wid_2)
        self.lookupFormat_comboBox = QComboBox(self.frame_content_wid_2)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_content_wid_4)
        self.lookupFormat2_comboBox = QComboBox(self.frame_content_wid_2)
        self.lookupFormat3_comboBox = QComboBox(self.frame_content_wid_2)
        self.browseCurrentPath_btn = QPushButton(self.frame_content_wid_3)

        self.optionBtns_layout = QVBoxLayout()
        self.rename_btn = QPushButton(self.row_3)
        self.export_btn = QPushButton(self.row_3)
        self.import_btn = QPushButton(self.row_3)
        self.restore_btn = QPushButton(self.row_3)

        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame_content_wid_3.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11.setContentsMargins(-1, 5, -1, 5)
        self.LookupType_comboBox.setAutoFillBackground(False)

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
        self.startLookup_btn.setStyleSheet(
            self.html.get_bg_color("light blue")
        )

        self.renameBy_comboBox.setStyleSheet(
            self.html.get_bg_color("dark blue")
        )

        self.renameBy2_comboBox.setStyleSheet(
            self.html.get_bg_color("dark blue")
        )

        self.LookupType_comboBox.setStyleSheet(
            self.html.get_bg_color("dark blue")
        )

        self.currentPath_lineEdit.setStyleSheet(
            self.html.get_bg_color("dark blue")
        )

        self.lookupInput_lineEdit.setStyleSheet(
            self.html.get_bg_color("dark blue")
        )

        self.renameValue_lineEdit.setStyleSheet(
            self.html.get_bg_color("dark blue")
        )

        self.lookupFormat_comboBox.setStyleSheet(
            self.html.get_bg_color("dark blue")
        )

        self.lookupFormat2_comboBox.setStyleSheet(
            self.html.get_bg_color("dark blue")
        )

        self.lookupFormat3_comboBox.setStyleSheet(
            self.html.get_bg_color("dark blue")
        )

        self.browseCurrentPath_btn.setStyleSheet(
            self.html.get_bg_color("light blue")
        )

        self.horizontalLayout_11.addLayout(self.first_layout)

        """
        ===================================================================
                                SET FRAMINGS
        ===================================================================
        """
        self.row_3.setMinimumSize(QSize(0, 150))
        self.rename_btn.setMinimumSize(QSize(150, 30))
        self.export_btn.setMinimumSize(QSize(150, 30))
        self.import_btn.setMinimumSize(QSize(150, 30))
        self.restore_btn.setMinimumSize(QSize(150, 30))
        self.startLookup_btn.setMinimumSize(QSize(150, 30))
        self.lookupInput_lineEdit.setMinimumSize(QSize(0, 30))
        self.currentPath_lineEdit.setMinimumSize(QSize(0, 30))
        self.renameValue_lineEdit.setMinimumSize(QSize(0, 30))
        self.browseCurrentPath_btn.setMinimumSize(QSize(150, 30))

        self.frame_content_wid_2.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.setContentsMargins(-1, 5, -1, 5)
        self.second_layout.setContentsMargins(-1, -1, -1, 0)
        self.lookupInput_lineEdit.setMaxLength(100)

        self.LookuByTitle_label.setLineWidth(1)
        self.LookuByTitle_label.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.renameBy_comboBox.setFrame(True)
        self.renameBy2_comboBox.setFrame(True)
        self.LookupType_comboBox.setFrame(True)
        self.lookupFormat_comboBox.setFrame(True)
        self.lookupFormat2_comboBox.setFrame(True)
        self.lookupFormat3_comboBox.setFrame(True)

        self.renameBy_comboBox.setAutoFillBackground(False)
        self.renameBy2_comboBox.setAutoFillBackground(False)
        self.isRecursive_checkBox.setAutoFillBackground(False)
        self.lookupFormat_comboBox.setAutoFillBackground(False)
        self.lookupFormat2_comboBox.setAutoFillBackground(False)
        self.lookupFormat3_comboBox.setAutoFillBackground(False)

        self.row_3.setFrameShape(QFrame.StyledPanel)
        self.table_layout.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_4.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_4.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addLayout(self.second_layout)

        self.third_layout.setContentsMargins(-1, -1, -1, 0)
        self.renameValue_lineEdit.setMaxLength(50)

        self.horizontalSpacer_3 = QSpacerItem(
            20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.third_layout.addItem(self.horizontalSpacer_3, 2, 1, 1, 1)
        self.horizontalLayout_13.addLayout(self.third_layout)

        self.row_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.row_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)

        self.first_layout.addWidget(self.LookupType_comboBox, 1, 0, 1, 1)
        self.first_layout.addWidget(self.PageTitle_label, 0, 0, 1, 1)
        self.first_layout.addWidget(self.currentPath_lineEdit, 1, 1, 1, 1)
        self.first_layout.addWidget(self.browseCurrentPath_btn, 1, 2, 1, 1)
        self.second_layout.addWidget(self.lookupInput_lineEdit, 1, 3, 1, 1)
        self.second_layout.addWidget(self.lookupFormat_comboBox, 1, 0, 1, 1)
        self.second_layout.addWidget(self.LookuByTitle_label, 0, 0, 1, 1)
        self.second_layout.addWidget(self.lookupFormat2_comboBox, 1, 1, 1, 1)
        self.second_layout.addWidget(self.lookupFormat3_comboBox, 1, 2, 1, 1)
        self.third_layout.addWidget(self.startLookup_btn, 1, 3, 1, 1)
        self.third_layout.addWidget(self.renameValue_lineEdit, 1, 2, 1, 1)
        self.third_layout.addWidget(self.renameBy_comboBox, 1, 0, 1, 1)
        self.third_layout.addWidget(self.renameBy2_comboBox, 1, 1, 1, 1)
        self.third_layout.addWidget(self.isRecursive_checkBox, 2, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_content_wid_3)
        self.verticalLayout.addWidget(self.frame_content_wid_2)
        self.verticalLayout.addWidget(self.frame_content_wid_4)
        self.verticalLayout.addWidget(self.row_3)
        self.horizontalLayout_12.addWidget(self.table_layout)
        self.optionBtns_layout.addWidget(self.rename_btn)
        self.optionBtns_layout.addWidget(self.restore_btn)
        self.optionBtns_layout.addWidget(self.export_btn)
        self.optionBtns_layout.addWidget(self.import_btn)
        self.horizontalLayout_12.addLayout(self.optionBtns_layout)

        self.row_3.setObjectName(u"row_3")
        self.widgets.setObjectName(u"widgets")
        self.first_layout.setObjectName(u"first_layout")
        self.third_layout.setObjectName(u"third_layout")
        self.second_layout.setObjectName(u"second_layout")
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.PageTitle_label.setObjectName(u"PageTitle_label")
        self.startLookup_btn.setObjectName(u"startLookup_btn")
        self.optionBtns_layout.setObjectName(u"optionBtns_layout")
        self.renameBy_comboBox.setObjectName(u"renameBy_comboBox")
        self.LookuByTitle_label.setObjectName(u"LookuByTitle_label")
        self.renameBy2_comboBox.setObjectName(u"renameBy2_comboBox")
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.LookupType_comboBox.setObjectName(u"LookupType_comboBox")
        self.frame_content_wid_3.setObjectName(u"frame_content_wid_3")
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.frame_content_wid_4.setObjectName(u"frame_content_wid_4")
        self.frame_content_wid_2.setObjectName(u"frame_content_wid_2")
        self.renameValue_lineEdit.setObjectName(u"renameValue_lineEdit")
        self.currentPath_lineEdit.setObjectName(u"currentPath_lineEdit")
        self.lookupInput_lineEdit.setObjectName(u"lookupInput_lineEdit")
        self.isRecursive_checkBox.setObjectName(u"isRecursive_checkBox")
        self.browseCurrentPath_btn.setObjectName(u"browseCurrentPath_btn")
        self.lookupFormat_comboBox.setObjectName(u"lookupFormat_comboBox")
        self.lookupFormat3_comboBox.setObjectName(u"lookupFormat3_comboBox")
        self.LookuByTitle_label.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.lookupFormat2_comboBox.setObjectName(u"lookupFormat2_comboBox")

        """
        ===================================================================
                                TABLE CONTENT
        ===================================================================
        """

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

        self.startLookup_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.browseCurrentPath_btn.setCursor(QCursor(Qt.PointingHandCursor))

        # BUTTONS DESIGN
        btns = {
            "rename_btn":           self.rename_btn,
            "export_btn":           self.export_btn,
            "import_btn":           self.import_btn,
            "restore_btn":          self.restore_btn,
        }

        for btn_name, btn in btns.items():
            btn.setObjectName(btn_name)
            btn.setMinimumSize(QSize(150, 30))
            btn.setStyleSheet(self.html.get_bg_color("light blue"))
            btn.setCursor(QCursor(Qt.PointingHandCursor))

            self.optionBtns_layout.addWidget(btn)

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
            self.rename_btn, "delete sign", size
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

        self.rename_btn.clicked.connect(
            lambda: self.rename_content_clicked()
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
                        COMBOBOXES ITEMS
        ===================================================================
        """

        data = {
            self.LookupType_comboBox:   (
                "FILES", "FOLDERS"
            ),
            self.lookupFormat_comboBox: (
                "NAME", "EXTENSION"
            ),
            self.lookupFormat2_comboBox: (
                "CONTAIN", "EQUAL TO"
            ),
            self.lookupFormat3_comboBox: (
                "Alphabets only", "Alphabets & Symbols", "Alphabets & Numbers", "Alphabets Excluding",
                "Numbers only", "Numbers & Symbols", "Numbers Excluding",
                "Symbols only", "Symbols Excluding",
                "Custom"
            ),
            self.renameBy_comboBox:     (
                "BULK", "TIMESTAMP", "NUMBERING", "CUSTOM"
            ),
            self.renameBy2_comboBox:    (
                "PREFIX NUMBERS", "SUFFIX NUMBERS", "CUSTOM PREFIX", "CUSTOM SUFFIX"
            )
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
            self.rename_btn:           ("RENAME", "Rename All Selected Items"),
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
            QCoreApplication.translate("MainWindow", "RENAME", None)
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
                "MainWindow", "Enter values to look for seperated by comma", None
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
