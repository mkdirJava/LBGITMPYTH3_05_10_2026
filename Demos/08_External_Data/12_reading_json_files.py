import json

with open('accounts.json') as accounts_file:
    accounts = json.load(accounts_file)
    for account in accounts['accounts']['account']:
        print('account_holder:', account['account_holder'])
        print('account_number:', account['account_number'])
        print('balance:', account['balance'])
