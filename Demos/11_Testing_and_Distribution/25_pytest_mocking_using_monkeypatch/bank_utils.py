# Simulated external dependency
def send_payment_to_bank_api(account_id, amount):
    # Imagine this calls a real banking API
    return {"status": "SUCCESS"}

def process_payment(account_id, amount):
    if amount <= 0:
        raise ValueError("Amount must be positive")

    response = send_payment_to_bank_api(account_id, amount)

    if response["status"] != "SUCCESS":
        raise RuntimeError("Payment failed")

    return "Payment processed"