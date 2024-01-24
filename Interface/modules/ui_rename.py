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
from Interface.constants import Dialog, Path


class Ui(Common):

    def __init__(self) -> None:
        super().__init__()

        self.paths = Path()
        self.dialog = Dialog()
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
        self.searchTypeHiddenLabel.setHidden(True)

        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.mainFrame.setMinimumSize(QSize(0, 150))
        self.mainFrame.setFrameShape(QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.mainFrameVL.setContentsMargins(0, 0, 0, 0)

        tables["RENAME"].render(self.tableWidget)

        self.bottomHLayout.setContentsMargins(40, -1, 40, -1)
        self.mainFrameVL.addWidget(self.tableWidget)
        self.mainFrameVL.addLayout(self.bottomHLayout)
        self.totalRecordsHL.setSpacing(20)

        self.bottomGridLayout.addLayout(self.totalRecordsHL, 1, 0, 1, 1)

        self.importBtn.setMinimumSize(QSize(150, 30))
        self.importBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.importBtn.setIconSize(QSize(30, 30))

        self.bottomGridLayout.addWidget(self.importBtn, 2, 2, 1, 1)

        self.renameBtn.setMinimumSize(QSize(150, 30))
        self.renameBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.renameBtn.setIconSize(QSize(30, 30))

        self.bottomGridLayout.addWidget(self.renameBtn, 2, 0, 1, 1)

        self.exportBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.exportBtn.setIconSize(QSize(30, 30))

        self.bottomGridLayout.addWidget(self.exportBtn, 2, 1, 1, 1)

        self.gridLayout_2.addLayout(self.bottomGridLayout, 1, 0, 1, 1)

        self.topGridLayout.setContentsMargins(-1, -1, -1, 0)
        self.totalRecordsTextLabel = QLabel(self.groupBox)
        self.totalRecordsTextLabel.setTextFormat(Qt.AutoText)

        self.topGridLayout.addWidget(self.totalRecordsTextLabel, 0, 0, 1, 1)

        self.exportBtn.setMinimumSize(QSize(150, 30))
        self.renameValueLineEdit.setMinimumSize(QSize(0, 30))
        self.renameValueLineEdit.setMaxLength(50)

        self.renameByComboBox.setIconSize(QSize(16, 16))
        self.renameBy2ComboBox.setIconSize(QSize(16, 16))

        self.renameByComboBox.setAutoFillBackground(False)
        self.renameBy2ComboBox.setAutoFillBackground(False)

        self.renameByComboBox.setFrame(True)
        self.renameBy2ComboBox.setFrame(True)

        self.importBtn.setEnabled(False)
        self.renameBtn.setEnabled(False)
        self.exportBtn.setEnabled(False)

        self.topGridLayout.addWidget(self.renameValueLineEdit, 2, 3, 1, 1)
        self.topGridLayout.addWidget(self.renameByComboBox, 2, 0, 1, 1)
        self.topGridLayout.addWidget(self.renameBy2ComboBox, 2, 2, 1, 1)
        self.topGridLayout.addWidget(self.totalRecordsLabel, 0, 2, 1, 1)
        self.gridLayout_2.addLayout(self.topGridLayout, 0, 0, 1, 1)
        self.bottomHLayout.addWidget(self.groupBox)
        self.verticalLayout.addWidget(self.mainFrame)

        self.importBtn.setStyleSheet(
            self.html.get_bg_color("light blue"))
        self.renameBtn.setStyleSheet(
            self.html.get_bg_color("light blue"))
        self.exportBtn.setStyleSheet(
            self.html.get_bg_color("light blue"))
        self.renameByComboBox.setStyleSheet(
            self.html.get_bg_color("dark blue"))
        self.renameBy2ComboBox.setStyleSheet(
            self.html.get_bg_color("dark blue"))
        self.renameValueLineEdit.setStyleSheet(
            self.html.get_bg_color("dark blue"))

        renameByComboBox_options = (
            "BULK", "TIMESTAMP", "NUMBERING", "CUSTOM"
        )
        renameBy2ComboBox_options = (
            "PREFIX NUMBER", "SUFFIX NUMBER", "CUSTOM PREFI", "CUSTOM SUFFIX"
        )

        for opt in renameByComboBox_options:
            self.renameByComboBox.addItem(opt)

        for opt in renameBy2ComboBox_options:
            self.renameBy2ComboBox.addItem(opt)

        self.totalRecordsLabel.setObjectName("totalRecordsLabel")
        self.searchTypeHiddenLabel.setObjectName("searchTypeHiddenLabel")
        
        self.retranslateUi()

        return self.widgets

    def retranslateUi(self):

        self.groupBox.setTitle(QCoreApplication.translate(
            "MainWindow", u"RENAME", None))
        self.importBtn.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Restore last deleted process", None))
        self.importBtn.setText(QCoreApplication.translate(
            "MainWindow", u"IMPORT", None))
        self.renameBtn.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Load previous lookup", None))
        self.renameBtn.setText(QCoreApplication.translate(
            "MainWindow", u"RENAME", None))
        self.exportBtn.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Restore last deleted process", None))
        self.exportBtn.setText(QCoreApplication.translate(
            "MainWindow", u"EXPORT", None))
        self.totalRecordsTextLabel.setText(
            QCoreApplication.translate("MainWindow", u"TOTAL RECORDS: ", None))
        self.renameValueLineEdit.setText("")
        self.renameValueLineEdit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Enter the value", None))
        self.renameByComboBox.setItemText(
            0, QCoreApplication.translate("MainWindow", u"BULK", None))
        self.renameByComboBox.setItemText(
            1, QCoreApplication.translate("MainWindow", u"TIMESTAMP", None))
        self.renameByComboBox.setItemText(
            2, QCoreApplication.translate("MainWindow", u"NUMBERING", None))
        self.renameByComboBox.setItemText(
            3, QCoreApplication.translate("MainWindow", u"CUSTOM", None))

        self.renameBy2ComboBox.setItemText(
            0, QCoreApplication.translate("MainWindow", u"PREFIX NUMBERS", None))
        self.renameBy2ComboBox.setItemText(
            1, QCoreApplication.translate("MainWindow", u"SUFFIX NUMBERS", None))
        self.renameBy2ComboBox.setItemText(
            2, QCoreApplication.translate("MainWindow", u"CUSTOM PREFIX ", None))
        self.renameBy2ComboBox.setItemText(
            3, QCoreApplication.translate("MainWindow", u"CUSTOM SUFFIX", None))

        self.totalRecordsLabel.setText(
            QCoreApplication.translate("MainWindow", u"0", None))
