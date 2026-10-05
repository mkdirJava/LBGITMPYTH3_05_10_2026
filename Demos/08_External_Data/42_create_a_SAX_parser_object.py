from xml import sax
from xml.sax.handler import ContentHandler

class AccountHandler(ContentHandler):
    def __init__(self):
        self.current_element = ""
        self.accounts = []

        # Temporary storage
        self.account_id = ""
        self.account_holder = ""
        self.balance = ""
        self.overdraft_limit = ""

    def startElement(self, name, attrs):
        self.current_element = name

        if name == "account":
            # Read attribute
            self.account_id = attrs.get("account_id", "")

            # Reset values
            self.account_holder = ""
            self.balance = ""
            self.overdraft_limit = ""

    def characters(self, content):
        content = content.strip()
        if not content:
            return

        if self.current_element == "account_holder":
            self.account_holder += content
        elif self.current_element == "balance":
            self.balance += content
        elif self.current_element == "overdraft_limit":
            self.overdraft_limit += content

    def endElement(self, name):
        if name == "account":
            # Clean currency values (remove £ and convert to float)
            balance_value = float(self.balance.replace("£", ""))
            overdraft_value = float(self.overdraft_limit.replace("£", ""))

            account_data = {
                "account_id": self.account_id,
                "account_holder": self.account_holder,
                "balance": balance_value,
                "overdraft_limit": overdraft_value
            }

            self.accounts.append(account_data)
            print(account_data)

        self.current_element = ""

parser = sax.make_parser()
handler = AccountHandler() # class the implements xml.sax.handler
parser.setContentHandler(handler)
parser.parse("accounts4.xml")

