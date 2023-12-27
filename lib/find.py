"""
    ### Classes handle Searching for file/folder if exist(s)
        * Built-in search algorithms used from lib os
"""

import os
import re


class Finder:

    def __init__(self) -> None:

        self.path = ""
        self.is_recursive = None
        self.is_case_sensitive = None

    def get_files(self) -> str:
        """
            Yield files in parent folder
        """

        for file in os.listdir(self.path):
            yield file

    def get_files_recursive(self) -> tuple[str:str]:
        """
            Yields tuple (root, file) recursively thorugh all folders

        """

        for root, _, files in os.walk(self.path):

            for file in files:
                yield (root, file)

    def get_folders(self):

        for file in os.listdir(self.path):
            yield file

    def get_folders_recursive(self):

        for root, folders, _ in os.walk(self.path):

            for folder in folders:
                yield (root, folder)


class File(Finder):

    def __init__(self) -> None:
        super().__init__()

        self.file_counter = 0
        self.detected_files = {}

    def set_path(self, path: str) -> None:
        self.path = path

    def set_recursive(self, rec: bool) -> None:
        self.is_recursive = rec

    def set_case_sensitive(self, cs: bool) -> None:
        self.is_case_sensitive = cs

    def reset_detected_files(self) -> None:
        self.file_counter = 0
        self.detected_files = {}

    def add_detected_file(self, file, root=''):
        """
            Store the detected file in a dict along its size and root
        """

        # SET DEFAULT PATH - FOR FOLDER DETECTION
        if not root:
            root = self.path

        # CONVERT BYTES TO MB
        size = os.path.getsize(f"{root}/{file}") / (1024*1024)

        self.detected_files[self.file_counter] = {
            "file": file,
            "root": root,
            "size": round(size, 3)
        }

        self.file_counter += 1

    def find(self, by: str, input: str):

        # TODO: METHOD TO BE TRUNCATED
        # RESET FILES ON EVERY SEARCH
        self.reset_detected_files()

        if self.is_recursive:

            for root, file in self.get_files_recursive():

                match by:

                    case "NAME":

                        if file[: file.find(".")].strip() == input:
                            self.add_detected_file(file, root)

                    case "EXTENSION":

                        if file.endswith(f".{input}"):
                            self.add_detected_file(file, root)

        else:

            for file in self.get_files():

                match by:

                    case "NAME":
                        if file[: file.find(".")].strip() == input:
                            self.add_detected_file(file)

                    case "EXTENSION":

                        if file.endswith(f".{input}"):
                            self.add_detected_file(file)

        return self.detected_files

    def search(self, by: str, input: str | list, exclude=[], custom="") -> dict:

        if exclude:

            # PRE CALCULATE THE REGEX FOR EXCLUSIONS
            exclude = set(exclude)
            num_regex = f"^[{''.join(set('0-9') - exclude)}]+$"
            alpha_regex = f"^[{''.join(sorted(set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') - exclude))}]+$"
            symbol_regex = f"^[^{''.join(map(re.escape, exclude))}]+$"

        # RESET FILES ON EVERY SEARCH
        self.reset_detected_files()

        if self.is_recursive:

            for root, file in self.get_files_recursive():

                file_title: str = file[: file.rfind(".")].strip()
                file_ext: str = file[file.rfind(".")+1:].strip()

                match by:

                    case "TITLE":
                        match input:
                            case "ALPHABETS":
                                if file_title.isalpha():
                                    self.add_detected_file(file, root)
                            case "SYMBOLS":
                                if re.match(re.compile(r'^[^\w\s]+$'), file_title):
                                    self.add_detected_file(file, root)
                            case "ALPHABETS & SYMBOLS":
                                if re.match(re.compile(r'^[a-zA-Z!@#$%^&*()_+.\\-]+|^[^\s/\\:*?"<>|]+$'), file_title):
                                    self.add_detected_file(file, root)
                            case "ALPHABETS & NUMBERS":
                                if re.match(re.compile(r'^[a-zA-Z0-9]+$'), file_title):
                                    self.add_detected_file(file, root)
                            case "NUMBERS & SYMBOLS":
                                if re.match(re.compile(r'^[0-9!@#$%^&*()_+.\\-]+|^[^\s/\\:*?"<>|]+$'), file_title):
                                    self.add_detected_file(file, root)
                            case "ALPHABETS EXCLUSION":
                                if re.match(re.compile(alpha_regex), file_title):
                                    self.add_detected_file(file, root)
                            case "NUMBERS EXCLUSION":
                                if re.match(re.compile(num_regex), file_title):
                                    self.add_detected_file(file, root)
                            case "SYMBOLS EXCLUSION":
                                if re.match(re.compile(symbol_regex), file_title):
                                    self.add_detected_file(file, root)
                            case "CUSTOM":
                                # (CONTAIN -> CUSTOM) OPTION CUSTOM INPUT LOOKING SPECIFIC INPUT IN TITLE
                                try:
                                    if re.match(re.compile(custom), file_title):
                                        self.add_detected_file(file, root)
                                except re.error:
                                    print("regex invalid")

                            case _:
                                # (EQUAL TO) OPTION CUSTOM INPUT BY USER LOOKING FOR SPECIFIC INPUT
                                if file_title in input:
                                    self.add_detected_file(file, root)

                    case "EXTENSION":
                        match input:
                            case "ALPHABETS":
                                if file_ext.isalpha():
                                    self.add_detected_file(file, root)
                            case "SYMBOLS":
                                if re.match(re.compile(r'^[^\w\s]+$'), file_ext):
                                    self.add_detected_file(file, root)
                            case "ALPHABETS & SYMBOLS":
                                if re.match(re.compile(r'^[a-zA-Z!@#$%^&*()_+.\\-]+|^[^\s/\\:*?"<>|]+$'), file_ext):
                                    self.add_detected_file(file, root)
                            case "ALPHABETS & NUMBERS":
                                if re.match(re.compile(r'^[a-zA-Z0-9]+$'), file_ext):
                                    self.add_detected_file(file, root)
                            case "NUMBERS & SYMBOLS":
                                if re.match(re.compile(r'^[0-9!@#$%^&*()_+.\\-]+|^[^\s/\\:*?"<>|]+$'), file_ext):
                                    self.add_detected_file(file, root)
                            case "ALPHABETS EXCLUSION":
                                if re.match(re.compile(alpha_regex), file_ext):
                                    self.add_detected_file(file, root)
                            case "NUMBERS EXCLUSION":
                                if re.match(re.compile(num_regex), file_ext):
                                    self.add_detected_file(file, root)
                            case "SYMBOLS EXCLUSION":
                                if re.match(re.compile(symbol_regex), file_ext):
                                    self.add_detected_file(file, root)
                            case "CUSTOM":
                                # (CONTAIN -> CUSTOM) OPTION CUSTOM INPUT LOOKING SPECIFIC INPUT IN TITLE
                                try:
                                    if re.match(re.compile(custom), file_ext):
                                        self.add_detected_file(file, root)
                                except re.error:
                                    print("regex invalid")

                            case _:
                                # (EQUAL TO) OPTION CUSTOM INPUT BY USER LOOKING FOR SPECIFIC INPUT
                                if file_ext in input:
                                    self.add_detected_file(file, root)
        else:

            for file in self.get_files():

                file_title: str = file[: file.find(".")].strip()
                file_ext: str = file[file.find(".")+1:].strip()

                match by:

                    case "TITLE":
                        match input:
                            case "ALPHABETS":
                                if file_title.isalpha():
                                    self.add_detected_file(file)
                            case "SYMBOLS":
                                if re.match(re.compile(r'^[^\w\s]+$'), file_title):
                                    self.add_detected_file(file)
                            case "ALPHABETS & SYMBOLS":
                                if re.match(re.compile(r'^[a-zA-Z!@#$%^&*()_+.\\-]+|^[^\s/\\:*?"<>|]+$'), file_title):
                                    self.add_detected_file(file)
                            case "ALPHABETS & NUMBERS":
                                if re.match(re.compile(r'^[a-zA-Z0-9]+$'), file_title):
                                    self.add_detected_file(file)
                            case "NUMBERS & SYMBOLS":
                                if re.match(re.compile(r'^[0-9!@#$%^&*()_+.\\-]+|^[^\s/\\:*?"<>|]+$'), file_title):
                                    self.add_detected_file(file)
                            case "ALPHABETS EXCLUSION":
                                if re.match(re.compile(alpha_regex), file_title):
                                    self.add_detected_file(file)
                            case "NUMBERS EXCLUSION":
                                if re.match(re.compile(num_regex), file_title):
                                    self.add_detected_file(file)
                            case "SYMBOLS EXCLUSION":
                                if re.match(re.compile(symbol_regex), file_title):
                                    self.add_detected_file(file)
                            case "CUSTOM":
                                # (CONTAIN -> CUSTOM) OPTION CUSTOM INPUT LOOKING SPECIFIC INPUT IN TITLE
                                try:
                                    if re.match(re.compile(custom), file_title):
                                        self.add_detected_file(file)
                                except re.error:
                                    print("regex invalid")

                            case _:
                                # (EQUAL TO) OPTION CUSTOM INPUT BY USER LOOKING FOR SPECIFIC INPUT
                                if file_title in input:
                                    self.add_detected_file(file)

                    case "EXTENSION":
                        match input:
                            case "ALPHABETS":
                                if file_ext.isalpha():
                                    self.add_detected_file(file)
                            case "SYMBOLS":
                                if re.match(re.compile(r'^[^\w\s]+$'), file_ext):
                                    self.add_detected_file(file)
                            case "ALPHABETS & SYMBOLS":
                                if re.match(re.compile(r'^[a-zA-Z!@#$%^&*()_+.\\-]+|^[^\s/\\:*?"<>|]+$'), file_ext):
                                    self.add_detected_file(file)
                            case "ALPHABETS & NUMBERS":
                                if re.match(re.compile(r'^[a-zA-Z0-9]+$'), file_ext):
                                    self.add_detected_file(file)
                            case "NUMBERS & SYMBOLS":
                                if re.match(re.compile(r'^[0-9!@#$%^&*()_+.\\-]+|^[^\s/\\:*?"<>|]+$'), file_ext):
                                    self.add_detected_file(file)
                            case "ALPHABETS EXCLUSION":
                                if re.match(re.compile(alpha_regex), file_ext):
                                    self.add_detected_file(file)
                            case "NUMBERS EXCLUSION":
                                if re.match(re.compile(num_regex), file_ext):
                                    self.add_detected_file(file)
                            case "SYMBOLS EXCLUSION":
                                if re.match(re.compile(symbol_regex), file_ext):
                                    self.add_detected_file(file)
                            case "CUSTOM":
                                # (CONTAIN -> CUSTOM) OPTION CUSTOM INPUT LOOKING SPECIFIC INPUT IN TITLE
                                try:
                                    if re.match(re.compile(custom), file_ext):
                                        self.add_detected_file(file)
                                except re.error:
                                    print("regex invalid")

                            case _:
                                # (EQUAL TO) OPTION CUSTOM INPUT BY USER LOOKING FOR SPECIFIC INPUT
                                if file_ext in input:
                                    self.add_detected_file(file)
        return self.detected_files


class Folder(Finder):

    def __init__(self) -> None:
        super().__init__()

        self.folder_counter = 0
        self.detected_folders = {}

    def set_path(self, path: str):
        self.path = path

    def reset_detected_folders(self) -> None:
        self.folder_counter = 0
        self.detected_folders = {}

    def set_recursive(self, rec: bool):
        self.is_recursive = rec

    def set_case_sensitive(self, cs: bool) -> None:
        self.is_case_sensitive = cs

    def add_detected_folder(self, folder, root=''):
        """
            Store the detected file in a dict along its size and root
        """

        # SET DEFAULT PATH - FOR FOLDER DETECTION
        if not root:
            root = self.path

        self.detected_folders[self.folder_counter] = {
            "folder": folder,
            "root": root,
            "size": "-"
        }

        self.folder_counter += 1

    def find(self, by: str, input: str):

        # RESET FILES ON EVERY SEARCH
        self.reset_detected_folders()

        if self.is_recursive:

            for root, folder in self.get_folders_recursive():

                match by:

                    case "NAME":
                        if folder == input:
                            self.add_detected_folder(folder, root)

        else:

            for folder in self.get_files():

                match by:

                    case "NAME":
                        if folder == input:
                            self.add_detected_folder(folder)

        return self.detected_folders
