# from a string:
import xml.dom.minidom
text = "<account><account_holder>Alice Johnson</account_holder><balance>2540.75</balance></account>"
doc = xml.dom.minidom.parseString(text)
print(doc.childNodes)
print(doc.firstChild.tagName)

print("***********************************************")

# from a file or file object
import xml.dom.minidom
doc = xml.dom.minidom.parse('accounts2.xml')

# creates a DOM object root node with child nodes
print(doc.childNodes)
print(doc.firstChild.tagName)
