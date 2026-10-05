from lxml import etree # ignore error: Cannot find reference 'etree' in '__init__.py'
dtdparser = etree.XMLParser(dtd_validation=True)
tree = etree.parse('accountsdtd.xml', dtdparser)
root = tree.getroot()

