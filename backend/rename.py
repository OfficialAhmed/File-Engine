
from frontend.environment import Common, RenameWorker, tables


class Response(Common):

    def __init__(self, renameBy2ComboBox, renameValueLineEdit, tableWidget, totalRecordsLabel) -> None:
        super().__init__()

        # WIDGETS REQUIRED FROM THE FRONT-END
        self.tableWidget = tableWidget
        self.totalRecordsLabel = totalRecordsLabel
        self.renameBy2ComboBox = renameBy2ComboBox
        self.renameValueLineEdit = renameValueLineEdit

        self.rows_to_remove = []

    def rename_content_clicked(self):

        # IF USER DID NOT ACCEPT DELETE PROCESS, TERMINATE
        if not self.dialog.show(
            "ARE YOU SURE YOU WANT TO *RENAME* SELECTED FILES? THIS IS IRREVERSIBALE",
            "ARE YOU SURE?"
        ):
            return

        # ALLOW ONLY INTEGERS FOR THE CUSTOM INPUT
        # IF THE OPTION DOESNT CONTAIN INT AND THE VALUE ISNT AN INT
        if not self.renameBy2ComboBox.currentText()[-1].isdigit() and not self.renameValueLineEdit.text().isdigit():
            self.dialog.show(
                f"Please enter a valid integer!",
                "W",   # CRITICAL MESSAGE
                False
            )
            return

        # RESET PROGRESS BAR
        self.progressBar.update(0)

        to_be_renamed = []

        # FLAG SELECTED TABLE ITEMS
        for indx, cb in enumerate(tables["RENAME"].checkboxes):

            # IF CHECKBOX SELECTED
            if cb.isChecked():

                # FETCH DATA FROM TABLE
                file = self.tableWidget.item(
                    indx, 0                                 # EACH ROW, 1ST COLUMN
                ).text()

                root = self.tableWidget.item(
                    indx, 1                                 # EACH ROW, 2ND COLUMN
                ).text()

                to_be_renamed.append(f"{root}//{file}")
                self.rows_to_remove.append(indx)

        if not to_be_renamed:
            self.dialog.show(
                "PLEASE SELECT AT LEAST ONE FILE",
                "NO SELECTION!",
                False
            )
            return

        # RENAME FILES WITH THREADS
        worker = RenameWorker(
            to_be_renamed,
            self.renameBy2ComboBox.currentText(),
            self.renameValueLineEdit.text()
        )

        # UPDATE PROGRESS BAR
        worker.progress_signal.connect(
            self.progressBar.update
        )

        # RENAME ROWS FROM THE TABLE
        worker.remove_rows_signal.connect(
            tables["RENAME"].remove_rows(
                self.rows_to_remove,
                self.totalRecordsLabel
            )
        )
        self.rows_to_remove.clear()

        # SUCCESSFULL ITEMS REMOVAL MESSAGE
        worker.is_success.connect(
            self.renaming_process_state
        )

        # UNSUCCESSFULL ITEMS REMOVAL MESSAGE
        worker.is_fail.connect(
            lambda error: self.dialog.show(
                f"SOMETHING WENT WRONG WHILE RENAMING | ERROR < {error} >",
                "C",    # CRITICAL MESSAGE
                False
            )
        )

        worker.run()

    def renaming_process_state(self, state: bool):

        if state:
            self.dialog.show(
                f"SUCCESSFULY RENAMED ALL ITEM(S)",
                "OPERATION SUCCESSFULL",
                False
            )

        else:
            self.dialog.show(
                f"SOME ITEM(S) WEREN'T RENAMED SUCCESSFULY",
                "OPERATION PARTIALLY SUCCESSFULL",
                False
            )
