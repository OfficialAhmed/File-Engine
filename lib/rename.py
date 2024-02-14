"""
    ### Classes handle renaming file/folder

"""


import json
import os


class Engine:

    def __init__(self) -> None:

        # UPDATED BY CALLER WHEN INIT
        self.trash_folder_path = None
        self.trash_content_file = None

        # REMOVED CONTENT TRACKER - FOR RESTORE FEATURE
        self.removed_content = {}

    def set_renaming_param(self, content_file_path: str, trash_folder_path: str, renaming_method: str, custom_val: str, files: list) -> None:
        """
            * Update init variables
            * Create trash folder, if doesnt exist
            * Check trash content file, if exists
        """
        self.trash_folder_path = trash_folder_path
        self.trash_content_file = content_file_path

        self.files = files
        self.custom_value = custom_val
        self.renaming_method = renaming_method

        # MAKE TRASH FOLDER IF IT DOESNT EXIST
        if not os.path.exists(self.trash_folder_path):
            os.mkdir(self.trash_folder_path)

        if os.path.exists(self.trash_content_file) and os.path.getsize(self.trash_content_file) > 0:
            self.removed_content = json.load(open(self.trash_content_file))

    def generate_bulk_titles(self, data_type: str) -> list[tuple]:
        """ 
            GENERATE TITLES IN BULK WITH DIFFERENT 
        """

        new_titles: list[tuple] = []
        start_index = 0

        # NUMBERING BASED ON LAST DIGIT
        match self.renaming_method[-1]:
            case "0":   start_index = 0
            case "1":   start_index = 1
            case _:     start_index = self.custom_value

        symbol = self.renaming_method[0]

        for index, old in enumerate(self.files, start_index):

            # SYMBOLS
            title = f"{index}"
            if "AS PREFIX" in self.renaming_method:
                title = f"{symbol}{index}"
            elif "AS SUFFIX" in self.renaming_method:
                title = f"{index}{symbol}"

            if data_type == "FILES":
                dot_index = old.rfind(".")
                file_ext = "." + old[dot_index + 1:]
                new = old[:old.rfind("/")] + title + file_ext

            else:
                new = old[:old.rfind("/")] + title

            new_titles.append((old, new))
        return new_titles

    def generate_timestamp_titles(self) -> list[tuple]:
        pass


class File(Engine):

    def __init__(self) -> None:
        super().__init__()

    def get_titles(self) -> list:
        return self.generate_bulk_titles("FILES")


class Folder(Engine):

    def __init__(self) -> None:
        super().__init__()

    def get_titles(self) -> list:
        return self.generate_bulk_titles("FOLDERS")
