import os
data_path = os.path.join(os.path.dirname(__file__), 'data.txt')
with open(data_path, "r") as my_file:
    for line in my_file:
        print(line, end="''")

    print(my_file)

# Without with (Context manager)

try:
    my_file = open(data_path, "r")
    for line in my_file:
        print(line, end="''")

    print(my_file)
finally:
    my_file.close(); # really should remember to do this.