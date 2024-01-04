"""
    ### Classes handle Searching for file/folder if exist(s)
        * Built-in search algorithms used from lib os
"""

import os
import re


class Finder:

    def __init__(self) -> None:

        self.path = ""
        self.counter = 0
        self.is_recursive = None
        self.is_case_sensitive = None
        self.detected_matches = {}
        self.regex = {
            "SYMBOLS":              r"^[@#$%^&*(){}~'_+\-.]+$",
            "ALPHABETS & SYMBOLS":  r'^[a-zA-Z!@#$%^&*()_+.\\-]+|^[^\s/\\:*?"<>|]+$',
            "ALPHABETS & NUMBERS":  r'^[a-zA-Z0-9]+$',
            "NUMBERS & SYMBOLS":    r"^[0-9!@#$%^&*(){}~'_+\-.]+$"
        }

    def exclude_regex(self, exclude):
        self.regex["NUMBERS EXCLUSION"] = f"^[{''.join(set('0-9') - exclude)}]+$"
        self.regex["SYMBOLS EXCLUSION"] = "^[^" + "@" + \
            "#$%^&*()" + "{}~'_+\-.]+$"  # FIXME: doesnt work
        self.regex["ALPHABETS EXCLUSION"] = f"^[{''.join(sorted(set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') - exclude))}]+$"

    def set_path(self, path: str) -> None:
        self.path = path

    def reset_detected_matches(self) -> None:
        self.folder_counter = 0
        self.detected_folders = {}

    def set_recursive(self, rec: bool):
        self.is_recursive = rec

    def set_case_sensitive(self, cs: bool) -> None:
        self.is_case_sensitive = cs

    def add_detected_match(self, object_name: str, match: str, root='') -> None:
        """
            Store the detected file in a dict along its size and root
        """

        # SET DEFAULT PATH - FOR FOLDER DETECTION
        if not root:
            root = self.path

        # CONVERT BYTES TO MB
        size = os.path.getsize(f"{root}/{match}") / (1024*1024)

        self.detected_matches[self.counter] = {
            object_name: match,
            "root": root,
            "size": round(size, 3)
        }

        self.counter += 1

    def get_files(self) -> str:
        """
            Yield files in parent folder
        """

        for file in os.listdir(self.path):
            yield file

    def get_recursive(self) -> tuple[str:str]:
        """
            Yields tuple (root, file) recursively thorugh all folders
        """

        for root, _, files in os.walk(self.path):

            for file in files:
                yield (root, file)

    def get_folders(self) -> str:

        for file in os.listdir(self.path):
            yield file

    def get_folders_recursive(self) -> tuple[str:str]:

        for root, folders, _ in os.walk(self.path):

            for folder in folders:
                yield (root, folder)

    def update_finder_param(self, path: str, is_recursive: bool, is_case_sensetive: bool) -> None:
        self.set_path(path)
        self.set_recursive(is_recursive)
        self.set_case_sensitive(is_case_sensetive)

    def get_by_title(self, input: list) -> dict:
        return self.search("TITLE", input)

    def get_by_extension(self, input: list) -> dict:
        return self.search("EXTENSION", input)

    def get_only_alphabets(self, search: str) -> dict:
        return self.search(search, "ALPHABETS")

    def get_only_symbols(self, search: str) -> dict:
        return self.search(search, "SYMBOLS")

    def get_alpha_symbol(self, search: str) -> dict:
        return self.search(search, "ALPHABETS & SYMBOLS")

    def get_alpha_num(self, search: str) -> dict:
        return self.search(search, "ALPHABETS & NUMBERS")

    def get_num_symbol(self, search: str) -> dict:
        return self.search(search, "NUMBERS & SYMBOLS")

    def get_custom(self, search: str, input: str) -> dict:
        return self.search(search, "CUSTOM (REGEX)", custom=input)

    def get_alpha_exclude(self, search: str, input) -> dict:
        return self.search(search, "ALPHABETS EXCLUSION", exclude=input)

    def get_num_exclude(self, search: str, input) -> dict:
        return self.search(search, "NUMBERS EXCLUSION", exclude=input)

    def get_symbol_exclude(self, search: str, input) -> dict:
        return self.search(search, "SYMBOLS EXCLUSION", exclude=input)


class File(Finder):

    def __init__(self) -> None:
        super().__init__()

    def search(self, by: str, input: str | list, exclude=[], custom="") -> dict:

        # RESET FILES ON EVERY SEARCH
        self.reset_detected_matches()

        if exclude:
            exclude = set(exclude)
            self.exclude_regex(exclude)

        def is_match(file: str, input: str | list) -> bool:

            file_title: str = file[: file.rfind(".")].strip()
            file_ext: str = file[file.rfind(".")+1:].strip()

            check = file_title
            if by == "EXTENSION":
                check = file_ext

            match input:

                case "ALPHABETS":

                    if check.isalpha():
                        return True

                case "CUSTOM (REGEX)":

                    # (CONTAIN -> CUSTOM) OPTION CUSTOM INPUT LOOKING SPECIFIC INPUT IN TITLE
                    try:
                        if re.match(re.compile(custom), check):
                            return True
                    except re.error:
                        print("regex invalid")

                case _:

                    if isinstance(input, list):
                        # (EQUAL TO) OPTION CUSTOM INPUT BY USER LOOKING FOR SPECIFIC INPUT
                        if check in input:
                            return True
                    else:
                        if re.match(re.compile(self.regex.get(input)), check):
                            return True

            return False

        if self.is_recursive:

            for root, file in self.get_recursive():
                if is_match(file, input):
                    self.add_detected_match("file", file, root)

        else:

            for file in self.get_files():
                if is_match(file, input):
                    self.add_detected_match("file", file)

        return self.detected_matches


class Folder(Finder):

    def __init__(self) -> None:
        super().__init__()

    def search(self, by, input: str | list, exclude=[], custom="") -> dict:
        """
            arg: by 
                A PLACEHOLDER NEVER USED FOR FOLDER SEARCH ... TO BE FIXED
        """

        # RESET FILES ON EVERY SEARCH
        self.reset_detected_matches()

        if exclude:
            exclude = set(exclude)
            self.exclude_regex(exclude)

        def is_match(folder: str, input: str | list) -> bool:

            match input:

                case "ALPHABETS":

                    if folder.isalpha():
                        return True

                case "CUSTOM (REGEX)":

                    # (CONTAIN -> CUSTOM) OPTION CUSTOM INPUT LOOKING SPECIFIC INPUT IN TITLE
                    try:
                        if re.match(re.compile(custom), folder):
                            return True
                    except re.error:
                        print("regex invalid")

                case _:

                    if isinstance(input, list):
                        # (EQUAL TO) OPTION CUSTOM INPUT BY USER LOOKING FOR SPECIFIC INPUT
                        if folder in input:
                            return True
                    else:
                        if re.match(re.compile(self.regex.get(input)), folder):
                            return True

            return False

        if self.is_recursive:

            for root, file in self.get_recursive():
                if is_match(file, input):
                    self.add_detected_match("folder", file, root)

        else:

            for file in self.get_files():
                if is_match(file, input):
                    self.add_detected_match("folder", file)

        return self.detected_matches
