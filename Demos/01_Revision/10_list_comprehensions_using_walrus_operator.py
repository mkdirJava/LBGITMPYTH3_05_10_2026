data = ["Frank", "Phil", "Jess", "Ron"]

# Comprehensions offer an opportunity to use the walrus (:=) operator
valid_lengths = [(name, name_len)
		for name in data
                 if (name_len := len(name)) > 3]

print(f"Names longer than 3 characters: {valid_lengths}")


# Parenthesis is needed due to operator precedence, note the difference:
if qty := len(data) > 3:
    print(qty)

if (qty := len(data)) > 3:
    print(qty)


principal = 5000
rate = 0.05
years = 10
threshold = 6000

# Calculate years and balances when compound interest exceeds £6000 threshold target
balances = [
    (balance, year)
    for year in range(1, years + 1)
    if (balance := principal * (1 + rate) ** year) > threshold
]

for balance in balances:
    print(f"Year {balance[1]:2}: £{balance[0]:,.2f}")

if qty := len(balances) > 3:
    print(qty)

if (qty := len(balances)) > 3:
    print(qty)


# Exchange rates relative to GBP
exchange_rates = {
    "EUR": 1.17,
    "USD": 1.32,
    "JPY": 189.50
}

# Each client has a list of (currency_code, amount_in_GBP) tuples
# and may also have have multiple conversion requests
client_requirements = {
    "client_123": [("EUR", 100), ("USD", 50)],
    "client_456": [("USD", 250), ("JPY", 10)],
    "client_789": [("JPY", 50), ("EUR", 75)]
}


# Convert each client's amount into the requested currency:
# Without walrus operator. Inefficient because exchange_rates[currency] is repeatedly
# evaluated for each client and currency
converted = {
    client: [
        (
            currency,
            round(amount * exchange_rates[currency], 2),
            f"Rate used: {exchange_rates[currency]}"
        )
        for currency, amount in requests
        if currency in exchange_rates
    ]
    for client, requests in client_requirements.items()
}
print(converted)

# With walrus (operator avoiding repeated dictionary lookups):
# exchange_rates[currency] look up is only done once (for each currency)

converted = {
    client: [
        (
            currency,
            round(amount * rate, 2),
            f"Rate used: {rate}"
        )
        for currency, amount in requests
        if (rate := exchange_rates.get(currency)) is not None
    ]
    for client, requests in client_requirements.items()
}

print(converted)

