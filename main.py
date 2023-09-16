
import lib.move as Move
import lib.delete as Delete
import lib.common.find as Finder

class Common:

    # Static objects
    FILE_FINDER = Finder.File
    FOLDER_FINDER = Finder.Folder


    def __init__(self) -> None:
        self.file_finder:Finder.File = self.get_file_finder()
        self.folder_finder:Finder.Folder = self.get_folder_finder()
        self.current_path = "test"
        self.trash_folder_path = "trash\\"

        self.trash_content_file = f"{self.trash_folder_path}content.json"
        
    
    def get_file_finder(self) -> Finder.File:
        return Common.FILE_FINDER

    def get_folder_finder(self) -> Finder.Folder:
        return Common.FOLDER_FINDER


if __name__ == "__main__":

    """
        Library testing
        to be removed 
    """
    
    remove_folder = Delete.Folder()

    remove_folder.by_name_contains("New")
    print(remove_folder.get_removed_content_count())
    # remove_folder.restore()
    # remove_folder.empty_trash()
