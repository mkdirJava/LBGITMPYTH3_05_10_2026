#Pythonic Coding Styles
# Look Before You Leap - Check first whether an operation is safe before doing it.
person = {"Name": "Ted", "Age":34, "Phone":"0123456789"}
person = {"Name": "Ted", "Phone":"0123456789" }
if "age" in person:
    age = person["Age"]
else:
    age = None

# Easier to Ask Forgiveness than Permission - Just do the operation, and handle errors if they occur.
try:
    age = person["Age"]
except KeyError:
    age = None

# Real‑World Finance Example

trade = {"trade_currency":"EUR", "settlement_currency":"USD", "fx_rate":0.89, "amount":100.00}
# LBYL
if "fx_rate" in trade and trade["fx_rate"] is not None:
    value_gbp = trade["amount"] * trade["fx_rate"]
else:
    value_gbp = None
print(f"LBYL: {value_gbp}")

# EAFP
try:
    value_gbp = trade["amount"] * trade["fx_rate"]
except (KeyError, TypeError):
    value_gbp = None
print(f"EAFP: {value_gbp}")