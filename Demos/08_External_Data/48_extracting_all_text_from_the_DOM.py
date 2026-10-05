import xml.dom.minidom

def getText(nodes):
    for child in nodes:
        if child.nodeType == child.TEXT_NODE:
            if not child.data.isspace():
                print(child.data)
        elif child.nodeType == child.ELEMENT_NODE:
            getText(child.childNodes)

doc = xml.dom.minidom.parse('accounts4.xml')
getText(doc.childNodes)
