import myminimalmodule

print(myminimalmodule.hello_world.__doc__) # doc string
print(myminimalmodule.hello_world) # type
print(callable(myminimalmodule.hello_world))

myminimalmodule.hello_world()