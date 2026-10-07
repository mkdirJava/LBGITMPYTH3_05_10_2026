
from enum import Enum
from typing import Dict, List, Set


class ExtendedIndustrySortCodeEntry():
    def __init__(self, 
                 bank_office_identifier: str, 
                 branch_title:str, 
                 telephone_number:str, 
                 postal_address:str):
        self.bank_office_identifier: str = bank_office_identifier
        self.branch_title: str = branch_title
        self.telephone_number: str = telephone_number
        self.postal_address: str = postal_address
        self.clearing: str
    
class UpdateActions(Enum):
    UPDATED = "UPDATED"
    CLOSED = "CLOSED"
    REDIRECT_SORT_CODES = "REDIRECTED"

class ExtendedIndustrySortCodeDirectory():

    def __init__(self,register: Dict[str,ExtendedIndustrySortCodeEntry] = {}):
        if register is not None:
            self.register = register
        else:
            self.register: Dict[str,ExtendedIndustrySortCodeEntry] ={}

    def register_interest():
        pass

    def update(entry: ExtendedIndustrySortCodeEntry, action: UpdateActions):
        match action:
            case UpdateActions.UPDATED:
                pass
            case UpdateActions.CLOSED:
                pass
            case UpdateActions.REDIRECT_SORT_CODES:
                pass


class NotificationEnum(Enum):
    EMAIL = "EMAIL"
    MOBILE = "MOBILE"
    NONE = "NONE"

class User():
    def __init__(self, name:str, subscription_type:str, destination:str,notification: NotificationEnum):
        self.name = name
        self.subscription_type = subscription_type
        self.destination = destination
        self.notification: Set[NotificationEnum] = (notification)

class NotificationContext():
    def __init__(self, message:str):
        self.message = message

class NotificationChannel():
    def __init__(self, type: NotificationEnum):
        self.notification_type: NotificationEnum = type
    
    def notify(notificationContext:NotificationContext):
        pass

class EISCDChangeNotifier():

    def __init__(self):
        self.notifiers: List[NotificationChannel]= []
        self.users: List[User] = []

    def add_notifier(self, notifier: NotificationChannel):
        self.notifiers.append(notifier)

    def subscribe(self,user: User):
        self.Users.append(user)
    
    def unsubscribe(self,user: User, notification_enum: NotificationEnum):
        for internal_user in self.users:
            internal_user.name == user.name
            internal_user.notification.remove(notification_enum)
        

    def update(self, notification_context: NotificationContext):
        self.notify(notification_context)


    def notify(self, notification_context: NotificationContext):
        for user in self.Users:
            user.notification_channel.notify(notification_context)





class MyPickle():
    def __init__(self, name: str):
        self.name = name



import pickle

my_pickle = MyPickle("time")
with open("my_pickle.pkl", "wb") as f:
    pickle.dump(my_pickle, f)

with open("my_pickle.pkl", "rb") as f:
    # load() automatically reconstructs the object state
    restored_pickle: MyPickle = pickle.load(f)    
    print(restored_pickle)