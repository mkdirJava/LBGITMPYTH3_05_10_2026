import inspect, sys, re

def look():
    for name, val in list(sys._getframe(1).f_locals.items()):
        #                      ^^^^^^^^^^ inspecting the previous code frame - i.e the caller's
        #                      The _getframe(1) indicates that we wish to go back one level in the code frame stack
        if inspect.ismodule(val):
            fullname = str(val)
            if not '(built-in)' in fullname \
                and not __name__ in fullname:
                match = re.search(r"'(.+)'.*'(.+)'", fullname)
                module,path = match.groups()
                print(f"{name:12s} maps to {path:s}")
