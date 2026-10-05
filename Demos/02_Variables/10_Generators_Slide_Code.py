import os
import glob

def get_files(path):
    pattern = os.path.join(path, '*')
    for item in glob.iglob(pattern):
        if os.path.isfile(item):
            yield item

for file in get_files('./'):
    print(file)

def iter_paths(path, kind="files"):
    pattern = os.path.join(path, '*')

    for item in glob.iglob(pattern):
        if kind == "files" and os.path.isfile(item):
            yield item
        elif kind == "dirs" and os.path.isdir(item):
            yield item

# def iter_paths(path, kind="files"):
#     pattern = os.path.join(path, '*')
#     if kind == "files":
#         for item in glob.iglob(pattern):
#             if os.path.isfile(item):
#                 yield item
#     elif kind == "dirs":
#         for item in glob.iglob(pattern):
#             if os.path.isdir(item):
#                 yield item

# def iter_paths(path, kind="files"):
#     pattern = os.path.join(path, '*')
#     if kind == "files":
#         return (item for item in glob.iglob(pattern)
#             if os.path.isfile(item))
#     elif kind == "dirs":
#         return (item for item in glob.iglob(pattern)
#             if os.path.isdir(item))

for f in iter_paths("./", kind="files"):
    print("FILE:", f)

dirs = list(iter_paths("./", kind="dirs"))
print(dirs)

