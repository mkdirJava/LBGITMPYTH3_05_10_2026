import sys

def add_ctxmgr(cls):
    def enterf(self):
        return self

    def exitf(self, exc_type, exc_value, tb):
        if tb:
            print("Error from line:", tb.tb_lineno,
                  file=sys.stderr)
            return True
        else:
            return False

    cls.__enter__ = enterf
    cls.__exit__ = exitf

    return cls


@add_ctxmgr
class SomeClass:
    ...

with SomeClass(...) as var:
    print(var)
