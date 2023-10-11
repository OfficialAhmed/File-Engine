"""
    Parent class holds constant values 
    for the interface
"""

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from controller import Environment

class Common:

    def __init__(self) -> None:
        self.constant = Constant()

    def set_icon(self, widget: QWidget, name: str, size=(18, 18)) -> str:

        widget.setIcon(
            QIcon(f"{self.constant.get_resources_path()}icons/{name}.svg")
        )

        widget.setIconSize(QSize(*size))

    def get_user_path(self) -> str | None:
        """
        Render a window to select the path
        """

        options = QFileDialog.Options()
        dialog = QFileDialog()
        dialog.setOptions(options)

        path = QFileDialog.getExistingDirectory(
            None,
            "PICK A FOLDER TO CONTINUE",
            "",  # PATH ON-WINDOW RENDER
            options=options,
        )

        # RETURN THE DIRECTORY PATH, OTHERWISE RETURN NONE
        return path if path else None
    
    def get_progress_unit(
            self,
            total_files: int,
        ) -> float:

        """
            Calculates the shunk to progress in percentage
        """

        return 100 / total_files


class Constant:

    _RESOURCES_PATH = ":/images/images/"

    @classmethod
    def get_resources_path(self):
        return self._RESOURCES_PATH


class Html:

    COLOR: dict = {
        "dark blue": "33, 37, 43",
        "light blue": "52, 59, 72",
        "dracula pink": "255, 121, 198",
        "dracula purple": "189, 147, 249"
    }

    def __init__(self) -> None:

        self.color = self.COLOR

    def get_bg_color(self, name: str) -> str:
        return f"background-color: rgb({self.color.get(name)})"

    def get_rgb_color(self, name: str) -> tuple[int, int, int]:
        return tuple(int(x) for x in self.color.get(name).split(", "))


class ProgressBar:

    # STORE GLOABLY FOR ALL CHILDREN
    progressBar = None

    def update(self, progress: int):
        self.progressBar.setValue(int(progress * 100))

    def set_widget(self, widget: QProgressBar):
        """
            #### Called after the progressbar widget rendered 
            * ONE TIME CALL METHOD
            * Widget will be stored in class for reference
        """
        self.progressBar = widget
        ProgressBar.progressBar = widget # Reference


class DeleteWorker(QThread):
    """
        DELETE FILES IN A SEPERATE THREAD FROM THE UI
    """

    # SIGNALS TO COMMUNICATE TO THE MAIN THREAD
    removed_rows_signal = Signal(list)
    update_progress_signal = Signal(float)

    def __init__(self, data: dict, checkboxes: list, lookup_type: str):
        super().__init__()

        self.data = data
        self.checkboxes = checkboxes
        self.lookup_type = lookup_type

        self.environment = Environment()

    def run(self):
        """
            AUTOMATICALLY INVOKED WHEN thread.start() IS CALLED        
        """

        removed_rows = []
        total_items = len(self.data)
        completed_items = 0

        for index, checkbox in enumerate(self.checkboxes):

            if checkbox.isChecked():

                data: dict = self.data.get(index)
                content_root = data.get("root")

                match self.lookup_type:

                    case "FILES":

                        file = data.get("file")

                        self.environment.remove_file(
                            f"{content_root}\\{file}"
                        )

                    case "FOLDERS":

                        folder = data.get("folder")

                        self.environment.remove_folder(
                            f"{content_root}\\{folder}",
                            folder
                        )

                removed_rows.append(index)
                self.data.pop(index)

            completed_items += 1
            progress = completed_items / total_items
            self.update_progress_signal.emit(progress)

        self.removed_rows_signal.emit(removed_rows)

        
        