import os
import glob

# The original
def original_iter_paths(path, kind="files"):
    pattern = os.path.join(path, '*')
    if kind == "files":
        for item in glob.iglob(pattern):
            if os.path.isfile(item):
                yield item
    elif kind == "dirs":
        for item in glob.iglob(pattern):
            if os.path.isdir(item):
                yield item

for f in original_iter_paths("./", kind="files"):
    print("FILE:", f)

dirs = list(original_iter_paths("./", kind="dirs"))
print(dirs)

# New version with generator expression
def iter_paths(path, kind="files"):
    pattern = os.path.join(path, '*')
    if kind == "files":
        return (item for item in glob.iglob(pattern) if os.path.isfile(item))
    elif kind == "dirs":
        return (item for item in glob.iglob(pattern) if os.path.isdir(item))

for f in iter_paths("./", kind="files"):
    print("FILE:", f)

dirs = list(iter_paths("./", kind="dirs"))
print(dirs)
