def print_greeting(name: str):
    print(name)


def print_greeting(name: str) -> None:
    print(name)

print_greeting("Ada")


def print_greeting(name: str) -> None:
    print(name)
    return 0

print_greeting("Ada")