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
        self.firstGrid = QGridLayout()
        self.secondGrid = QGridLayout()
        self.thirdGrid = QGridLayout()

        self.tableFrame = QFrame(self.widgets)
        self.contentFrame1 = QFrame(self.widgets)
        self.contentFrame2 = QFrame(self.widgets)
        self.contentFrame3 = QFrame(self.widgets)
        self.tableWidget = QTableWidget(self.tableFrame)

        self.pageTitleLabel = QLabel(self.contentFrame1)
        self.lookupByTitleLabel = QLabel(self.contentFrame2)
        self.renameToTitleLabel = QLabel(self.contentFrame3)

        self.pathLineEdit = QLineEdit(self.contentFrame1)
        self.lookupByLineEdit = QLineEdit(self.contentFrame2)
        self.renameToLineEdit = QLineEdit(self.contentFrame3)

        self.horizontalBoxLayout = QHBoxLayout(self.tableFrame)
        self.horizontalBoxLayout2 = QHBoxLayout(self.contentFrame1)
        self.horizontalBoxLayout3 = QHBoxLayout(self.contentFrame2)
        self.horizontalBoxLayout4 = QHBoxLayout(self.contentFrame3)

        self.isRecursiveCheckBox = QCheckBox(self.contentFrame2)

        self.lookupByComboBox = QComboBox(self.contentFrame1)
        self.lookupByComboBox2 = QComboBox(self.contentFrame2)
        self.lookupByComboBox3 = QComboBox(self.contentFrame2)
        self.lookupByComboBox4 = QComboBox(self.contentFrame2)

        self.renameToComboBox = QComboBox(self.contentFrame3)
        self.renameToComboBox2 = QComboBox(self.contentFrame3)

        self.optionBtns_layout = QVBoxLayout()
        self.verticalBoxLayout = QVBoxLayout(self.widgets)

        self.browsePathBtn = QPushButton(self.contentFrame1)
        self.startLookupBtn = QPushButton(self.contentFrame2)
        self.renameBtn = QPushButton(self.tableFrame)
        self.exportBtn = QPushButton(self.tableFrame)
        self.importBtn = QPushButton(self.tableFrame)
        self.restoreBtn = QPushButton(self.tableFrame)

        self.verticalBoxLayout.setSpacing(10)
        self.verticalBoxLayout.setContentsMargins(10, 10, 10, 10)
        self.contentFrame1.setFrameShape(QFrame.NoFrame)
        self.contentFrame1.setFrameShadow(QFrame.Raised)
        self.horizontalBoxLayout2.setContentsMargins(-1, 5, -1, 5)
        self.lookupByComboBox.setAutoFillBackground(False)

        self.set_controller_widgets(
            self.lookupByComboBox,
            self.pathLineEdit,
            self.lookupByComboBox2,
            self.lookupByLineEdit,
            self.isRecursiveCheckBox,
            self.startLookupBtn
        )

        self.rename_options_menu = {

            "BULK":         ("PREFIX NUMBERS", "SUFFIX NUMBERS"),
            "TIMESTAMP":    ("mm_dd_yy_hh_msms", "mm_dd_hh_mm_msms", "hh_mm_ss_msms"),
            "CUSTOM":       (),

        }

        self.options = {
            self.lookupByComboBox:   (
                "FILES", "FOLDERS"
            ),
            self.lookupByComboBox2: (
                "NAME", "EXTENSION"
            ),
            self.lookupByComboBox3: (
                "CONTAIN", "EQUAL TO"
            ),
            self.lookupByComboBox4: (
                "Alphabets only", "Alphabets & Symbols", "Alphabets & Numbers",
                "Alphabets Excluding", "Numbers only", "Numbers & Symbols",
                "Numbers Excluding", "Symbols only", "Symbols Excluding", "Custom"
            ),
            self.renameToComboBox:     self.rename_options_menu.keys(),
            self.renameToComboBox2:    self.rename_options_menu.get("BULK")
        }

        """
        ===================================================================
                            SET STYLESHEET
        ===================================================================
        """
        self.startLookupBtn.setStyleSheet(
            self.html.get_bg_color("light blue")
        )

        self.renameToComboBox.setStyleSheet(
            self.html.get_bg_color("dark blue")
        )

        self.renameToComboBox2.setStyleSheet(
            self.html.get_bg_color("dark blue")
        )

        self.lookupByComboBox.setStyleSheet(
            self.html.get_bg_color("dark blue")
        )

        self.pathLineEdit.setStyleSheet(
            self.html.get_bg_color("dark blue")
        )

        self.lookupByLineEdit.setStyleSheet(
            self.html.get_bg_color("dark blue")
        )

        self.renameToLineEdit.setStyleSheet(
            self.html.get_bg_color("dark blue")
        )

        self.lookupByComboBox2.setStyleSheet(
            self.html.get_bg_color("dark blue")
        )

        self.lookupByComboBox3.setStyleSheet(
            self.html.get_bg_color("dark blue")
        )

        self.lookupByComboBox4.setStyleSheet(
            self.html.get_bg_color("dark blue")
        )

        self.browsePathBtn.setStyleSheet(
            self.html.get_bg_color("light blue")
        )

        self.lookupByTitleLabel.setStyleSheet(
            self.html.get_text_color("dracula purple")
        )

        self.renameToTitleLabel.setStyleSheet(
            self.html.get_text_color("dracula purple")
        )

        self.horizontalBoxLayout2.addLayout(self.firstGrid)

        """
        ===================================================================
                                SET FRAMINGS
        ===================================================================
        """
        self.tableFrame.setMinimumSize(QSize(0, 150))
        self.renameBtn.setMinimumSize(QSize(150, 30))
        self.exportBtn.setMinimumSize(QSize(150, 30))
        self.importBtn.setMinimumSize(QSize(150, 30))
        self.restoreBtn.setMinimumSize(QSize(150, 30))
        self.startLookupBtn.setMinimumSize(QSize(150, 30))
        self.lookupByLineEdit.setMinimumSize(QSize(0, 30))
        self.pathLineEdit.setMinimumSize(QSize(0, 30))
        self.renameToLineEdit.setMinimumSize(QSize(0, 30))
        self.browsePathBtn.setMinimumSize(QSize(150, 30))

        self.contentFrame2.setFrameShape(QFrame.NoFrame)
        self.contentFrame2.setFrameShadow(QFrame.Raised)

        self.horizontalBoxLayout3.setContentsMargins(-1, 5, -1, 5)
        self.secondGrid.setContentsMargins(-1, -1, -1, 0)
        self.lookupByLineEdit.setMaxLength(100)

        # self.tableFrame.setFrameShape(QFrame.StyledPanel)
        # self.tableWidget.setFrameShape(QFrame.NoFrame)
        # self.contentFrame3.setFrameShape(QFrame.NoFrame)
        # self.contentFrame3.setFrameShadow(QFrame.Raised)

        self.horizontalBoxLayout3.addLayout(self.secondGrid)

        self.thirdGrid.setContentsMargins(-1, -1, -1, 0)
        self.renameToLineEdit.setMaxLength(50)

        self.horizontalBoxLayout4.addLayout(self.thirdGrid)

        self.tableFrame.setFrameShadow(QFrame.Raised)
        self.horizontalBoxLayout.setSpacing(0)
        self.horizontalBoxLayout.setContentsMargins(0, 0, 0, 0)

        self.firstGrid.addWidget(self.lookupByComboBox, 1, 0, 1, 1)
        self.firstGrid.addWidget(self.pageTitleLabel, 0, 0, 1, 1)
        self.firstGrid.addWidget(self.pathLineEdit, 1, 1, 1, 1)
        self.firstGrid.addWidget(self.browsePathBtn, 1, 2, 1, 1)

        self.secondGrid.addWidget(self.lookupByLineEdit, 1, 3, 1, 1)
        self.secondGrid.addWidget(self.lookupByComboBox2, 1, 0, 1, 1)
        self.secondGrid.addWidget(self.lookupByTitleLabel, 0, 0, 1, 1)
        self.secondGrid.addWidget(self.lookupByComboBox3, 1, 1, 1, 1)
        self.secondGrid.addWidget(self.lookupByComboBox4, 1, 2, 1, 1)

        self.thirdGrid.addWidget(self.renameToTitleLabel, 0, 0, 1, 1)
        self.thirdGrid.addWidget(self.startLookupBtn, 1, 3, 1, 1)
        self.thirdGrid.addWidget(self.renameToLineEdit, 1, 1, 1, 1)
        self.thirdGrid.addWidget(self.renameToComboBox, 1, 0, 1, 1)
        self.thirdGrid.addWidget(self.renameToComboBox2, 1, 2, 1, 1)
        self.thirdGrid.addWidget(self.isRecursiveCheckBox, 2, 0, 1, 1)

        self.verticalBoxLayout.addWidget(self.contentFrame1)
        self.verticalBoxLayout.addWidget(self.contentFrame2)
        self.verticalBoxLayout.addWidget(self.contentFrame3)
        self.verticalBoxLayout.addWidget(self.tableFrame)

        self.optionBtns_layout.addWidget(self.renameBtn)
        self.optionBtns_layout.addWidget(self.restoreBtn)
        self.optionBtns_layout.addWidget(self.exportBtn)
        self.optionBtns_layout.addWidget(self.importBtn)

        self.horizontalBoxLayout.addWidget(self.tableWidget)
        self.horizontalBoxLayout.addLayout(self.optionBtns_layout)

        """
        ===================================================================
                                TABLE CONTENT
        ===================================================================
        """

        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            self.tableWidget.sizePolicy().hasHeightForWidth()
        )
        self.tableWidget.setSizePolicy(sizePolicy3)

        self.init_table(self.tableWidget)

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

        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(
            QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.startLookupBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.browsePathBtn.setCursor(QCursor(Qt.PointingHandCursor))

        # BUTTONS DESIGN
        btns = {
            "rename_btn":           self.renameBtn,
            "export_btn":           self.exportBtn,
            "import_btn":           self.importBtn,
            "restore_btn":          self.restoreBtn,
        }

        for btn_name, btn in btns.items():
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
            self.browsePathBtn, "folder_outline", size
        )
        self.set_icon(
            self.startLookupBtn, "start", size
        )
        self.set_icon(
            self.renameBtn, "delete sign", size
        )
        self.set_icon(
            self.restoreBtn, "restore file", size
        )
        self.set_icon(
            self.importBtn, "file upload", size
        )
        self.set_icon(
            self.exportBtn, "file download", size
        )

        """
        ===================================================================
                        BUTTONS & EVENT/SIGNAL
        ===================================================================
        """

        # MANUALY ENTERED PATH
        self.pathLineEdit.textChanged.connect(
            lambda: self.set_user_path(
                self.pathLineEdit.text(),
                True
            )
        )
        self.browsePathBtn.clicked.connect(
            lambda: self.set_user_path(
                self.get_path(),
                False
            )
        )
        self.startLookupBtn.clicked.connect(
            lambda: self.start_lookup_clicked()
        )
        self.renameBtn.clicked.connect(
            lambda: self.rename_content_clicked()
        )
        self.exportBtn.clicked.connect(
            lambda: self.export_process_clicked()
        )
        self.importBtn.clicked.connect(
            lambda: self.import_process_clicked()
        )
        self.restoreBtn.clicked.connect(
            lambda: self.restore_content_clicked()
        )
        self.lookupByComboBox.currentTextChanged.connect(
            lambda: self.change_lookup_format()
        )
        self.lookupByComboBox3.currentTextChanged.connect(
            lambda: self.lookup_input_2_changed()
        )
        self.lookupByComboBox4.currentTextChanged.connect(
            lambda: self.lookup_input_3_changed()
        )
        self.renameToComboBox.currentTextChanged.connect(
            lambda: self.rename_method_changed()
        )

        # ON TABLE-HEADER CLICK
        self.tableWidget.horizontalHeader().sectionClicked.connect(
            self.table_header_clicked
        )

        return self.widgets

    def lookup_input_2_changed(self):

        if self.lookupByComboBox3.currentText() != "CONTAIN":
            self.lookupByLineEdit.show()
            self.lookupByComboBox4.hide()
            return

        self.lookupByLineEdit.hide()
        self.lookupByComboBox4.show()

    def lookup_input_3_changed(self):

        # IF THE SELECTED OPTION DOESNT CONTAIN CUSTOM INPUT, HIDE INPUT
        if self.lookupByComboBox4.currentText().lower().split(" ")[-1] not in ("custom", "excluding"):
            self.lookupByLineEdit.hide()
            return

        self.lookupByLineEdit.show()

    def rename_method_changed(self):

        # SHOW THE RENAME TO COMBO BOXES BASED ON THE OPTION OF THE FIRST COMBO BOX
        match self.renameToComboBox.currentText().lower():

            case "timestamp":
                self.renameToLineEdit.hide()
                self.renameToComboBox2.show()

            case "custom":
                self.renameToLineEdit.show()
                self.renameToComboBox2.hide()

            case "bulk":
                self.renameToLineEdit.show()
                self.renameToComboBox2.show()

        self.renameToComboBox2.clear()
        self.renameToComboBox2.addItems(
            self.rename_options_menu.get(
                self.renameToComboBox.currentText()
            )
        )

    def retranslateUi(self):
        """
        TRANSLATE UI TEXT
        """

        """
        ===================================================================
                        COMBOBOXES ITEMS
        ===================================================================
        """

        for widget, info in self.options.items():
            widget.addItems([
                QCoreApplication.translate("MainWindow", text, None) for text in info
            ])

        """
        ===================================================================
                        SET TEXT / TOOL TIPS
        ===================================================================
        """

        data = {
            self.renameBtn:           ("RENAME", "Rename All Selected Items"),
            self.restoreBtn:          ("RESTORE", "Restore Last Deleted Process"),
            self.exportBtn:           ("EXPORT", "Store Current Lookup"),
            self.importBtn:           ("IMPORT", "Load Previous Lookup"),
            self.startLookupBtn:      ("START", "Start Lookup Process"),
            self.isRecursiveCheckBox: ("RECURSIVE", "Find Files Recursively Through The Selected Path"),
        }

        for widget, info in data.items():
            widget.setText(
                QCoreApplication.translate("MainWindow", info[0], None)
            )
            widget.setToolTip(
                QCoreApplication.translate("MainWindow", info[1], None)
            )

        self.pageTitleLabel.setText(
            QCoreApplication.translate("MainWindow", "RENAME", None)
        )

        self.pathLineEdit.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "Enter the path where should the lookup process begin",
                None,
            )
        )
        self.pathLineEdit.setPlaceholderText(
            QCoreApplication.translate(
                "MainWindow", "Enter the path here", None
            )
        )
        self.browsePathBtn.setText(
            QCoreApplication.translate(
                "MainWindow", "OPEN", None
            )
        )
        self.lookupByLineEdit.setPlaceholderText(
            QCoreApplication.translate(
                "MainWindow", "Enter values to look for [seperated by comma]...", None
            )
        )
        self.renameToLineEdit.setPlaceholderText(
            QCoreApplication.translate(
                "MainWindow", "Enter the value here...", None
            )
        )
        self.lookupByTitleLabel.setText(
            QCoreApplication.translate(
                "MainWindow", "LOOKUP BY", None
            )
        )
        self.renameToTitleLabel.setText(
            QCoreApplication.translate(
                "MainWindow", "RENAME TO", None
            )
        )

        """
        ===================================================================
                            SET VISIBILITY
        ===================================================================
        """
        self.lookupByLineEdit.hide()

        self.tableWidget.setSortingEnabled(True)
        self.retranslateTableHeaders()

        # SET CACHED DATA
        self.import_cache()
