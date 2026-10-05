from observerinterface import Observer

class SMSAlert(Observer):
    def update(self, account):
        print(f"[SMS] Alert: Balance is now £{account.balance}")

class EmailAlert(Observer):
    def update(self, account):
        print(f"[Email] Alert: Balance updated to £{account.balance}")