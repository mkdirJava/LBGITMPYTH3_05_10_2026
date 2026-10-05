from account import Account
from currentaccount import CurrentAccount
from isaaccount import ISAAccount
import sys
from importlib import import_module

class Factory:
    @staticmethod
    def create(account_type, *args, **kwargs):
        if account_type == "CurrentAccount":
            return CurrentAccount(*args, **kwargs)
        elif account_type == "ISAAccount":
            return ISAAccount(*args, **kwargs)
        else:
            raise ValueError(f"Unknown account type: {account_type}")


    CLASS_MAP = {
        "currentaccount": "CurrentAccount",
        "isaaccount": "ISAAccount"
    }

    # A Factory Method (one possible, simple solution)
    @staticmethod
    def create_generic(account_type, *args, **kwargs):
        ...
        # Try to dynamically build the right object by
        # Importing modules as needed (with two types of check)
        try:
            module_name = account_type.lower()

            if module_name not in sys.modules:
                account_module = import_module(account_type)
            else:
                account_module = sys.modules[module_name]

            class_name = Factory.CLASS_MAP[module_name]
            account_class = getattr(account_module, class_name)

        except (AttributeError, ModuleNotFoundError):
            raise ImportError(f'{account_type} cannot be found')

        if not issubclass(account_class, Account):
            raise ImportError(f'{account_type} is not a type of account')

        return account_class(*args, **kwargs)


