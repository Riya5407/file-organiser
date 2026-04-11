import os
import shutil

def get_unique_filename(folder_path, filename):
    name, ext = os.path.splitext(filename)
    counter = 1
    new_filename = filename
    while os.path.exists(os.path.join(folder_path, new_filename)):
        new_filename = f"{name}_{counter}{ext}"
        counter += 1
    return new_filename

def move_file(src, dest_folder, filename):
    try:
        os.makedirs(dest_folder, exist_ok=True)

        new_filename = get_unique_filename(dest_folder, filename)

        if new_filename != filename:
            print(f"Renamed: {filename} -> {new_filename}")
        
        shutil.move(src, os.path.join(dest_folder, new_filename))
        print(f"Moved: {filename} -> {dest_folder}")
    
    except Exception as e:
        print(f"Error moving {filename}: {e}")

def organize_folder(folder_path):

    file_types = {
        "Images" : [".jpg", ".jpeg", ".png", ".gif"],
        "Documents" : [".pdf", ".docx", ".txt"],
        "Videos" : [".mp4", ".avi", ".mkv"],
        "Audio" : [".mp3", ".wav", ".aac"],
        "Archives" : [".zip", ".rar", ".tar", ".gz"],
        "Scripts" : [".py", ".js", ".sh"],
        "Spreadsheets" : [".xlsx", ".csv"],
        "Presentations" : [".pptx", ".ppt"]
        }
    
    files = os.listdir(folder_path)

    for file in files:
        if file.startswith('.'):
            continue

        file_path = os.path.join(folder_path, file)

        if not os.path.isfile(file_path):
            continue

        extension = os.path.splitext(file)[1].lower()
        moved = False

        for folder, extensions in file_types.items():
                if extension in extensions:
                    target_folder = os.path.join(folder_path, folder)
                    move_file(file_path, target_folder, file)
                    moved = True
                    break
        if not moved:
            other_folder = os.path.join(folder_path, "Others")
            move_file(file_path, other_folder, file)


if __name__ == "__main__":
    folder_path = input("Enter the path of the folder you want to organize: ").strip()
    if not os.path.exists(folder_path):
        print("Invalid Path.")
    else:
        organize_folder(folder_path)