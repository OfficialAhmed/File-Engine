
import os
import json
import shutil
from constants import Path

class Mover:
    """ 
        Parent class for removing. 
        Hold the common data processing between files and folders 
    """
    
    def __init__(self) -> None:

        # MOVED CONTENT TRACKER - FOR RESTORE FEATURE
        self.moved_content = {}

    def set_mover_param(self, content_file_path: str, trash_folder_path="", method="delete") -> None:
        """
            PARAMS CANNOT BE PASSED ON INIT METHOD
        """
        self.moved_content_file = content_file_path
        self.trash_folder_path = trash_folder_path
        self.method = method

        # READ DELETED CONTENT IF EXIST
        if os.path.exists(self.moved_content_file) and os.path.getsize(self.moved_content_file) > 0:
            self.moved_content = json.load(open(self.moved_content_file))

    def empty_trash(self) -> None:
        """
            Delete all "trash" content
        """
        # TODO: REMOVE RETURN
        return
        shutil.rmtree(self.trash_folder_path)

    def dump_moved_content(self) -> None | str:

        if self.moved_content:
            with open(self.moved_content_file, "w+") as file:
                json.dump(self.moved_content, file)

    def restore_deleted(self, dest: str) -> None:
        """
            Redo moving from trash to original content's destination by reading the generated JSON
        """

        shutil.move(
            f"{Path.TRASH_PATH}{dest.replace(':', '')}",
            dest
        )

        # Reset JSON content by overwriting the file
        open(Path.TRASH_CONTENT_FILE, "w+")

    def restore_moved(self, src, dest) -> None:

        shutil.move(src, dest)

        # Reset JSON content by overwriting the file
        open(Path.MOVED_CONTENT_FILE, "w+")

    def make_trash_dir(self):

        # MAKE TRASH FOLDER IF IT DOESNT EXIST
        if not os.path.exists(self.trash_folder_path):
            os.mkdir(self.trash_folder_path)


class File(Mover):

    def __init__(self) -> None:
        super().__init__()

    def move(self, src: str, dest: str):

        try:

            if dest == "trash":

                self.make_trash_dir()

                # REMOVE ':' FROM REPLICATED DIR-TREE
                dest = self.trash_folder_path + src.replace(":", "")

                # REPLICATE THE DIR-TREE INSIDE TRASH
                os.makedirs(os.path.dirname(dest), exist_ok=True)

            else:
                dest += "/" + os.path.basename(src)

            shutil.move(src, dest)

            # KEEP TRACK OF THE MOVED CONTENT
            if self.method == "delete":
                if src not in self.moved_content.values():
                    self.moved_content[len(self.moved_content) + 1] = src

            else:
                # {src : dest} JSON FORM BEFORE MOVING
                if src not in self.moved_content:
                    self.moved_content[src] = dest

        except FileNotFoundError:
            return f"{src} -> DOESNT EXIST"

        except Exception as e:
            return str(e)

        finally:
            self.dump_moved_content()


class Folder(Mover):

    def __init__(self) -> None:
        super().__init__()

    def move(self, src: str, dest: str):

        try:

            if dest == "trash":

                self.make_trash_dir()

                # REMOVE ':' FROM REPLICATED DIR-TREE
                new_dest = self.trash_folder_path + src.replace(":", "")

                # REPLICATE THE DIR-TREE INSIDE TRASH
                os.makedirs(os.path.dirname(new_dest), exist_ok=True)

            else:
                new_dest = f"{dest}/{os.path.basename(src)}"

            return

            # IF FOLDER EXIST COPY FILES MANUALLY,
            # ELSE MOVE THE ENTIRE FOLDER
            if os.path.exists(new_dest):

                for file in os.listdir(src):
                    shutil.move(
                        f"{src}/{file}",
                        f"{new_dest}/{file}"
                    )
                shutil.rmtree(src)

            else:
                shutil.move(src, new_dest)

            # KEEP TRACK OF THE MOVED CONTENT
            if self.method == "delete":
                if src not in self.moved_content.values():
                    self.moved_content[len(self.moved_content) + 1] = src

            else:
                # {src : dest} JSON FORM BEFORE MOVING
                if src not in self.moved_content:
                    self.moved_content[src] = new_dest

        except Exception as e:
            return str(e)

        finally:
            self.dump_moved_content()
