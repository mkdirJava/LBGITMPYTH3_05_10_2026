from abc import abstractmethod, ABC
from typing import NewType, Union, NamedTuple,Generic,TypeVar,List

Tabulus = NewType("Tabulus", int)
Tabulus_2 = NewType("Tabulus_2", str)
Accord  = Union[ str , int]


class BaseAction(ABC):
    @abstractmethod
    def do_action(self)-> str: ...

class Dog(BaseAction):
    def do_action(self)-> str:
        return "dog action"
    
class Cat(BaseAction):
    def do_action(self) -> str:
        return "cat action"
    
class ActionUser[T: BaseAction ]():

    def __init__ (self, actioners: List[T]):
        super().__init__()
        self.actioners = actioners

    def do_something(self):
        for actioner in self.actioners:
            print(actioner.do_action())


actioners: List[BaseAction] = [Dog(),Cat()]
action_user = ActionUser(actioners=actioners)
action_user.do_something()
thing = BaseAction()



        
