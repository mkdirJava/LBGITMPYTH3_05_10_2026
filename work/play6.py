import re
from typing import List
    
class CustomerProfileValidation():
    def __init__(self, email: str, mobile: str, customerId:str):
        self.pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        self._email= email
        self._mobile_number = mobile
        self.customer_id = customerId
        
    def __email_validator(self):
        if re.fullmatch(self.pattern, self._email) is  None:
            raise ValueError("Email Validation failed")

    def __mobile_number_validator(self):
        if self._mobile_number.isnumeric() is False or len(self._mobile_number) != 10 :
            raise ValueError("Phone number number must be numeric and be 10 digits long")

    def __customer_Id_validator(self): 
        if self.customer_id.isnumeric() is False or len(self.customer_id) != 8 :
            raise ValueError("Customer id number number must be numeric and be 8 digits long")

    def run_validations(self) -> List[str]:        
        error_messages: List[str] = []
        for attr in dir(self):
            if "validator" in attr and callable(getattr(self,attr)):
                try:
                    validator_method = getattr(self,attr)
                    validator_method()
                except ValueError as e:
                    error_messages.append(e)
        return error_messages
        
customer_profile_validator = CustomerProfileValidation("h@gmail.com","1234567890","12345678")
error_messages = customer_profile_validator.run_validations()
print(error_messages)