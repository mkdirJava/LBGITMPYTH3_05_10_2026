import inspect
import sys

def doit():
    pass

# Code is designed to make it look like an error occurred
# especially so because the print statements are writing to stderr
lineno = inspect.currentframe().f_lineno
code = inspect.currentframe().f_code
print(f"is doit a module? {inspect.ismodule(doit)}")
print(f"is doit a function? {inspect.isfunction(doit)}")
print(f"An error occurred on line: {lineno}", file=sys.stderr) #6
print(f"Code object: {code}", file=sys.stderr)
print(f"Raw compiled bytecode: {code.co_code}", file=sys.stderr)
