"""
    ### Classes handle removing for file/folder
    
    Deleting is simply moving files to a temp folder 'Trash' before completely erasing it from the computer.
    Upon user permission and confirmation -> Empty trash folder
    
"""

import os, json
import shutil
from main import Common


    
class Engine(Common):
    """ 
        Parent class for removing. 
        Hold the common data processing between files and folders 
    """

    def __init__(self) -> None:
        super().__init__()

        self.create_trash()

        # Removed content tracker -> For restoring feature
        self.removed_content = {}

        if os.path.exists(self.trash_content_file):
            
            try:
                self.removed_content = json.load(open(self.trash_content_file))
            
            # JSON exists but empty 
            except json.decoder.JSONDecodeError:
                pass


    def create_trash(self) -> None:
        """
            Make trash if it doesnt exist
        """

        if not os.path.exists(self.trash_folder_path):
            os.mkdir(self.trash_folder_path)


    def empty_trash(self) -> None:
        """
            Delete all content in the "trash" folder
        """

        for file in os.listdir(self.trash_folder_path):
            os.remove(file)


    def dump_trash_content(self, content:dict) -> None:
        """
            Store deleted content information as json
        """

        if content:
            with open(self.trash_content_file, "w+") as file:
                json.dump(content, file)


    def move(self, source:str, folder_name:str = "") -> None:
        """
            Store content in trash
        """
        
        try:
            
            if not folder_name:

                file_destination = "\\".join(source.split("\\")[:-1])

                # Replicate the directory tree inside trash before moving the file
                os.makedirs(f"{self.trash_folder_path}{file_destination}", exist_ok=True)
                shutil.move(source, f"{self.trash_folder_path}{file_destination}")

            # If folder is selected, check existence before moving
            if not os.path.exists(self.trash_folder_path+f"{folder_name}"):
                shutil.move(source, f"{self.trash_folder_path}{source}")


            # Keep track of the removed content
            total_content = len(self.removed_content) + 1
            self.removed_content[total_content] = source

        except Exception as e: print(str(e))
        

    def restore(self) -> None:
        """
            Redo moving from trash to original content's destination by reading the generated JSON
        """

        if not os.path.exists(self.trash_content_file):
            
            print("Restore not available. Content file not found")
            return

        data:dict = json.load(open(self.trash_content_file))

        for destination in data.values():
            
            shutil.move(
                f"{self.trash_folder_path}{destination}", 
                destination
            )

        # Reset JSON content by overwriting the file
        open(self.trash_content_file, "w+")


class File(Engine):

    def __init__(self) -> None:
        super().__init__()


    def by_extension(self, extension:str) -> None:
        """
            Move the files with the provided extension 
        """

        for file in self.file_finder(self.current_path).by_extention(extension):  
            self.move(file)
        self.dump_trash_content(self.removed_content)


    def by_name(self, name:str) -> None:
        """
            Move files with exact file name
        """

        for file in self.file_finder(self.current_path).by_name(name):
            self.move(file)
        self.dump_trash_content(self.removed_content)

    
    def by_name_contains(self, name:str) -> None:
        """
            Move files contain the provided name
        """

        for file in self.file_finder(self.current_path).by_name_contains(name):
            self.move(file)
        self.dump_trash_content(self.removed_content)



class Folder(Engine):
    
    def __init__(self) -> None:
        super().__init__()


    def by_name(self, name:str) -> None:
        """
            Move folders with exact name
        """

        for folder in self.folder_finder(self.current_path).by_name(name):
            self.move(folder, folder)
        self.dump_trash_content(self.removed_content)

    
    def by_name_contains(self, name:str) -> None:
        """
            Move folders contain the provided name
        """

        for folder in self.folder_finder(self.current_path).by_name_contains(name):
            self.move(folder, folder)
        self.dump_trash_content(self.removed_content)
