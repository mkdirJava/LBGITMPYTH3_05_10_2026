# Suppose lots of unrelated classes need logging:
class Dog:
    ...

class Car:
    ...

class DatabaseConnection:
    ...
# These classes have nothing in common conceptually. so
# creating a base class can be awkward:
class LoggedObject:
    def log(self, message):
        print(message)

class Dog(LoggedObject):
    ...
# Now we're effectively saying:
# A Dog is a LoggedObject.
# which isn't really true.

# A mixin provides a small reusable piece of functionality:
class LoggingMixin:
    def log(self, message):
        print(message)

# Used like:
class Dog(LoggingMixin):
    pass

class Car(LoggingMixin):
    pass

# Now the meaning is:
# Dog gets logging behaviour.
# not
# Dog is fundamentally a logging object.

# However, there is absolutely no difference between mixin's and classes they use the 
# same notation (mixins are declared using "class" keyword). By convention they end with the word "Mixin"