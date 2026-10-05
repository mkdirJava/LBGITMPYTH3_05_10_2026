portfolio = {
    "name": "Global Fund",
    "positions": [
        {"symbol": "AAPL", "qty": 100, "price": 175.5},
        {"symbol": "MSFT", "qty": 80, "price": 310.2},
    ],
    "sub_portfolios": [
        {
            "name": "EMEA Book",
            "positions": [
                {"symbol": "VOD.L", "qty": 2000, "price": 0.98}
            ],
            "sub_portfolios": []
        },
        {
            "name": "US Tech Book",
            "positions": [
                {"symbol": "AMZN", "qty": 10, "price": 3300},
            ],
            "sub_portfolios": [
                {
                    "name": "AI Sub-Fund",
                    "positions": [
                        {"symbol": "NVDA", "qty": 5, "price": 650}
                    ],
                    "sub_portfolios": []
                }
            ]
        }
    ]
}

def portfolio_value(pf):
    # Value of direct positions
    value = sum(pos["qty"] * pos["price"] for pos in pf["positions"])

    # Recursively add value of each sub-portfolio
    for sub_pf in pf["sub_portfolios"]:
        value += portfolio_value(sub_pf)

    return value

total = portfolio_value(portfolio)
print(f"Total Portfolio Value: {total:,.2f}") # Total Portfolio Value: 80,576.00

print("\n*****************************************************************************\n")
def get_transaction_source(tx_id, ledger):
    """Recursively find the original transaction ID for a given audit trail."""
    # Base Case: If the transaction has no parent, it is the source
    parent_id = ledger.get(tx_id)

    if parent_id is None:
        return tx_id

    # Recursive Case: Move up the chain to the parent
    return get_transaction_source(parent_id, ledger)


# Audit Ledger: {Transaction: Parent_Transaction}
audit_trail = {
    "TX-104": "TX-103",
    "TX-103": "TX-102",
    "TX-102": "TX-101",
    "TX-101": None  # Original deposit
}

original_source = get_transaction_source("TX-104", audit_trail)
print(f"The original source of TX-104 is: {original_source}")
# Output: The original source of TX-104 is: TX-101
