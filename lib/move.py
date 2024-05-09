
import os
import json
import shutil


class Mover:
    """ 
        Parent class for removing. 
        Hold the common data processing between files and folders 
    """

    def __init__(self) -> None:

        # UPDATED BY CALLER WHEN INIT
        self.trash_folder_path = None
        self.trash_content_file = None

        # MOVED CONTENT TRACKER - FOR RESTORE FEATURE
        self.moved_content = {}

    def set_mover_param(self, content_file_path: str, trash_folder_path: str) -> None:
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

        # READ MOVED CONTENT IF EXIST
        if os.path.exists(self.trash_content_file) and os.path.getsize(self.trash_content_file) > 0:
            self.moved_content = json.load(open(self.trash_content_file))

    def empty_trash(self) -> None:
        """
            Delete all "trash" content
        """

        shutil.rmtree(self.trash_folder_path)

    def move_to(self, src: str, dest: str, folder_name: str = "") -> None | str:
        """
            ### Store content in trash folder

            * Files:
                param 'folder_name' must be empty

            * Folders:
                Both params required
        """

        try:

            # MOVE DIRECTLY TO TRASH
            if dest.lower() == "trash":

                # REMOVE ':' FROM PATH
                # CONCATENATION WITHOUT FILE NOR FOLDER NAME
                dest_with_filename = self.trash_folder_path + \
                    src.replace(":", "")
                dest = os.path.dirname(dest_with_filename)

            else:
                dest_with_filename = dest + src.replace(":", "")

            # REPLICATE THE DIR-TREE INSIDE TRASH
            os.makedirs(dest, exist_ok=True)

            if not folder_name:
                shutil.move(src, dest_with_filename)

            else:

                # IF FOLDER EXIST COPY FILES MANUALLY,
                # ELSE MOVE THE ENTIRE FOLDER
                if os.path.exists(f"{dest}\\{folder_name}"):

                    for file in os.listdir(src):
                        shutil.move(
                            f"{src}\\{file}",
                            f"{dest_with_filename}"
                        )
                    shutil.rmtree(src)

                else:
                    shutil.move(src, dest_with_filename)

            # KEEP TRACK OF THE MOVED CONTENT
            if src not in self.moved_content.values():
                self.moved_content[len(self.moved_content) + 1] = src

        except FileNotFoundError:
            return f"{src} -> DOESNT EXIST"

        except Exception as e:
            return str(e)

        finally:

            # DUMP CONTENT IF AVAILABLE TO JSON
            if self.moved_content:
                with open(self.trash_content_file, "w+") as file:
                    json.dump(self.moved_content, file)

    def restore(self, destination: str) -> None:
        """
            Redo moving from trash to original content's destination by reading the generated JSON
            * return total content restored
        """

        shutil.move(
            f"{self.trash_folder_path}{destination.replace(':', '')}",
            destination
        )

        # Reset JSON content by overwriting the file
        open(self.trash_content_file, "w+")
        self.moved_content.clear()


class File(Mover):

    def __init__(self) -> None:
        super().__init__()


class Folder(Mover):

    def __init__(self) -> None:
        super().__init__()
