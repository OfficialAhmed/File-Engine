
from environment import Common, RenameWorker, tables
from PySide6.QtWidgets import QLineEdit, QComboBox


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


class Option:
    """
        AVAILABLE OPTIONS FOR DIFFIRENT CATEGORY.
        AUTOMATED BASED ON THE CATEGORY PICKED
    """

    def __init__(self, cb: QComboBox, cb2: QComboBox, custom_input: QLineEdit) -> None:

        self.cb:            QComboBox = cb
        self.cb2:           QComboBox = cb2
        self.custom_input:  QLineEdit = custom_input

        self.options = {
            "BULK": (
                "START FROM 0",
                "START FROM 1",
                "START FROM CUSTOM",
                "# AS PREFIX & START FROM 0",
                "# AS PREFIX & START FROM CUSTOM",
                "# AS SUFFIX & START FROM 0",
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

        self.custom_options = (
            "START FROM CUSTOM",
            "# AS PREFIX & START FROM CUSTOM",
            "# AS SUFFIX & START FROM CUSTOM"
        )

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

    def toggle_custom_value(self):

        self.custom_input.setEnabled(
            self.cb2.currentText() in self.custom_options
        )
