from abc import abstractmethod
class Command:
    @abstractmethod
    def execute(self):
        pass

# Concrete Commands
# Create Folder
class CreateFolderCommand(Command):
    def __init__(self, fs, path):
        self.fs = fs
        self.path = path

    def execute(self):
        self.fs.create_folder(self.path)

# Create File
class CreateFileCommand(Command):
    def __init__(self, fs, filename):
        self.fs = fs
        self.filename = filename

    def execute(self):
        self.fs.create_file(self.filename)

# Move File
class MoveFileCommand(Command):
    def __init__(self, fs, src, dest):
        self.fs = fs
        self.src = src
        self.dest = dest

    def execute(self):
        self.fs.move_file(self.src, self.dest)

# Rename File
class RenameFileCommand(Command):
    def __init__(self, fs, src, new_name):
        self.fs = fs
        self.src = src
        self.new_name = new_name

    def execute(self):
        self.fs.rename_file(self.src, self.new_name)