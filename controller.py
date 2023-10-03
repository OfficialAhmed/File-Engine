"""

    CONTROLLER CACHE:
        CONNECTS THE BACK-END (lib) WITH THE FRONT-END (Interface)

    CALLABLE METHODS BY THE UI

"""


import os
import lib.move as Move
import lib.find as Finder
import lib.delete as Delete


class Environment:
    """
        ### UI Common methods and static variables
            * static vars called by self in the init, else use getters
    """

    ROOT_PATH:  str = os.getcwd() + "\\"
    DATA_PATH:  str = ROOT_PATH + "data\\"

    TRASH_PATH: str = DATA_PATH + "trash\\"
    CACHE_FILE: str = DATA_PATH + "Cache.json"

    def __init__(self) -> None:
        self.__file_finder = Finder.File()
        self.__folder_finder = Finder.Folder()

        self.__file_remover = Delete.File()
        self.__folder_remover = Delete.Folder()

        self.trash_content_file = f"{self.TRASH_PATH}content.json"

        self.__update_remover_param()

    """
    ///////////////////////
        Finder methods
    ///////////////////////
    """

    def update_finder_param(self, path: str, is_recursive: bool) -> None:
        """
            Variables set from UI after rendering
        """

        self.__file_finder.set_path(path)
        self.__file_finder.set_recursive(is_recursive)

        self.__folder_finder.set_path(path)
        self.__folder_finder.set_recursive(is_recursive)

    def get_files_by_name(self, name: str) -> dict:
        return self.__file_finder.find("NAME", name)

    def get_folders_by_name(self, name: str) -> dict:
        return self.__folder_finder.find("NAME", name)

    def get_files_by_pattern(self, pattern: str) -> dict:
        return self.__file_finder.find("PATTERN", pattern)

    def get_folders_by_pattern(self, pattern: str) -> dict:
        return self.__folder_finder.find("PATTERN", pattern)

    def get_files_by_extension(self, extension: str) -> dict:
        return self.__file_finder.find("EXTENSION", extension)

    """
    ///////////////////////
        Remover methods
    ///////////////////////
    """

    def __update_remover_param(self) -> None:
        """
            Set when remover object init
        """

        self.__file_remover.set_remover_param(
            self.trash_content_file,
            self.TRASH_PATH
        )

    def remove_file(self, file_path: str) -> None:
        self.__file_remover.remove(file_path)

    def remove_folder(self, folder_path: str, folder_name: str) -> None:
        self.__folder_remover.remove(folder_path, folder_name)
