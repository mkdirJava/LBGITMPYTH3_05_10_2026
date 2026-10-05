def fx_convert(amount, rate, fees):
    return amount * rate * (1 - fees)
#gbp_usd = partial(fx_convert, rate=1.2610, fees=0.0005)
# Create a GBP→USD converter using a lambda instead of partial
# We hardcode the rate and fees, leaving 'amount' as the argument
gbp_usd = lambda amt: fx_convert(amt, rate=1.2610, fees=0.0005)

print(gbp_usd(100_000))  # convert 100k GBP to USD
