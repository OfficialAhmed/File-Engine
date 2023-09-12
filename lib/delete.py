"""
    ### Classes handle removing for file/folder
    
    Deleting is simply moving files to a temp folder 'Trash' before completely erasing it from the computer.
    Upon user permission and confirmation -> Empty trash folder
    
"""

import os, shutil
from main import Common


class Engine(Common):
    """ Parent class for removing. Hold the common data processing between files and folders """

    def __init__(self) -> None:
        super().__init__()

        self.trash_folder = "trash"
        self.create_trash()


    def create_trash(self):
        """
            Make trash if it doesnt exist
        """

        if not os.path.exists(self.trash_folder):
            os.mkdir(self.trash_folder)


    def empty_trash(self):
        """
            Delete all content in the "trash" folder
        """

        for file in os.listdir(self.trash_folder):
            os.remove(file)


class File(Engine):

    def __init__(self) -> None:
        super().__init__()


    def by_extension(self, extension:str):
        """
            Find the files with the provided extension then move them to trash folder
        """

        for file in self.file_finder(self.current_path).by_extention(extension):  
            shutil.move(file, self.trash_folder)

    def by_name(self):
        pass


class Folder(Engine):
    def __init__(self) -> None:
        super().__init__()
