import xml.etree.ElementTree as ET
tree = ET.parse('accounts2.xml')
root = tree.getroot()

for account in root.findall('account'):
    for item in account:
        print(item.tag, ":", item.text)
