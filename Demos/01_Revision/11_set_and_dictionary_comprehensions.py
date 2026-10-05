import os
import glob

# Python 3 allows comprehensions on sets…
gbp_prices = {10, 25, 40, 100}
exchange_rate = 1.17   # GBP → EUR

eur_prices = {round(price * exchange_rate, 2) for price in gbp_prices}
print(eur_prices)


# … and dictionaries
exchange_rates = {"EUR": 1.17, "USD": 1.32, "JPY": 189.50}

# Each client has a list of (currency_code, amount_in_GBP) tuples
client_requirements = {"client_123": ("EUR", 100), "client_456": ("USD", 250),"client_789": ("JPY", 500)}

# Convert each client's amount into the requested currency
converted = {
    client: (currency, round(amount * exchange_rates[currency], 2))
    for client, (currency, amount) in client_requirements.items()
}
print(converted)



# Example that uses glob module to retrieve file system info
# set comprehension and tuples
pattern = './*.py'
tsizes = {(fname, os.path.getsize(fname))
           for fname in glob.iglob(pattern)}

print(tsizes)

# dictionary comprehension
dsizes = {fname: size for fname, size in tsizes
          if size > 0}
print(dsizes)
