import re


class CustomerProfileValidator:
    def __init__(self, email: str, mobile: str, customerID: str):
        self.email = email
        self.mobile = mobile
        self.customerID = customerID

    def _validate_email(self) -> bool:
        """Validate email"""
        email = self.email.strip().lower()
        return re.fullmatch(r"^[a-z]+\.[a-z]+@[a-z]+\.[a-z]{2,}$", email) is not None

    def _validate_mobile(self) -> bool:
        """Validate mobile telephone"""
        mobile = self.mobile.replace(" ","")
        print(mobile)
        return re.fullmatch(r"\d{10}", mobile) is not None

    def _validate_customer_id(self) -> bool:
        """Validate Customer ID"""
        customerID = self.customerID.strip()
        return customerID.isdigit() and len(customerID) == 8

    def run_validations(self) -> dict[str, bool]:

        results = {
            # dictionary comprehension:
            # keys are methods' documentation
            # values are result of calling methods
            method.__doc__: method()
            for name in dir(self) # iterate over all attributes of instance
            if name.startswith("_validate_")
            and callable(method := getattr(self, name)) # use walrus operator to get the method
            and callable(getattr(type(self), name, None)) # Ensure method exists on the class,and is not just dynamically added to the instance.
        }
        print(results)
        results["all_valid"] = all(results.values())
        return results

# Testing your validator 
def test_customer_profile_validator():
    customer = CustomerProfileValidator(
        email="frank.boifur@qa.com",
        mobile="071 234 5678",
        customerID="01234567",
    )
    results = customer.run_validations()
    return results

# Run your test
if __name__ == "__main__":
    print(test_customer_profile_validator())