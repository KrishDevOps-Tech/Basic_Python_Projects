# Organizer for files in folder.

import os
import shutil

# Categories aur unke extensions
CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar"],
    "Scripts": [".py", ".html", ".css", ".js", ".cpp"],
}

# # # 1. Pehla loop: Category aur uski list nikalni hai
# EXT_MAP = {}
# for cat, extensions in CATEGORIES.items():
#     # 2. Doosra loop: List ke andar se ek-ek extension nikalega
#     for ext in extensions:
#         # 3. Nayi dictionary me daal dega yeh line of code.
#         EXT_MAP[ext] = cat

# O(1) Quick lookup map
EXT_MAP = {ext: cat for cat, extensions in CATEGORIES.items() for ext in extensions}


def organize():
    print("=" * 45)
    print("           FILE ORGANIZER TOOL               ")
    print("=" * 45)

    # 1. Path input (quotes aur spaces dono saaf honge)
    raw_path = input("Folder ka path daalo: ").strip().strip('"').strip("'")

    if not raw_path:
        print("Path khali nahi ho sakta!")
        return

    if not os.path.isdir(raw_path):
        print(f"Error: Yeh valid folder nahi hai -> {raw_path}")
        return

    # Is script ka apna path (taaki script khud ko move na kar le)
    current_script = os.path.abspath(__file__)

    moved_count = 0
    skipped_count = 0

    print("\nSorting shuru ho rahi hai...\n")

    for item in os.listdir(raw_path):
        source_path = os.path.join(raw_path, item)

        # Folders, hidden files (.git vagera), ya khud script ko chhedna nahi hai
        if (
            os.path.isdir(source_path)
            or item.startswith(".")
            or os.path.abspath(source_path) == current_script
        ):
            continue

        # Extension nikalo
        name, ext = os.path.splitext(item)
        category = EXT_MAP.get(ext.lower(), "Others")

        # Destination folder banao agar nahi hai
        dest_folder = os.path.join(raw_path, category)
        os.makedirs(dest_folder, exist_ok=True)

        # Same naam ki file already ho toh _1, _2 lagao (Collision handle)
        dest_file = os.path.join(dest_folder, item)
        counter = 1
        while os.path.exists(dest_file):
            new_name = f"{name}_{counter}{ext}"
            dest_file = os.path.join(dest_folder, new_name)
            counter += 1

        # File ko move karo
        try:
            shutil.move(source_path, dest_file)
            print(f"Moved: {item}  -->  {category}/")
            moved_count += 1
        except Exception as e:
            print(f"Skipped ({item}): {e}")
            skipped_count += 1

    print("\n" + "=" * 45)
    print(f"Done! {moved_count} files sorted, {skipped_count} and skip also.")
    print("=" * 45)


if __name__ == "__main__":
    organize()
