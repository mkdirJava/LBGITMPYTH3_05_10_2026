from xml.parsers import expat
import sys

Tags = 0
def count_tags(name, attr): global Tags; Tags += 1

ExParser = expat.ParserCreate()
ExParser.StartElementHandler = count_tags

try:
    ExParser.ParseFile(open('books.xml', 'rb'))
except expat.ExpatError:
    print("Error!", file=sys.stderr)
    exit(1)
else:
    print("XML is well-formed and has", Tags, "tags")
