class Thing():
    who_am_I = ("I'm a thing")

    def lets_do_it(self):
        print("We are doing it!")

def do_something():
    print("I'm doing something")

print(locals())
print("*"*30)
print(globals())

print(eval('37'))  # 37
print(exec('37'))  # None

print(exec('if True: print(37)')) # 37 then None on next line
print(eval('if True: print(37)')) # SyntaxError: invalid syntax


