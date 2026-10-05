import os
import glob

def iter_paths(path, kind="files"):
    pattern = os.path.join(path, '*')

    for item in glob.iglob(pattern):
        if kind == "files" and os.path.isfile(item):
            yield item
        elif kind == "dirs" and os.path.isdir(item):
            yield item


gen = iter_paths("./", kind="files")

fname = next(gen, False)
while fname:
    print(fname)
    fname = next(gen, False)

# You don't need a loop!
folders = []
gen = iter_paths("./", kind="dirs")
folders.append(next(gen, False))
folders.append(next(gen, False))
folders.append(next(gen, False)) 

print(folders)

