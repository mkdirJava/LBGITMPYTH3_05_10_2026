import xml.dom.minidom
doc = xml.dom.minidom.parse('accounts2.xml')

for node in doc.childNodes:
    if node.nodeType == doc.ELEMENT_NODE:
        print(node.nodeName, "\n", node.childNodes)

# or use properties of the element nodes
account1 = doc.firstChild.firstChild.nextSibling
print(account1.childNodes[1:-1:2])
