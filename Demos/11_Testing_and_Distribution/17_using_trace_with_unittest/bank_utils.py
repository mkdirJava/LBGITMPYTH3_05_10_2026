def calculate_fees(balance, withdrawals):
    fee = 0

    # £1 fee per withdrawal after 3 free ones
    if withdrawals > 3:
        fee = (withdrawals - 3) * 1

    # Overdraft fee
    if balance < 0:
        fee += 10

    return fee