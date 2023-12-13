from PySide6.QtCore import QCoreApplication, QSize, Qt
from PySide6.QtGui import QBrush, QColor, QCursor, QPalette
from PySide6.QtWidgets import (
    QAbstractItemView, QAbstractScrollArea, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QVBoxLayout, QWidget
)

import os
import json
from Interface.environment import Common, RestoreWorker, DeleteWorker


class Ui(Common):

    def __init__(self) -> None:
        super().__init__()
        self.rows_to_remove = []

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
        worker = DeleteWorker(
            files_to_remove,
            self.lookupType.currentText()
        )

        # UPDATE PROGRESS BAR
        worker.progress_signal.connect(
            self.progressBar.update
        )

        # DELETE ROWS FROM THE UI
        worker.remove_rows_signal.connect(
            self.remove_table_rows
        )

        # SUCCESSFULL ITEMS REMOVAL MESSAGE
        worker.is_success.connect(
            self.removing_process_state
        )

        # UNSUCCESSFULL ITEMS REMOVAL MESSAGE
        worker.is_fail.connect(
            lambda error: self.controller.show_dialog(
                f"SOMTHING WENT WRONG WHILE REMOVING | ERROR <{error}>",
                "C",    # CRITICAL MESSAGE
                False
            )
        )

        worker.run()

    def restore_content_clicked(self) -> None:

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

    def removing_process_state(self, state: bool):

        if state:
            self.controller.show_dialog(
                f"SUCCESSFULY REMOVED ALL ITEM(S)",
                "OPERATION SUCCESSFULL",
                False
            )

        else:
            self.controller.show_dialog(
                f"SOME ITEM(S) WEREN'T REMOVED SUCCESSFULY",
                "OPERATION PARTIALLY SUCCESSFULL",
                False
            )
            
    def restore_process_state(self, state: bool):

        if state:
            self.controller.show_dialog(
                f"SUCCESSFULY RESTORED ALL ITEM(S)",
                "OPERATION SUCCESSFULL",
                False
            )

        else:
            self.controller.show_dialog(
                f"SOME ITEM(S) WEREN'T RESTORED SUCCESSFULY",
                "OPERATION PARTIALLY SUCCESSFULL",
                False
            )

    def render_page(self):
        self.widgets = QWidget()

        """
        ===================================================================
                        SET WIDGETS (SENSITIVE LAYOUT)
        ===================================================================
        """
        self.first_layout = QGridLayout()
        self.second_layout = QGridLayout()

        self.main_frame_verticalLayout = QVBoxLayout(self.widgets)
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

        self.row_3 = QFrame(self.widgets)
        self.horizontalLayout_12 = QHBoxLayout(self.row_3)

        self.main_frame_verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.main_frame_verticalLayout.addWidget(self.frame_content_wid_3)
        self.first_layout.addWidget(self.PageTitle_label, 0, 0, 1, 1)
        self.first_layout.addWidget(self.LookupType_comboBox, 1, 0, 1, 1)
        self.first_layout.addWidget(self.currentPath_lineEdit, 1, 1, 1, 1)
        self.first_layout.addWidget(self.browseCurrentPath_btn, 1, 2, 1, 1)
        self.second_layout.addWidget(self.LookuByTitle_label, 0, 0, 1, 1)
        self.second_layout.addWidget(self.lookupInput_lineEdit, 1, 1, 1, 1)
        self.second_layout.addWidget(self.startLookup_btn, 1, 2, 1, 1)
        self.second_layout.addWidget(self.lookupFormat_comboBox, 1, 0, 1, 1)
        self.second_layout.addWidget(self.isRecursive_checkBox, 2, 0, 1, 1)

        self.LookuByTitle_label.setLineWidth(1)
        self.LookuByTitle_label.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter
        )

        self.LookupType_comboBox.setFrame(True)
        self.lookupFormat_comboBox.setFrame(True)

        self.isRecursive_checkBox.setChecked(True)

        self.startLookup_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.browseCurrentPath_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_10.addLayout(self.second_layout)
        self.main_frame_verticalLayout.addWidget(self.frame_content_wid_2)

        self.horizontalLayout_11.addLayout(self.first_layout)
        self.main_frame_verticalLayout.setSpacing(10)
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
        self.frame_content_wid_2.setFrameShadow(QFrame.Raised)
        self.frame_content_wid_3.setFrameShadow(QFrame.Raised)
        self.frame_content_wid_4.setFrameShadow(QFrame.Raised)

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
        self.second_layout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)

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

        self.init_table(self.table_layout)

        self.horizontalLayout_12.addWidget(self.table_layout)

        self.optionBtns_layout = QVBoxLayout()

        self.delete_btn = QPushButton(self.row_3)
        self.restore_btn = QPushButton(self.row_3)
        self.export_btn = QPushButton(self.row_3)
        self.import_btn = QPushButton(self.row_3)

        self.horizontalLayout_12.addLayout(self.optionBtns_layout)
        self.main_frame_verticalLayout.addWidget(self.row_3)

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
            self.html.get_bg_color("light blue")
        )
        self.lookupInput_lineEdit.setStyleSheet(
            self.html.get_bg_color("dark blue")
        )
        self.startLookup_btn.setStyleSheet(
            self.html.get_bg_color("light blue")
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
        self.row_3.setObjectName("row_3")
        self.widgets.setObjectName("widgets")
        self.table_layout.setObjectName("table_layout")
        self.first_layout.setObjectName("first_layout")
        self.second_layout.setObjectName("second_layout")
        self.main_frame_verticalLayout.setObjectName("verticalLayout")
        self.startLookup_btn.setObjectName("startLookup_btn")
        self.PageTitle_label.setObjectName("PageTitle_label")
        self.optionBtns_layout.setObjectName("optionBtns_layout")
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

        self.set_icon(
            self.browseCurrentPath_btn, "folder_outline", size
        )
        self.set_icon(
            self.startLookup_btn, "start", size
        )
        self.set_icon(
            self.delete_btn, "delete sign", size
        )
        self.set_icon(
            self.restore_btn, "restore file", size
        )
        self.set_icon(
            self.import_btn, "file upload", size
        )
        self.set_icon(
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
                self.get_path(),
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
            lambda: self.restore_content_clicked()
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
