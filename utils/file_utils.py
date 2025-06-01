import os
import shutil

def get_media_files(folder):
    return [os.path.join(folder, f) for f in os.listdir(folder)
            if f.lower().endswith(('.jpg', '.jpeg', '.png', '.mp4', '.mov', '.gif'))]

def move_file_to_category(file_path, categories, dest_root):
    for category in categories:
        dest_dir = os.path.join(dest_root, category)
        os.makedirs(dest_dir, exist_ok=True)
        shutil.copy(file_path, dest_dir)
        print(f"Copied to {dest_dir}: {file_path}")
