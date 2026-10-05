from lxml import etree
xml_file = "accounts4.xml"
dtd_file = "accounts4.dtd"
tree = etree.parse(xml_file)
root = tree.getroot()
dtd = etree.DTD(dtd_file)
if dtd.validate(root):
    print (f"XML in {xml_file} is valid")
else:
    # Display most recent DTD error from log
    print(dtd.error_log.last_error)

