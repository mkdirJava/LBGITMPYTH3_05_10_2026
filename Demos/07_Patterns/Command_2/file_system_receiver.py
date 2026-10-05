import os
import shutil

class FileSystem:
    def create_folder(self, path):
        os.makedirs(path, exist_ok=True)
        print(f"Created folder: {path}")

    def create_file(self, filename):
        full_path = os.path.join(os.path.curdir, filename)
        # Create the file (and write content if provided)
        with open(full_path, "w") as f:
            f.write("# TRANSACTIONS")
        print(f"Created file: {full_path}")


    def move_file(self, src, dest):
        shutil.move(src, dest)
        print(f"Moved file from {src} to {dest}")

    def rename_file(self, src, new_name):
        directory = os.path.dirname(src)
        new_path = os.path.join(directory, new_name)
        os.rename(src, new_path)
        print(f"Renamed file to {new_path}")
        return new_path