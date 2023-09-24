"""

    CONTROLLER CACHE:
        CONNECTS THE BACK-END (lib) WITH THE FRONT-END (Interface)

    CALLABLE METHODS BY THE UI

"""


import lib.move as Move
import lib.delete as Delete
import lib.find as Finder


class Cache:

    # STATIC OBJECTS - RECUSIVE ENABLED BY DEFAULT
    FILE_FINDER = Finder.File
    FOLDER_FINDER = Finder.Folder


    def __init__(self) -> None:

        self.file_finder = Finder.File
        self.folder_finder = Finder.Folder
        self.trash_folder_path = "trash\\"

        self.trash_content_file = f"{self.trash_folder_path}content.json"


    def update_param(self, path:str, is_recursive:bool) -> None:
        self.file_finder.set_path(path)
        self.file_finder.set_recursive(is_recursive)

        self.folder_finder.set_path(path)
        self.folder_finder.set_recursive(is_recursive)


    def get_files_by_name(self, name:str) -> list:
        print(self.file_finder.by_name(name))


    def get_files_by_extension(self, extension:str) -> list:
        print(self.file_finder.by_extention(extension))


    def get_files_by_pattern(self, pattern:str) -> list:
        print(self.file_finder.by_pattern(pattern))


    def get_folders_by_name(self, name:str) -> list:
        print(self.folder_finder.by_name(name))


    def get_folders_by_pattern(self, pattern:str) -> list:
        print(self.folder_finder.pattern(pattern))
