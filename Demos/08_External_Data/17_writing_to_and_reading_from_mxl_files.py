from xml.etree.ElementTree import Element, SubElement, ElementTree

accounts = {
    "ACC45678": {
        "account_holder": "Alice Johnson",
        "balance": 2540.75
    },
    "ACC45679": {
        "account_holder": "Sadia Saleem",
        "balance": 342.76
    }
}

# Create root element
root = Element("accounts")

# Add each account
for account_number, details in accounts.items():
    account_elem = SubElement(root, "account")
    account_elem.set("id", account_number)

    for key, value in details.items():
        child = SubElement(account_elem, key)
        child.text = str(value)

# Write XML to file
tree = ElementTree(root)
tree.write("accounts.xml", encoding="utf-8", xml_declaration=True)


import xml.etree.ElementTree as ET

# Read XML file
tree = ET.parse("accounts.xml")
root = tree.getroot()

# Create CSV string
csv_string = "account_number,account_holder,balance\n"

for account in root.findall("account"):
    account_number = account.get("id")
    account_holder = account.find("account_holder").text
    balance = account.find("balance").text

    csv_string += (
        f"{account_number},"
        f"{account_holder},"
        f"{balance}\n"
    )

print(csv_string)

