def calculate_savings_balance(principal, int_rate, monthly_deposit=12):
    print(f'principal: {principal}, rate: {int_rate}, deposit: {monthly_deposit}')

calculate_savings_balance(1000, 0.03, 50)
calculate_savings_balance(1000, 0.03)
calculate_savings_balance(principal=1000, monthly_deposit=50, int_rate=0.03)



