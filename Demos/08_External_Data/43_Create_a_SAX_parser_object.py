from xml import sax
from xml.sax.handler import ContentHandler

inAccount = 0

class AccountHandler (sax.handler.ContentHandler):
    def __init__(self):
        self.text = ''

    def startElement(self, name, attributes):
        global inAccount
        self.tag = name
        if attributes.items():
            print(attributes.items())
        if name == 'account':
            inAccount= True
            self.elems = {}

    def characters(self, data):
        if not data.isspace():
            self.text += data

    def endElement(self, name):
        global inAccount
        if inAccount and not name  == 'account':
            self.elems[name] = self.text
        elif inAccount and name == 'account':
                inAccount = False
                for k,v in self.elems.items():
                    print(k.ljust(15),":",v)
        if self.text:
            self.text = self.tag = ''

parser = sax.make_parser()
handler = AccountHandler() # class the implements xml.sax.handler
parser.setContentHandler(handler)
parser.parse("accounts4.xml")
