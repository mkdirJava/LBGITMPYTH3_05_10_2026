from bankaccount import BankAccount
from concreteobservers import SMSAlert
from concreteobservers import EmailAlert

account = BankAccount("Peter", 1000)

sms_alert = SMSAlert()
email_alert = EmailAlert()

# Attach observers
account.attach(sms_alert)
account.attach(email_alert)

# Perform transactions
account.deposit(200)
account.withdraw(150)

# Detach observers
account.detach(sms_alert)
account.detach(email_alert)

# Perform transactions
account.deposit(400)
account.withdraw(250)