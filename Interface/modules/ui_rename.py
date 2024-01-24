from PySide6.QtCore import QCoreApplication, QSize, Qt
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import (
    QFrame, QGroupBox,
    QGridLayout, QHBoxLayout, QLabel, QPushButton,
    QTableWidget, QVBoxLayout, QWidget, QLineEdit, QComboBox
)

import os
import json
from Interface.environment import Common, RestoreWorker, DeleteWorker, tables
# from Interface.constants import Dialog, Path


class Option:

    def __init__(self, cb: QComboBox, cb2: QComboBox, custom_input: QLineEdit) -> None:

        self.cb:            QComboBox = cb
        self.cb2:           QComboBox = cb2
        self.custom_input:  QLineEdit = custom_input

        self.options = {
            "BULK": (
                "START FROM 0",
                "START FROM 1",
                "START FROM CUSTOM",
                "# AS PREFIX & START FROM 1",
                "# AS SUFFIX & START FROM 1",
                "# AS PREFIX & START FROM CUSTOM",
                "# AS SUFFIX & START FROM CUSTOM"
            ),

            "TIMESTAMP": (
                "DD_MM_YY-seed",
                "DD_MM_YY_hh-seed",
                "DD_MM_YY_hh_mm-seed",
                "DD_MM_YY_hh_mm_ssss-seed",
                "hh_mm_ssss-seed",
            ),
        }

    def generate_default_options(self):
        """ GENERATE RENAMING OPTIONS FOR BOTH COMBOBOXES """

        for option in self.options.keys():
            self.cb.addItem(option)

        self.generate_cb2_options()

    def generate_cb2_options(self):
        """ GENERATE RENAMING OPTIONS FOR 2ND COMBOBOX """

        self.cb2.clear()
        for option in self.options.get(self.cb.currentText()):
            self.cb2.addItem(option)


class Ui(Common):

    def __init__(self) -> None:
        super().__init__()

        self.rows_to_remove = []

    def render_page(self):

        self.widgets = QWidget()
        self.bottomHLayout = QHBoxLayout()
        self.topGridLayout = QGridLayout()
        self.totalRecordsHL = QHBoxLayout()
        self.bottomGridLayout = QGridLayout()

        self.mainFrame = QFrame(self.widgets)
        self.verticalLayout = QVBoxLayout(self.widgets)

        self.mainFrameVL = QVBoxLayout(self.mainFrame)
        self.tableWidget = QTableWidget(self.mainFrame)
        self.groupBox = QGroupBox(self.mainFrame)
        self.importBtn = QPushButton(self.groupBox)
        self.renameBtn = QPushButton(self.groupBox)
        self.exportBtn = QPushButton(self.groupBox)
        self.totalRecordsLabel = QLabel(self.groupBox)
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.renameValueLineEdit = QLineEdit(self.groupBox)
        self.renameByComboBox = QComboBox(self.groupBox)
        self.renameBy2ComboBox = QComboBox(self.groupBox)
        self.searchTypeHiddenLabel = QLabel(self.groupBox)
        self.totalRecordsTextLabel = QLabel(self.groupBox)

        tables["RENAME"].render(self.tableWidget)
        self.rename_options = Option(
            self.renameByComboBox, self.renameBy2ComboBox, self.renameValueLineEdit
        )

        self.searchTypeHiddenLabel.setHidden(True)

        self.mainFrameVL.setContentsMargins(0, 0, 0, 0)
        self.topGridLayout.setContentsMargins(-1, 10, -1, 0)
        self.bottomHLayout.setContentsMargins(40, -1, 40, -1)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)

        self.mainFrame.setFrameShape(QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Raised)

        self.importBtn.setIconSize(QSize(30, 30))
        self.renameBtn.setIconSize(QSize(30, 30))
        self.exportBtn.setIconSize(QSize(30, 30))
        self.renameByComboBox.setIconSize(QSize(16, 16))
        self.renameBy2ComboBox.setIconSize(QSize(16, 16))

        self.importBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.renameBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.exportBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.exportBtn.setMinimumSize(QSize(150, 30))
        self.mainFrame.setMinimumSize(QSize(0, 150))
        self.importBtn.setMinimumSize(QSize(150, 30))
        self.renameBtn.setMinimumSize(QSize(150, 30))
        self.renameValueLineEdit.setMinimumSize(QSize(0, 30))
        self.renameValueLineEdit.setMaxLength(30)

        self.mainFrameVL.addWidget(self.tableWidget)
        self.bottomHLayout.addWidget(self.groupBox)
        self.verticalLayout.addWidget(self.mainFrame)
        self.bottomGridLayout.addWidget(self.renameBtn, 2, 0, 1, 1)
        self.bottomGridLayout.addWidget(self.importBtn, 2, 2, 1, 1)
        self.bottomGridLayout.addWidget(self.exportBtn, 2, 1, 1, 1)
        self.topGridLayout.addWidget(self.renameByComboBox, 2, 0, 1, 1)
        self.topGridLayout.addWidget(self.renameBy2ComboBox, 2, 2, 1, 1)
        self.topGridLayout.addWidget(self.totalRecordsLabel, 0, 2, 1, 1)
        self.topGridLayout.addWidget(self.renameValueLineEdit, 2, 3, 1, 1)
        self.topGridLayout.addWidget(self.totalRecordsTextLabel, 0, 0, 1, 1)

        self.mainFrameVL.addLayout(self.bottomHLayout)
        self.gridLayout_2.addLayout(self.topGridLayout, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.bottomGridLayout, 1, 0, 1, 1)
        self.bottomGridLayout.addLayout(self.totalRecordsHL, 1, 0, 1, 1)

        self.totalRecordsTextLabel.setTextFormat(Qt.AutoText)

        # fmt: off
        self.importBtn.setStyleSheet(self.html.get_bg_color("light blue"))
        self.renameBtn.setStyleSheet(self.html.get_bg_color("light blue"))
        self.exportBtn.setStyleSheet(self.html.get_bg_color("light blue"))
        self.renameByComboBox.setStyleSheet(self.html.get_bg_color("dark blue"))
        self.renameBy2ComboBox.setStyleSheet(self.html.get_bg_color("dark blue"))
        self.renameValueLineEdit.setStyleSheet(self.html.get_bg_color("dark blue"))

        self.totalRecordsLabel.setObjectName("totalRecordsLabel")
        self.searchTypeHiddenLabel.setObjectName("searchTypeHiddenLabel")

        self.rename_options.generate_default_options()
        self.renameByComboBox.currentIndexChanged.connect(
            lambda: self.rename_options.generate_cb2_options()
        )

        self.retranslateUi()
        return self.widgets

    def retranslateUi(self):

        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"RENAME", None))
        self.importBtn.setText(QCoreApplication.translate("MainWindow", u"IMPORT", None))
        self.renameBtn.setText(QCoreApplication.translate("MainWindow", u"RENAME", None))
        self.exportBtn.setText(QCoreApplication.translate("MainWindow", u"EXPORT", None))
        self.totalRecordsLabel.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.totalRecordsTextLabel.setText(QCoreApplication.translate("MainWindow", u"TOTAL RECORDS: ", None))

        self.exportBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Save current lookup", None))
        self.importBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Load previous lookup", None))
        self.renameBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Rename selected files", None))
        self.renameValueLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter the value", None))

