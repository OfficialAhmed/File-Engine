"""
    ### Classes handle removing for file/folder
    
    Deleting is simply moving files to a temp folder 'Trash' before completely erasing it from the computer.
    Upon user permission and confirmation -> Empty trash folder
    
"""

import os
import json
import shutil


class Remover:
    """ 
        Parent class for removing. 
        Hold the common data processing between files and folders 
    """

    def __init__(self) -> None:

        # UPDATED BY CALLER WHEN INIT
        self.trash_folder_path = None
        self.trash_content_file = None

        self.__removed_content_count = 0

        # Removed content tracker -> For restoring feature
        self.removed_content = {}

    def set_remover_param(self, content_file_path: str, trash_folder_path: str) -> None:
        """
            * Update init variables
            * Create trash folder, if doesnt exist
            * Check trash content file, if exists
        """
        self.trash_folder_path = trash_folder_path
        self.trash_content_file = content_file_path

        self._create_trash()

        if os.path.exists(self.trash_content_file):

            try:
                self.removed_content = json.load(open(self.trash_content_file))

            # JSON exists but empty
            except json.decoder.JSONDecodeError:
                pass

    def _create_trash(self) -> None:
        """
            Make trash if it doesnt exist
        """

        if not os.path.exists(self.trash_folder_path):
            os.mkdir(self.trash_folder_path)

    def empty_trash(self) -> None:
        """
            Delete all content in the "trash" folder
        """

        shutil.rmtree(self.trash_folder_path)

    def dump_trash_content(self, content: dict) -> None:
        """
            Store deleted content information as json
        """

        if content:
            with open(self.trash_content_file, "w+") as file:
                json.dump(content, file)

    def move(self, source: str, folder_name: str = "") -> None:
        """
            ### Store content in trash folder

            * Files:
                param 'folder_name' should be empty

            * Folders:
                Both params required
        """

        try:

            # File is selected to be moved
            if not folder_name:
                
                # REMOVE ':' FROM PATH
                # CONCATENATE WITH '\\' WITHOUT THE FILE NAME
                file_destination = self.trash_folder_path + \
                    "\\".join(
                        source.replace(
                            ":", ""
                        ).split("\\")[:-1]
                    )

                # Replicate the directory tree inside trash before moving the file
                os.makedirs(file_destination, exist_ok=True)
                shutil.move(source, file_destination)

            # If folder is selected, check existence before moving
            if not os.path.exists(f"{self.trash_folder_path}{folder_name}"):
                shutil.move(source, f"{self.trash_folder_path}{source}")

            # Keep track of the removed content
            self.removed_content[len(self.removed_content) + 1] = source
            self.__removed_content_count += 1

        except Exception as e:
            print(str(e))

    def restore(self) -> None:
        """
            Redo moving from trash to original content's destination by reading the generated JSON
        """

        if not os.path.exists(self.trash_content_file):

            print("Restore not available. Content file not found")
            return

        data: dict = json.load(open(self.trash_content_file))

        for destination in data.values():

            shutil.move(
                f"{self.trash_folder_path}{destination}",
                destination
            )

        # Reset JSON content by overwriting the file
        open(self.trash_content_file, "w+")

    def get_removed_content_count(self) -> int:
        return self.__removed_content_count


class File(Remover):

    def __init__(self) -> None:
        super().__init__()

    def remove(self, file_path: str):
        self.move(file_path)
        self.dump_trash_content(self.removed_content)


class Folder(Remover):

    def __init__(self) -> None:
        super().__init__()

    def remove(self, folder_path: str, folder_name: str):
        self.move(folder_path, folder_name)
        self.dump_trash_content(self.removed_content)

