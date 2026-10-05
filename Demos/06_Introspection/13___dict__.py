import currentAccount
import pprint

pprint.pprint(currentAccount.__dict__)
print("*************************************************")
pprint.pprint(currentAccount.CurrentAccount.__dict__)
print("*************************************************")
ca = currentAccount.CurrentAccount() # Error
pprint.pprint(ca.__dict__)