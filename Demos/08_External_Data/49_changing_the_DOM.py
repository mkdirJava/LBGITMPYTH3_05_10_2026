import xml.dom.minidom
doc = xml.dom.minidom.parse('accounts4.xml')

for account in doc.getElementsByTagName('account'):
    bal = account.removeChild(account.getElementsByTagName('balance')[0])
    account.insertBefore(bal, account.lastChild)

    balance = account.childNodes[5].firstChild
    balance.data = '£12.00'
    for child in account.childNodes:
        if child.nodeType == account.ELEMENT_NODE:
            print(f"{child.nodeName}: ", end="")
            for detail in child.childNodes:
                print(detail.data)

