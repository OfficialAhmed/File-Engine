
import lib.common.find as Find


class Common:

    def __init__(self) -> None:
        pass


if __name__ == "__main__":
    path = "test"
    
    # print( Find.File(path, False).by_extention("png") )
    # print( Find.File(path, True).by_name("testing") )

    print( Find.Folder(path, True).by_name("New folder") )