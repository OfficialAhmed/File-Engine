import os
import json
from environment import Common, RestoreWorker, DeleteWorker, tables


# FIXME: RESPONSE CLASS DUPLICATED FOR TESTING ONLY
class Response(Common):

    def __init__(self, totalRecordsLabel, tableWidget, searchTypeHiddenLabel) -> None:
        super().__init__()

        # WIDGETS REQUIRED FROM THE FRONT-END
        self.tableWidget = tableWidget
        self.totalRecordsLabel = totalRecordsLabel
        self.searchTypeHiddenLabel = searchTypeHiddenLabel

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
                    f"CANNOT FIND PREVIOUSLY MOVED FILES.",
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

    def move_content_clicked(self):

        # IF USER DID NOT ACCEPT DELETE PROCESS, TERMINATE
        if not self.dialog.show(
            "ARE YOU SURE YOU WANT TO *REMOVE* THE SELECTED FILES?",
            "ARE YOU SURE?"
        ):
            return

        # RESET PROGRESS BAR
        self.progressBar.update(0)

        to_be_removed = []

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

                to_be_removed.append(f"{root}//{file}")
                self.rows_to_remove.append(indx)

        if not to_be_removed:
            self.dialog.show(
                "PLEASE SELECT AT LEAST ONE FILE",
                "NO SELECTION!",
                False
            )
            return

        # DELETE FILES WITH THREADS
        worker = DeleteWorker(
            to_be_removed,
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
            self.moving_process_state
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

    def moving_process_state(self, state: bool):

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
