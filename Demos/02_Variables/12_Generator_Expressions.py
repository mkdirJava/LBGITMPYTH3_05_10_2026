principal = 1000
rate = 0.05
years = 10

# Generator expression: compute value per year using compound‑interest formula:
balances = (principal * (1 + rate) ** year for year in range(1, years + 1))
print("Yearly balances:")
for amount in balances:
    print(f"£{amount:,.2f}, ", end="")
