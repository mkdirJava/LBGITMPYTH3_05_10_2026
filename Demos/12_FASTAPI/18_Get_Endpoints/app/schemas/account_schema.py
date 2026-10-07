from pydantic import BaseModel, Field

class Account(BaseModel):
    account_id: int
    customer_id: int
    balance: float = Field(gt=0)


class Thing ():
    def __init__(self):
        self.__name =""
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, new_name: str):
        self.__name = new_name



t = Thing()
t.name = "hi"
print(t.name)
setattr(t,"name",True)
print(t.name)
