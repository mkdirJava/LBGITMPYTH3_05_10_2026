import xml.dom.minidom
doc = xml.dom.minidom.parse('accounts4.xml')

for account in doc.getElementsByTagName('account'):

    print(account.getAttributeNode('account_id').nodeValue)

    for child in account.childNodes:
        if child.nodeType == account.ELEMENT_NODE:
            for detail in child.childNodes:
                print(detail.data)
