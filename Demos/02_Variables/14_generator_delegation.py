import os
import glob


def _iter_dirs(path):
    """Sub-generator: yields directory paths, and count."""
    pattern = os.path.join(path, '*')
    count = 0
    for item in glob.iglob(pattern):
        if os.path.isdir(item):
            count += 1
            yield item
    return count


def list_dirs(path):
    """Delegating generator: wraps _iter_dirs with a header/footer and
    captures its return value via the `yield from` expression."""
    yield f"Scanning {path}..."
    total = yield from _iter_dirs(path)
    yield f"Found {total} director{'y' if total == 1 else 'ies'}."


if __name__ == "__main__":
    for line in list_dirs('.'):
        print(line)

import os
import glob

def iter_paths(path, kind="files"):
    pattern = os.path.join(path, '*')

    def _iter_files():
        for item in glob.iglob(pattern):
            if os.path.isfile(item):
                yield item

    def _iter_dirs():
        for item in glob.iglob(pattern):
            if os.path.isdir(item):
                            yield item

    if kind == "files":
        yield from _iter_files()
    elif kind == "dirs":
        yield from _iter_dirs()

for f in iter_paths("./", kind="files"):
    print("FILE:", f)

dirs = list(iter_paths("./", kind="dirs"))
print(dirs)


