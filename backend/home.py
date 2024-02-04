import json
import os
import shutil

from environment import Common

class Feature(Common):
    """
        Main Page interactions and functionality
    """

    def __init__(self) -> None:
        super().__init__()

    def set_display_mode(self):
        """
            CHANGE DISPLAY MODE FROM DARK/LIGHT OR LIGHT/DARK
            STORE THE BOOL VALUE IN THE DEFAULT SETTINGS
        """

        if self.dialog.show(
            "THEME WILL BE CHANGED AFTER RESTARTING",
            "Q"
        ):
            path = "data/settings/default.json"
            settings: dict = json.load(open(path))

            # INVERSE THE SAVED THEME MODE
            is_light_theme = False if settings.get("is_light_theme") else True

            settings["is_light_theme"] = is_light_theme

            json.dump(settings, open(path, "w"))

    def empty_trash(self):

        if self.dialog.show(
            "ATTENTION! THIS WILL EMPTY THE TRASH. YOU WILL NO LONGER ABLE TO RESTORE PREVIOUSLY EDITED FILES",
            "W"
        ):
            path = "data/trash"

            try:
                shutil.rmtree(path)
                os.mkdir(path)
                self.dialog.show(
                    f"TRASH REMOVED SUCCESSFULLY",
                    "I",
                    False
                )

            except Exception as e:
                self.dialog.show(
                    f"SOMTHING WENT WRONG. COULDN'T EMPTY TRASH | ERROR {e}",
                    "C",
                    False
                )
