"""
    ### Classes handle Searching for file/folder if exist(s)


"""

import os

class Finder:

    def __init__(self) -> None:

        self.path = ""
        self.is_recursive = None
        

    @classmethod
    def get_files(self) -> str:
        """
            Yield files in parent folder
        """

        for file in os.listdir(self.path):
            yield file

    @classmethod
    def get_files_recursive(self) -> tuple[str:str]:
        """
            Yields tuple (root, file) recursively thorugh all folders

        """
        
        for root, _, files in os.walk(self.path):

            for file in files:
                yield (root, file)


    @classmethod
    def get_folders(self):

        for file in os.listdir(self.path):
            yield file


    @classmethod
    def get_folders_recursive(self):
        
        for root, folders, _ in os.walk(self.path):

            for folder in folders:
                yield (root, folder)



class File(Finder):

    def __init__(self) -> None:
        super().__init__()

    @classmethod
    def set_path(self, path:str):

        if not os.path.exists(path):
            print("path error")
        
        self.path = path


    @classmethod
    def set_recursive(self, rec:bool):
        self.is_recursive = rec
        

    @classmethod
    def by_extention(self, extension:str) -> list:
        """
            Find files by extention
        """

        detected_files = []

        if self.is_recursive:

            for root, file in self.get_files_recursive():

                if file.endswith(f".{extension}"):
                    detected_files.append(f"{root}\{file}")
        
        else:

            for file in self.get_files():

                if file.endswith(f".{extension}"):
                    detected_files.append(file)


        return detected_files


    @classmethod
    def by_name(self, name:str) -> list:
        """
            Find files by exact name (CASE-SENSETIVE)
        """
        
        detected_files = []

        if self.is_recursive:    

            for root, file in self.get_files_recursive():

                if file[ : file.find(".")].strip() == name:
                    detected_files.append(f"{root}\{file}")
        
        else:

            for file in self.get_files():

                if file[ : file.find(".")].strip() == name:
                    detected_files.append(file)
            
        return detected_files
    
    
    @classmethod
    def by_pattern(self, name:str) -> list:
        """
            Find files by exact name (NOT CASE-SENSETIVE)
        """
        
        detected_files = []

        if self.is_recursive:    

            for root, file in self.get_files_recursive():

                if name in file:
                    detected_files.append(f"{root}\{file}")
        
        else:

            for file in self.get_files():

                if name in file:
                    detected_files.append(file)
            
        return detected_files       



class Folder(Finder):
    
    def __init__(self) -> None:
        super().__init__()


    @classmethod
    def set_path(self, path:str):

        if not os.path.exists(path):
            raise FileNotFoundError
        
        self.path = path


    @classmethod
    def set_recursive(self, rec:bool):
        self.is_recursive = rec
    
    
    @classmethod
    def by_name(self, name:str) -> list:
        """
            Find files by exact name
        """
        
        detected_folders = []

            
        if self.is_recursive:    

            for root, folder in self.get_folders_recursive():

                if folder == name:
                    detected_folders.append(f"{root}\{folder}")

        else:
            
            for folder in self.get_folders():

                if folder == name:
                    detected_folders.append(folder)

        return detected_folders
    

    @classmethod
    def pattern(self, name:str) -> list:
        """
            Find files contain the given name
        """
        
        detected_folders = []

        if self.is_recursive:    

            for root, folder in self.get_folders_recursive():

                if name in folder:

                    # Add the root before to keep track of the full path
                    detected_folders.append(f"{root}\{folder}")
        
        else:

            for folder in self.get_folders():

                if name in folder:
                    detected_folders.append(folder)
            
        return detected_folders       
