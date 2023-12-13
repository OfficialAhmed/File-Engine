from PySide6.QtCore import QCoreApplication, QSize, Qt
from PySide6.QtGui import QBrush, QColor, QCursor, QPalette
from PySide6.QtWidgets import (
    QAbstractItemView, QAbstractScrollArea, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QVBoxLayout, QWidget
)

import os
import json
from Interface.environment import Common, RestoreWorker


class Ui(Common):

    def __init__(self) -> None:
        super().__init__()

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
            worker = RestoreWorker(data)

            # UPDATE PROGRESS BAR WITH THE VALUE RETURNED BY THE SIGNAL
            worker.progress_signal.connect(
                self.progressBar.update
            )

            # SUCCESSFULL ITEMS REMOVAL MESSAGE
            worker.is_success.connect(
                self.renaming_process_state
            )

            # UNSUCCESSFULL ITEMS REMOVAL MESSAGE
            worker.is_fail.connect(
                lambda error: self.controller.show_dialog(
                    f"SOMTHING WENT WRONG WHILE RESTORING | ERROR <{error}>",
                    "C",
                    False
                )
            )

            worker.run()

        except Exception as e:

            self.controller.show_dialog(
                f"CANNOT READ RESTORE FILE. ERROR| {e}",
                "C",
                is_dialog=False
            )
            return None

    def renaming_process_state(self, state: bool):
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

        self.init_table(self.table_layout)

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

        self.set_icon(
            self.browseCurrentPath_btn, "folder_outline", size
        )
        self.set_icon(
            self.startLookup_btn, "start", size
        )
        self.set_icon(
            self.rename_btn, "delete sign", size
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
