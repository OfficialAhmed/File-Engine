"""
    ### Classes handle renaming file/folder

"""


import json
import time
import os


class Engine:

    def __init__(self) -> None:

        self.paths: list[str] = []      # PATHS OF FILES OR FOLDERS
        self.data_type: str = ""        # FILES OR FOLDERS
        self.timestamps = {
            "[hh_mm_ss] ~ seed":               "[%H_%M_%S] ~",
            "[DD_MM_YY] ~ seed":               "[%d_%m_%y] ~",
            "[DD_MM_YY] [hh] ~ seed":          "[%d_%m_%y] [%H] ~",
            "[DD_MM_YY] [hh_mm] ~ seed":       "[%d_%m_%y] [%H_%M] ~",
            "[DD_MM_YY] [hh_mm_ss] ~ seed":    "[%d_%m_%y] [%H_%M_%S] ~"
        }
        
        # UPDATED BY CALLER WHEN INIT
        self.trash_folder_path = None
        self.trash_content_file = None

        # REMOVED CONTENT TRACKER - FOR RESTORE FEATURE
        self.removed_content = {}

    def _set_renaming_param(
            self,
            content_file_path: str,
            trash_folder_path: str,
            renaming_method: str,
            renaming_algo: str,
            custom_val: str,
            files: list
    ) -> None:
        """
            * Update init variables
            * Create trash folder, if doesnt exist
            * Check trash content file, if exists
        """
        self.trash_folder_path = trash_folder_path
        self.trash_content_file = content_file_path

        self.paths = files
        self.custom_value = custom_val
        self.renaming_algo = renaming_algo
        self.renaming_method = renaming_method

        # MAKE TRASH FOLDER IF IT DOESNT EXIST
        if not os.path.exists(self.trash_folder_path):
            os.mkdir(self.trash_folder_path)

        if os.path.exists(self.trash_content_file) and os.path.getsize(self.trash_content_file) > 0:
            self.removed_content = json.load(open(self.trash_content_file))

    def _reform_path(self, path: str, new_title: str) -> str:
        """
            RENAME FILE OR FOLDER TITLE INSIDE A GIVEN PATH
        """

        if self.data_type != "FILES":
            return path[:path.rfind("/")] + new_title

        else:
            dot_index = path.rfind(".")
            file_ext = f".{path[dot_index + 1:]}"
            return path[:path.rfind("/")] + new_title + file_ext

    def _generate_bulk_titles(self, data_type: str) -> list[tuple]:
        """ 
            GENERATE TITLES IN BULK WITH DIFFERENT NUMBERING POSITION 
        """

        self.data_type = data_type
        start_index = 0
        new_titles: list[tuple] = []

        # NUMBERING BASED ON LAST DIGIT
        match self.renaming_method[-1]:
            case "0":   start_index = 0
            case "1":   start_index = 1
            case _:     start_index = self.custom_value

        symbol = self.renaming_method[0]

        for index, file_path in enumerate(self.paths, start_index):

            # SYMBOLS
            title = f"{index}"
            if "AS PREFIX" in self.renaming_method:
                title = f"{symbol}{index}"
            elif "AS SUFFIX" in self.renaming_method:
                title = f"{index}{symbol}"

            new_titles.append(
                (file_path, self._reform_path(file_path, title))
            )

        return new_titles

    def _generate_timestamp_titles(self, data_type: str) -> list[tuple]:
        """
            GENERATE TITLE BASED ON FILE|FOLDER LAST MODIFIED TIMESTAMP 
        """

        self.data_type = data_type
        new_titles: list[tuple] = []

        for seed, path in enumerate(self.paths, 1):

            # LAST-MODIFIED TIMESTAMP
            # SEED AS SUFFIX, TO AVOID RENAMING CLASHES
            last_modified_time = time.strftime(
                f'{self.timestamps.get(self.renaming_method)} {seed}',
                time.localtime(
                    os.path.getmtime(path)
                )
            )

            new_titles.append(
                (path, self._reform_path(path, last_modified_time))
            )

        return new_titles


class File(Engine):

    def __init__(self) -> None:
        super().__init__()
        self.TYPE = "FILES"

    def get_bulk_titles(self) -> list:
        return self._generate_bulk_titles(self.TYPE)

    def get_timestamp_titles(self) -> list:
        return self._generate_timestamp_titles(self.TYPE)


class Folder(Engine):

    def __init__(self) -> None:
        super().__init__()
        self.TYPE = "FOLDERS"

    def get_bulk_titles(self) -> list:
        return self._generate_bulk_titles(self.TYPE)

    def get_timestamp_titles(self) -> list:
        return self._generate_timestamp_titles(self.TYPE)
