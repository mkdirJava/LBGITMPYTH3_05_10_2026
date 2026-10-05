class PaymentGateway:
    async def process_payment(self, from_account, to_account, amount):
        # Imagine this calls an external API
        raise NotImplementedError


class BankService:
    def __init__(self, payment_gateway):
        self.payment_gateway = payment_gateway

    async def transfer(self, from_account, to_account, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        result = await self.payment_gateway.process_payment(
            from_account, to_account, amount
        )

        if result["status"] != "success":
            raise RuntimeError("Payment failed")

        return result