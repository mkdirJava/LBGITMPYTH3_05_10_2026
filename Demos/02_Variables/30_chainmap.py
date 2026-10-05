from collections import ChainMap
# Three separate directories
employees = {"Alice Green": "020 7000 1234", "John Smith": "020 7000 5678",}
customers = {"Mary Brown": "01632 960111", "Tom Harris": "01632 960222",}
suppliers = {"ACME Supplies": "0141 555 2020","PaperCo": "0141 555 3030",}

# Combine them into a single searchable directory
phone_directory = ChainMap(employees, customers, suppliers)
# Look up entries
print(phone_directory["John Smith"])  # From employees
print(phone_directory["Mary Brown"])  # From customers
print(phone_directory["PaperCo"])  # From suppliers

# Adding a new employee (affects ONLY the first map)
employees["Chris Miles"] = "020 7000 9999"
print(phone_directory["Chris Miles"])

customers["George Michael"] = "020 6000 8888"
print(phone_directory["George Michael"]) # errors

# Adding a new layer — e.g., temporary contractors
contractors = {"Zara Khan": "07700 900111"}
phone_directory = phone_directory.new_child(contractors)

print(phone_directory["Zara Khan"])  # Found in the new top layer  # Fails for union of dictionaries
print(phone_directory.parents["Alice Green"])  # Underlying maps unaffected
print(phone_directory["Alice Green"])


def thing()-> str:
    return "hi"

t = thing

t()