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
        Called by the `ui_delete`
            * static vars called by self in the init, else use getters
    """

    ROOT_PATH:  str = os.getcwd() + "\\"
    DATA_PATH:  str = ROOT_PATH + "data\\"

    TRASH_PATH: str = DATA_PATH + "trash\\"
    CACHE_FILE: str = DATA_PATH + "Cache.json"
    TRASH_CONTENT_FILE = f"{TRASH_PATH}content.json"

    FILE_FINDER = Finder.File()
    FOLDER_FINDER = Finder.Folder()

    FILE_REMOVER = Delete.File()
    FOLDER_REMOVER = Delete.Folder()

    """
    /////////////////////////////////////////////////
                    FINDER METHODS
    //////////////////////////////////////////////////////
    """

    def update_finder_param(self, path: str, is_recursive: bool) -> None:
        """
            Variables set from UI after rendering
        """

        self.FILE_FINDER.set_path(path)
        self.FILE_FINDER.set_recursive(is_recursive)

        self.FOLDER_FINDER.set_path(path)
        self.FOLDER_FINDER.set_recursive(is_recursive)

    def get_files_by_name(self, name: str) -> dict:
        return self.FILE_FINDER.find("NAME", name)

    def get_folders_by_name(self, name: str) -> dict:
        return self.FOLDER_FINDER.find("NAME", name)

    def get_files_by_pattern(self, pattern: str) -> dict:
        return self.FILE_FINDER.find("PATTERN", pattern)

    def get_folders_by_pattern(self, pattern: str) -> dict:
        return self.FOLDER_FINDER.find("PATTERN", pattern)

    def get_files_by_extension(self, extension: str) -> dict:
        return self.FILE_FINDER.find("EXTENSION", extension)

    """
    /////////////////////////////////////////////////////
                    REMOVER METHODS
    ///////////////////////////////////////////
    """

    def update_remover_param(self) -> None:
        """
            Set when remover object init
        """

        self.FILE_REMOVER.set_remover_param(
            self.TRASH_CONTENT_FILE,
            self.TRASH_PATH
        )
        self.FOLDER_REMOVER.set_remover_param(
            self.TRASH_CONTENT_FILE,
            self.TRASH_PATH
        )

    def remove_file(self, file_path: str) -> None:
        self.FILE_REMOVER.remove(file_path)

    def remove_folder(self, folder_path: str, folder_name: str) -> None:
        self.FOLDER_REMOVER.remove(folder_path, folder_name)

    def restore_removed_content(self) -> int:
        return self.FILE_REMOVER.restore()

    def total_content_removed(self, is_file=True) -> int:
        """
            Get total num files/folders removed and reset it to `0`
            for the next iteration
        """

        if is_file:
            total = self.FILE_REMOVER.get_removed_content_count()
            self.FILE_REMOVER.reset_removed_content_count()

        else:
            total = self.FOLDER_REMOVER.get_removed_content_count()
            self.FOLDER_REMOVER.reset_removed_content_count()

        return total
