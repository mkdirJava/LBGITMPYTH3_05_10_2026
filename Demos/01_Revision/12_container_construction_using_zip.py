amounts = [1250.50, 300.00, 999.99, 42.10]
currencies = ["GBP", "USD", "EUR", "GBP"]

# Using zip() to build a list of transaction records
transactions = list(zip(amounts, currencies))

print(transactions)

# Building a more useful structure: list of dicts
transactions = [
    {"amount": amt, "currency": cur}
    for amt, cur in zip(amounts, currencies)
]

print(transactions)

# Converting Multicurrency Transactions
fx_rates = {
    "GBP": 1.00,
    "USD": 0.79,
    "EUR": 0.86
}

gbp_values = [
    amount * fx_rates[currency]
    for amount, currency in zip(amounts, currencies)
]

print(gbp_values)

keys = ["a", "b", "c"]
vals = ["apple", "banana", "carrot"]
mydict = dict(zip(keys, vals))
print(mydict)
mydict = {k: v for k, v in zip(keys, vals)}
print(mydict)
zlist = [*zip(keys, vals)]
print (zlist)
zlist = list(zip(keys, vals))
print(zlist)


