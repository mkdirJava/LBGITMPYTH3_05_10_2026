import xml.etree.ElementTree as ET
tree = ET.parse('accounts3.xml')
root = tree.getroot()

account1 = root[0]
limit = ET.SubElement(account1, 'overdraft_limit', {})
limit.text = '£500.00'

for item in account1.iter():
    print(item.text)

account2 = root[1]
account2[1].text = '£12.07'
for item in account2.iter():
    print(item.text)

tree.write('newaccounts.xml',
           encoding='UTF-8',
           xml_declaration=True)
