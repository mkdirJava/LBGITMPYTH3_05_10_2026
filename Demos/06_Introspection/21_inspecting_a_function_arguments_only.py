import inspect

def myfunc1(char, qty=10):
    return char * qty

def myfunc2(*, char, qty=10):
    return char * qty

def myfunc3(char, **kwargs):
    return char * kwargs[0]

print(inspect.getfullargspec(myfunc1))
print(inspect.getfullargspec(myfunc2))
print(inspect.getfullargspec(myfunc3))
