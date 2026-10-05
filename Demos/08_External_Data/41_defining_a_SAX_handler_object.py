import xml.sax.handler

class AccountHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self.text = ''

    def startElement(self, name, attributes):
        self.tag = name
        if attributes.items():
            print(attributes.items())

    def characters(self, data):
        if not data.isspace(): self.text += data

    def endElement(self, name):
        if self.text:
            print(self.tag,':',self.text)
            self.text = self.tag = ''
