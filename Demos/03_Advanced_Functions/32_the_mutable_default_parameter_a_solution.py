def add_to_new_list(name, new_list=None):
    if new_list is None:
        new_list = []
    new_list.append(name)
    return new_list

print(add_to_new_list("Hamza"))
print(add_to_new_list("Sadia"))
print(add_to_new_list("Kate"))