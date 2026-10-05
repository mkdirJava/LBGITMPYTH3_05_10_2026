# closures are functions that capture and retain state from their surrounding scope.
# Closures are widely used in trading engines, pricing functions, fee calculators,
# and ETL pipelines where you want to create specialized functions with embedded
# configuration (like FX rates, haircut rules, or trader limits).

#Example 1 — Creating a Fee‑Adjusted FX Converter (Trading & Risk)
# A very common need in trading/risk systems: converting amounts into a base currency
# (e.g., GBP), but with desk-specific FX spreads or fees baked in.
# Closures let you generate a custom conversion function for each desk or client.
# Why closures make sense here:
# - Each desk uses different cost assumptions
# - No need for global state, classes, or passing config everywhere
# - Extremely fast to call inside real-time pipelines
# - Clean and safe for multi-tenant or multi‑client systems
# Build the closure:
def make_fx_converter(rates_gbp, fee_bps):
    """
    Returns a conversion function that converts amounts from various
    currencies to GBP using a configurable fee (basis points).
    """
    fee_multiplier = 1 - fee_bps / 10_000   # convert bps → multiplier

    def convert(amount, currency):
        # --- closure captures rates_gbp & fee_multiplier ---
        rate = rates_gbp[currency]
        return amount * rate * fee_multiplier

    return convert   # converting function with captured state

# Using the closure
# FX rates into GBP
rates = {"USD": 0.79, "EUR": 0.86, "GBP": 1.00}

# Create desk-specific converters
prime_broker_conv = make_fx_converter(rates, fee_bps=1.5)  # PB adds 1.5bps
retail_conv       = make_fx_converter(rates, fee_bps=8.0)  # retail more expensive

print(prime_broker_conv(1_000_000, "USD"))   # trader-friendly fee
print(retail_conv(1_000_000, "USD"))         # worse for retail


#Example 2 — Per‑Trader Limit Checker (Risk / Compliance)
# Every trader has different risk limits:
# - max order size
# - max notional
# - max daily volume
# A closure makes it easy to build a customised limit checker for each trader.
# Why closures are ideal here
# - Each trader’s limits are “baked into” their checker
# - The function is self-contained and requires no configuration interface
# - Perfect for real-time pre‑trade checks or intra‑day monitoring
# - Avoids shared mutable state
# - Scales cleanly with hundreds of traders/desks
# Build the closure
def make_limit_checker(max_qty, max_notional):
    """
    Creates a function that checks whether an incoming order
    violates the trader's limits.
    """
    def check(order):
        # --- closure captures max_qty & max_notional ---
        if order["qty"] > max_qty:
            return False, f"Quantity limit exceeded ({order['qty']} > {max_qty})"
        if order["qty"] * order["price"] > max_notional:
            return False, f"Notional limit exceeded"
        return True, "OK"

    return check

# Using the closure
alice_limits = make_limit_checker(max_qty=5000, max_notional=2_000_000)
bob_limits   = make_limit_checker(max_qty=1000, max_notional=250_000)

order1 = {"symbol": "AAPL", "qty": 3000, "price": 175}
order2 = {"symbol": "AAPL", "qty": 6000, "price": 175}

print(alice_limits(order1))   # (True, 'OK')
print(bob_limits(order1))     # (False, 'Quantity limit exceeded...')
print(alice_limits(order2))   # (False, 'Quantity limit exceeded...')





def get_data(orig, tipe):
    temp = orig.split(" ")

    def get_tuple():
        return tuple(temp)

    def get_list():
       return temp

    if tipe == 1:
        return get_tuple

    elif tipe == 2:
        return get_list

data = "Phil Frank Ron"

result1 = get_data(data, 1)
result2 = get_data(data, 2)
print(result1) # prints <function get_data.<locals>.get_tuple at 0x000002A63BA47880>
print(result2) # prints <function get_data.<locals>.get_list at 0x000002A63BA479C0>

print(result1()) # ('Phil', 'Frank', 'Ron')
print(result2()) # ['Phil', 'Frank', 'Ron']
