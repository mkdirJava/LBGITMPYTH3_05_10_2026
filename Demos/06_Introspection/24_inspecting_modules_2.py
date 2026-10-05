import spection
import re
import pprint
import sys

for name, val in list(sys._getframe(1).f_locals.items()):
    if inspect.ismodule(val):
        fullname = str(val)
        if not '(built-in)' in fullname and not __name__ in fullname:
            match = re.search(r"'(.+)'.*'(.+)'", fullname)
            module, path = match.groups()
            print(f"{name:12s} maps to {path:s}")

spection.look()

x = re.search
pprint.pprint(x)