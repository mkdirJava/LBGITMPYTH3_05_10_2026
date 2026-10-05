class BankService:
    def __init__(self, fraud_checker):
        self.fraud_checker = fraud_checker

    async def transfer(self, from_acc, to_acc, amount):
        is_safe = await self.fraud_checker.check(from_acc, to_acc, amount)

        if not is_safe:
            raise ValueError("Fraud detected")

        return {"status": "success", "amount": amount}