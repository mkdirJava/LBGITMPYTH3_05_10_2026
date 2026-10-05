from pprint import pprint

class Validator:
    MIN_SIZE = 8

    def __init__(self, new_pwd):
        """Constructor"""
        self.__password = new_pwd
        self.__methods = self.get_checks()

    def check_len(self):
        """Checks minimum length of password"""
        return len(self.__password) >= Validator.MIN_SIZE

    def check_uppercase(self):
        """At least one uppercase letter"""
        return any(char.isupper() for char in self.__password)

    # def check_isdigit(self):
    #     """At least one digit"""
    #     return any(char.isdigit() for char in self.__password)

    def get_checks(self):
        """Dynamically assemble the check"""
        # Assembles a list of callable "check" methods
        methods = [method for attrib in dir(self)
                          if attrib.startswith("check_") and
                          callable(method := getattr(self, attrib))]
        return methods

    @property
    def checks(self):
        _descriptions = [method.__doc__ for method in self.__methods]
        return list(zip(_descriptions, self.__results))

    @property
    def is_valid(self):
        self.__results = [func() for func in self.__methods]
        return all(self.__results)


password = input("Enter password: ")
new_validator = Validator(password)

if new_validator.is_valid is True:
    print(f"{password} is valid")
else:
    print(f"{password} is invalid")
    pprint(new_validator.checks)
