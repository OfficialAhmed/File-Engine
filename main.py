
import shutil
import lib.move as Move
import lib.delete as Delete
import lib.common.find as Finder

class Common:

    def __init__(self) -> None:
        self.file_finder = Finder.File
        self.folder_finder = Finder.Folder
        self.current_path = "test"
        
    def move_file(self, source:str, destination:str) -> None:
        shutil.move(source, destination)


if __name__ == "__main__":

    # Move.File().by_extension("txt")
    Delete.File().by_name_contains("testing")
