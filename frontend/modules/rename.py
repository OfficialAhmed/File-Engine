from PySide6.QtCore import QCoreApplication, QSize, Qt
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import (
    QFrame, QGroupBox,
    QGridLayout, QHBoxLayout, QLabel, QPushButton,
    QTableWidget, QVBoxLayout, QWidget, QLineEdit, QComboBox
)

from environment import tables
from backend.rename import Response, Option


class Ui(Response):

    def __init__(self) -> None:

        self.table = tables["RENAME"]

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
        self.totalRecordsTextLabel = QLabel(self.groupBox)
        self.searchTypeHiddenLabel = QLabel(self.groupBox)

        self.searchTypeHiddenLabel.setHidden(True)

        """
        ===================================================================
                        SET BACKEND SPECS
        ===================================================================
        """
        super().__init__(
            tableWidget=self.tableWidget,
            renameByComboBox=self.renameByComboBox,
            renameBy2ComboBox=self.renameBy2ComboBox,
            totalRecordsLabel=self.totalRecordsLabel,
            renameValueLineEdit=self.renameValueLineEdit
        )
        self.table.render(self.tableWidget)
        self.table.set_total_records_widget(self.totalRecordsLabel)
        self.rename_options = Option(
            self.renameByComboBox, self.renameBy2ComboBox, self.renameValueLineEdit
        )

        self.renameValueLineEdit.setEnabled(False)

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
        self.searchTypeHiddenLabel.setObjectName(u"searchTypeHiddenLabel")

        """
        ===================================================================
                        RENDER PAGE ICONS
        ===================================================================
        """
        size = (20, 20)
        self.set_icon(self.importBtn, "file upload", size)
        self.set_icon(self.exportBtn, "file download", size)

        """
        ===================================================================
                        BUTTONS & EVENT/SIGNAL
        ===================================================================
        """

        self.rename_options.generate_default_options()
        self.renameByComboBox.currentIndexChanged.connect(
            lambda: self.rename_options.generate_cb2_options()
        )
        self.renameBy2ComboBox.currentIndexChanged.connect(
            lambda: self.rename_options.toggle_custom_value()
        )
        self.renameBtn.clicked.connect(
            lambda: self.rename_content_clicked()
        )
        self.exportBtn.clicked.connect(
            lambda: self.table.export_process_clicked()
        )
        self.importBtn.clicked.connect(
            lambda: self.table.import_process_clicked()
        )

        self.retranslateUi()

    def get_widgets(self) -> QWidget:
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

