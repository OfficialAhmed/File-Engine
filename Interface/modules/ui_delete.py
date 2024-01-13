from PySide6.QtCore import QCoreApplication, QSize, Qt
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import (
    QFrame, QGroupBox,
    QGridLayout, QHBoxLayout, QLabel, QPushButton,
    QTableWidget, QVBoxLayout, QWidget
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

    def restore_content_clicked(self) -> None:

        # PROMPT USER
        if not self.dialog.show(
            "ARE YOU SURE YOU WANT TO *RESTORE* PREVIOUSLY REMOVED ITEMS?",
            "ARE YOU SURE?"
        ):
            return None

        try:

            trash_file = self.paths.TRASH_CONTENT_FILE

            # FILE MUST EXIST AND NOT EMPTY, ELSE TERMINATE PROCESS
            if not os.path.exists(trash_file) or not os.path.getsize(trash_file) > 0:

                self.dialog.show(
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
                self.restore_process_state
            )

            # UNSUCCESSFULL ITEMS REMOVAL MESSAGE
            future_process.is_fail.connect(
                lambda error: self.dialog.show(
                    f"SOMTHING WENT WRONG WHILE RESTORING | ERROR <{error}>",
                    "C",
                    False
                )
            )

            future_process.run()

            # REFORMAT RESTORED DATA FOR THE TABLE
            table_data = {}
            for item in data.values():
                file_size = "-"
                last_slash = item.rfind("/")
                file_name = item[last_slash + 1:]
                file_path = item[: last_slash]

                table_data[file_name] = {
                    "deleted": file_name,
                    "root": file_path,
                    "size": file_size
                }

            tables["DELETE"].fill(table_data)
            self.totalRecordsLabel.setText(str(len(table_data)))

        except Exception as e:

            self.dialog.show(
                f"CANNOT READ RESTORE FILE. ERROR| {e}",
                "C",
                is_dialog=False
            )
            return None

    def delete_content_clicked(self):

        # IF USER DID NOT ACCEPT DELETE PROCESS, TERMINATE
        if not self.dialog.show(
            "ARE YOU SURE YOU WANT TO *REMOVE* THE SELECTED FILES?",
            "ARE YOU SURE?"
        ):
            return

        # RESET PROGRESS BAR
        self.progressBar.update(0)

        files_to_remove = []

        # FLAG SELECTED TABLE ITEMS
        for indx, cb in enumerate(tables["DELETE"].checkboxes):

            # IF CHECKBOX SELECTED
            if cb.isChecked():

                # FETCH DATA FROM TABLE
                file = self.tableWidget.item(
                    indx, 0                                 # EACH ROW, 1ST COLUMN
                ).text()

                root = self.tableWidget.item(
                    indx, 1                                 # EACH ROW, 2ND COLUMN
                ).text()

                files_to_remove.append(f"{root}//{file}")
                self.rows_to_remove.append(indx)

        if not files_to_remove:
            self.dialog.show(
                "PLEASE SELECT AT LEAST ONE FILE",
                "NO SELECTION!",
                False
            )
            return

        # DELETE FILES WITH THREADS
        worker = DeleteWorker(
            files_to_remove,
            self.searchTypeHiddenLabel.text()
        )

        # UPDATE PROGRESS BAR
        worker.progress_signal.connect(
            self.progressBar.update
        )

        # DELETE ROWS FROM THE TABLE
        worker.remove_rows_signal.connect(
            tables["DELETE"].remove_rows(
                self.rows_to_remove,
                self.totalRecordsLabel
            )
        )
        self.rows_to_remove.clear()

        # SUCCESSFULL ITEMS REMOVAL MESSAGE
        worker.is_success.connect(
            self.removing_process_state
        )

        # UNSUCCESSFULL ITEMS REMOVAL MESSAGE
        worker.is_fail.connect(
            lambda error: self.dialog.show(
                f"SOMTHING WENT WRONG WHILE REMOVING | ERROR <{error}>",
                "C",    # CRITICAL MESSAGE
                False
            )
        )

        worker.run()

    def removing_process_state(self, state: bool):

        if state:
            self.dialog.show(
                f"SUCCESSFULY REMOVED ALL ITEM(S)",
                "OPERATION SUCCESSFULL",
                False
            )

        else:
            self.dialog.show(
                f"SOME ITEM(S) WEREN'T REMOVED SUCCESSFULY",
                "OPERATION PARTIALLY SUCCESSFULL",
                False
            )

    def restore_process_state(self, state: bool):

        if state:
            self.dialog.show(
                f"SUCCESSFULY RESTORED ALL ITEM(S)",
                "OPERATION SUCCESSFULL",
                False
            )

        else:
            self.dialog.show(
                f"SOME ITEM(S) WEREN'T RESTORED SUCCESSFULY",
                "OPERATION PARTIALLY SUCCESSFULL",
                False
            )

    def render_page(self):
        """
        ===================================================================
                        SET WIDGETS (SENSITIVE LAYOUT)
        ===================================================================
        """

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

        tables["DELETE"].render(self.tableWidget)

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

        self.set_icon(
            self.deleteBtn, "delete sign", size
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

        self.deleteBtn.clicked.connect(
            lambda: self.delete_content_clicked()
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
        tables["DELETE"].retranslate_headers()

        self.groupBox.setTitle(
            QCoreApplication.translate("MainWindow", u"DELETE", None)
        )
        self.totalRecordsTxtLabel.setText(
            QCoreApplication.translate("MainWindow", "TOTAL RECORDS: ", None))
        self.totalRecordsLabel.setText(
            QCoreApplication.translate("MainWindow", "0", None))
