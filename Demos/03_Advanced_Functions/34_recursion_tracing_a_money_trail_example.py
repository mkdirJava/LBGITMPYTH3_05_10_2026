def get_transaction_source(tx_id, ledger):
    # Recursively find the original transaction ID
    parent_id = ledger.get(tx_id)
    if parent_id is None:
        return tx_id
    # Recursive Case: Move up the chain to the parent
    return get_transaction_source(parent_id, ledger)

# Audit Ledger: {Transaction: Parent_Transaction}
audit_trail = {
    "TX-104": "TX-103", "TX-103": "TX-102", 
    "TX-102": "TX-101", "TX-101": None  # Original deposit
}

original_source = get_transaction_source("TX-104", audit_trail)
print(f"The original source of TX-104 is: {original_source}")
