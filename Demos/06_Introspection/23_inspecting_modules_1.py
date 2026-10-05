import inspect, re
import pprint
import currentAccount
import math as m

for name, val in list(locals().items()):
    if inspect.ismodule(val):
        fullname = str(val)
        if not '(built-in)' in fullname:
            match = re.search(r"'(.+)'.*'(.+)'", fullname)
            module, path = match.groups()
            print(f"{name:12s} maps to {path:s}")



