
import inspect

def example_function():
    x = 10
    frame = inspect.currentframe()

    print("Current line:", frame.f_lineno)
    print("Local variables:", frame.f_locals)
    print("Function name:", frame.f_code.co_name)

example_function()

# prints:
# Current line: 6
# Local variables: {'x': 10, 'frame': <frame object>}
# Function name: example_function

print("*************************************")

# Frames and the call stack
def outer():
    inner()
    # import inspect
    # frame = inspect.currentframe()
    # print("In Outer: Current function:", frame.f_code.co_name)
    # print("In Outer: Caller function:", frame.f_back.f_code.co_name)

def inner():
    import inspect
    frame = inspect.currentframe()
    print("Current function:", frame.f_code.co_name)
    print("Caller function:", frame.f_back.f_code.co_name)

outer()
