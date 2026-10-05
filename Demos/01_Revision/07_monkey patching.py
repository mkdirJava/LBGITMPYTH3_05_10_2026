# Monkey patching
# Replacing or adding attributes (usually methods) at runtime

# Can be done by accident
#len = 42
var = 56
x = "A piece of text"
if var > len(x):
    print("var is bigger the length of x!")

# sometimes by design
import sys
realout = sys.stdout
err_file = open("my_dialog.log", "a") # printed output will temporarily be redirected to the file
sys.stdout = err_file
print("This is a test", flush=True)
sys.stdout = realout
