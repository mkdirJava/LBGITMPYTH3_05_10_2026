# Fixed currency FX conversion function
# Great for risk engines or trade‑capture components.
from functools import partial

def fx_convert(amount, rate, fees):
    return amount * rate * (1 - fees)

# Create a GBP→USD converter with fixed spread + fee
gbp_usd = partial(fx_convert, rate=1.2610, fees=0.0005)

print(gbp_usd(100_000))  # convert 100k GBP to USD
