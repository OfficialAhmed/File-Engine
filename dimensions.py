import os
import cv2
from pathlib import Path

def get_video_dimensions(
    folder: str = r"F:\Videos",
    min_width: int = 720,
) -> None:
    
    folder_path = Path(folder)

    if not folder_path.is_dir():
        raise NotADirectoryError(f"{folder!r} is not a valid directory")

    # Walk through the directory (non‑recursive, like os.listdir)
    for entry in folder_path.iterdir():
        if not entry.is_file():
            continue                    

        # Try to open the file with OpenCV
        cap = cv2.VideoCapture(str(entry))
        if not cap.isOpened():
            # Not a readable video – skip silently or log if you wish
            cap.release()
            continue

        # Grab width and height from the capture properties
        width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

        cap.release()

        # Report videos that are narrower than the threshold
        if width < min_width:
            print(entry)   # prints the absolute path

# ----------------------------------------------------------------------
if __name__ == "__main__":
    get_video_dimensions()