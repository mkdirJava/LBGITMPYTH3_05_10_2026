result = 9

def scope_test1():
   result = 56

scope_test1()
print(result)

def scope_test2():
   global result
   result = 56

scope_test2()
print(result)