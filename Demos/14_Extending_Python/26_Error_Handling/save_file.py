import filesavemodule

content = "To be or not to be, that is the question. Whether tis..."
path = r"C:\temp\backupy"
filename = "shakespeare.txt"
try:
    filesavemodule.save_to_file(path, filename, content)
    print(f"Content successfully saved to path: {path}\\{filename}.")
except NotADirectoryError as e:
    print(f"{e}")
except FileNotFoundError as e:
    print(f"No such file: {e.filename}")



