class Base:
    name = "Base"

    @classmethod
    def who_am_i_cls(cls):
        return cls.name

    @staticmethod
    def who_am_i_stc():
        return Base.name

class Child(Base):
    name = "Child"

print(Child.who_am_i_cls()) # prints "Child" because cls is bound to Child.
print(Child.who_am_i_stc()) # prints "Base" because the method has no knowledge of the class that invoked it.