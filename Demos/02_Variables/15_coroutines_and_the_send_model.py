def compound_interest(initial_balance, annual_rate):
    # Coroutine tracks compound interest and accepts new deposits.
    balance = initial_balance
    rate = annual_rate
    # Prime: initial yield returns the starting balance
    value = yield balance
    while True:
        if isinstance(value, dict):
        # Allow dynamic updates
            balance += value.get("deposit", 0)
            rate = value.get("rate", rate)
        balance *= (1 + rate) # Apply one period of interest
        # Yield updated balance and wait for next instruction
        value = yield balance

# Start with £1000, interest rate 5%
c = compound_interest(1000, 0.05)
print("Start:", next(c))
print(f"After deposit: £{c.send({'deposit': 200}):,.2f}")
print(f"Next period: £{c.send({}):,.2f}")
print(f"After rate change: £{c.send({'rate': 0.07}):,.2f}")
print(f"After another deposit: £{c.send({'deposit': 500}):,.2f}")
