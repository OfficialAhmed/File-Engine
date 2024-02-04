from PySide6.QtCore import QCoreApplication, QSize, Qt
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import (
    QFrame, QGroupBox,
    QGridLayout, QHBoxLayout, QLabel, QPushButton,
    QTableWidget, QVBoxLayout, QWidget
)


from frontend.environment import tables
from backend.delete import Response


class Ui(Response):

    def __init__(self) -> None:

        self.table = tables["DELETE"]

        self.widgets = QWidget()
        self.gridLayout = QGridLayout()
        self.bottomHLayout = QHBoxLayout()
        self.totalRecordsHL = QHBoxLayout()

        self.mainFrame = QFrame(self.widgets)
        self.groupBox = QGroupBox(self.mainFrame)
        self.deleteBtn = QPushButton(self.groupBox)
        self.exportBtn = QPushButton(self.groupBox)
        self.importBtn = QPushButton(self.groupBox)
        self.restoreBtn = QPushButton(self.groupBox)
        self.gridLayoutGL = QGridLayout(self.groupBox)
        self.totalRecordsLabel = QLabel(self.groupBox)
        self.mainFrameVL = QVBoxLayout(self.mainFrame)
        self.tableWidget = QTableWidget(self.mainFrame)
        self.verticalLayout = QVBoxLayout(self.widgets)
        self.totalRecordsTxtLabel = QLabel(self.groupBox)

        self.searchTypeHiddenLabel = QLabel(self.groupBox)
        self.table.set_total_records_widget(self.totalRecordsLabel)

        super().__init__(
            self.totalRecordsLabel,
            self.tableWidget,
            self.searchTypeHiddenLabel
        )

        self.searchTypeHiddenLabel.setHidden(True)

        self.mainFrameVL.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setContentsMargins(0, 15, 0, 0)
        self.bottomHLayout.setContentsMargins(40, -1, 40, -1)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)

        self.deleteBtn.setIconSize(QSize(30, 30))
        self.exportBtn.setIconSize(QSize(30, 30))
        self.importBtn.setIconSize(QSize(30, 30))
        self.restoreBtn.setIconSize(QSize(30, 30))

        self.deleteBtn.setMinimumSize(QSize(150, 30))
        self.exportBtn.setMinimumSize(QSize(150, 30))
        self.importBtn.setMinimumSize(QSize(150, 30))
        self.restoreBtn.setMinimumSize(QSize(150, 30))

        self.deleteBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.exportBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.importBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.restoreBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.setSpacing(10)
        self.totalRecordsHL.setSpacing(20)
        self.totalRecordsTxtLabel.setTextFormat(Qt.AutoText)

        """
        ===================================================================
                                SET WIDGETS LAYOUT
        ===================================================================
        """
        self.gridLayout.addWidget(self.deleteBtn, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.exportBtn, 2, 2, 1, 1)
        self.gridLayout.addWidget(self.importBtn, 2, 3, 1, 1)
        self.gridLayout.addWidget(self.restoreBtn, 2, 1, 1, 1)
        self.bottomHLayout.addWidget(self.groupBox)
        self.verticalLayout.addWidget(self.mainFrame)
        self.totalRecordsHL.addWidget(self.totalRecordsTxtLabel)
        self.totalRecordsHL.addWidget(self.totalRecordsLabel)

        self.mainFrameVL.addWidget(self.tableWidget)
        self.mainFrameVL.addLayout(self.bottomHLayout)
        self.gridLayout.addLayout(self.totalRecordsHL, 1, 0, 1, 1)
        self.gridLayoutGL.addLayout(self.gridLayout, 0, 0, 1, 1)

        """
        ===================================================================
                                TABLE CONTENT
        ===================================================================
        """

        self.table.render(self.tableWidget)

        """
        ===================================================================
                           SET OBJECT NAMES
        ===================================================================
        """
        self.widgets.setObjectName("widgets")
        self.groupBox.setObjectName(u"groupBox")
        self.importBtn.setObjectName(u"importBtn")
        self.exportBtn.setObjectName(u"exportBtn")
        self.deleteBtn.setObjectName(u"deleteBtn")
        self.mainFrame.setObjectName(u"mainFrame")
        self.restoreBtn.setObjectName(u"restoreBtn")
        self.gridLayout.setObjectName(u"gridLayout")
        self.tableWidget.setObjectName(u"tableWidget")
        self.mainFrameVL.setObjectName(u"mainFrameVL")
        self.gridLayoutGL.setObjectName(u"gridLayoutGL")
        self.bottomHLayout.setObjectName(u"bottomHLayout")
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.totalRecordsHL.setObjectName(u"totalRecordsHL")
        self.totalRecordsLabel.setObjectName(u"totalRecordsLabel")
        self.totalRecordsTxtLabel.setObjectName(u"totalRecordsTxtLabel")
        self.searchTypeHiddenLabel.setObjectName(u"searchTypeHiddenLabel")

        # BUTTONS DESIGN
        btns = {
            "deleteBtn":    self.deleteBtn,
            "restoreBtn":   self.restoreBtn,
            "exportBtn":    self.exportBtn,
            "importBtn":    self.importBtn
        }

        for btn_name, btn in btns.items():
            btn.setObjectName(btn_name)
            btn.setMinimumSize(QSize(150, 30))
            btn.setStyleSheet(self.html.get_bg_color("light blue"))
            btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.retranslateUi()

        """
        ===================================================================
                        RENDER PAGE ICONS
        ===================================================================
        """

        size = (20, 20)
        self.set_icon(self.deleteBtn, "delete sign", size)
        self.set_icon(self.importBtn, "file upload", size)
        self.set_icon(self.restoreBtn, "restore file", size)
        self.set_icon(self.exportBtn, "file download", size)

        """
        ===================================================================
                        BUTTONS & EVENT/SIGNAL
        ===================================================================
        """

        self.deleteBtn.clicked.connect(
            lambda: self.delete_content_clicked()
        )

        self.exportBtn.clicked.connect(
            lambda: self.table.export_process_clicked()
        )

        self.importBtn.clicked.connect(
            lambda: self.table.import_process_clicked()
        )

        self.restoreBtn.clicked.connect(
            lambda: self.restore_content_clicked()
        )

    def get_widgets(self):
        return self.widgets

    def retranslateUi(self):
        """
        TRANSLATE UI TEXT
        """

        """
        ===================================================================
                        SET TEXT / TOOL TIPS
        ===================================================================
        """

        data = {
            self.deleteBtn:           ("DELETE", "Delete All Selected Items"),
            self.restoreBtn:          ("RESTORE", "Restore Last Deleted Process"),
            self.exportBtn:           ("EXPORT", "Store Current Lookup"),
            self.importBtn:           ("IMPORT", "Load Previous Lookup")
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

        """
        ////////////////////////////////////////////////
                TABLE CONTENT
        ////////////////////////////////////////////////
        """
        self.tableWidget.setSortingEnabled(True)
        self.table.retranslate_headers()

        self.groupBox.setTitle(
            QCoreApplication.translate("MainWindow", u"DELETE", None)
        )
        self.totalRecordsTxtLabel.setText(
            QCoreApplication.translate("MainWindow", "TOTAL RECORDS: ", None))
        self.totalRecordsLabel.setText(
            QCoreApplication.translate("MainWindow", "0", None))
