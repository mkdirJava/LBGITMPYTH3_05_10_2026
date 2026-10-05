result = 9

def my_func():
    result = 36

    def scope_test():
        nonlocal result
        if result < 40:
            result += 1
            scope_test()

    scope_test()
    print(result, "from my_func")

my_func()
print(result, "from main")
