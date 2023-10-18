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

        # REMOVED CONTENT TRACKER - FOR RESTORE FEATURE
        self.removed_counter = 0
        self.removed_content = {}

    def set_remover_param(self, content_file_path: str, trash_folder_path: str) -> None:
        """
            * Update init variables
            * Create trash folder, if doesnt exist
            * Check trash content file, if exists
        """
        self.trash_folder_path = trash_folder_path
        self.trash_content_file = content_file_path

        # MAKE TRASH FOLDER IF IT DOESNT EXIST
        if not os.path.exists(self.trash_folder_path):
            os.mkdir(self.trash_folder_path)

        if os.path.exists(self.trash_content_file) and os.path.getsize(self.trash_content_file) > 0:
            self.removed_content = json.load(open(self.trash_content_file))

    def empty_trash(self) -> None:
        """
            Delete all "trash" content
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
                param 'folder_name' must be empty

            * Folders:
                Both params required
        """

        try:

            # REMOVE ':' FROM PATH
            # CONCATENATION WITHOUT FILE NOR FOLDER NAME
            dest_with_filename = self.trash_folder_path + \
                source.replace(":", "")
            dest = os.path.dirname(dest_with_filename)

            # REPLICATE THE DIR-TREE INSIDE TRASH
            os.makedirs(dest, exist_ok=True)

            if not folder_name:

                shutil.move(source, dest_with_filename)

            else:

                # IF FOLDER EXIST COPY FILES MANUALLY,
                # ELSE MOVE THE ENTIRE FOLDER
                if os.path.exists(f"{dest}\\{folder_name}"):

                    for file in os.listdir(source):
                        shutil.move(f"{source}\\{file}",
                                    f"{dest_with_filename}")
                    shutil.rmtree(source)

                else:
                    shutil.move(source, dest_with_filename)

            # KEEP TRACK OF THE REMOVED CONTENT
            if source not in self.removed_content.values():
                self.removed_content[len(self.removed_content) + 1] = source

            self.removed_counter += 1

        except Exception as e:
            print(str(e))

    def restore(self, destination: str) -> None:
        """
            Redo moving from trash to original content's destination by reading the generated JSON
            * return total content restored
        """

        if not os.path.exists(self.trash_content_file):
            print("Restore not available. Content file not found")
            return

        shutil.move(
            f"{self.trash_folder_path}{destination.replace(':', '')}",
            destination
        )

        # Reset JSON content by overwriting the file
        open(self.trash_content_file, "w+")
        self.removed_content = {}

    def get_removed_content_count(self) -> int:
        return self.removed_counter

    def reset_removed_content_count(self) -> None:
        self.removed_counter = 0


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
