import inspect


class TraceUse(object):
    def __init__(self, pname, pos):
        self.tpos = f"{pname} created at line: {pos}"
        print(f"[INIT] Descriptor initialized with value: {self.tpos}")

    def __get__(self, inst, cls):
        print("[__get__] Accessing the attribute via descriptor")
        print(f"          Instance: {inst}")
        print(f"          Class: {cls}")
        return self.tpos

    def __set__(self, inst, value):
        print("[__set__] Setting the attribute via descriptor")
        print(f"          New value: {value}")
        self.tpos = str(value)

    def __delete__(self, inst):
        print("[__delete__] Deleting the attribute via descriptor")
        self.tpos = None


class Person(object):
    # Descriptor assigned at class level
    t1 = TraceUse('Mark A', inspect.currentframe().f_lineno)


# --- Demonstration ---
print("\n--- Creating Person instance ---")
p = Person()

print("\n--- Accessing attribute (triggers __get__) ---")
print("p.t1 =", p.t1)

print("\n--- Setting attribute (triggers __set__) ---")
p.t1 = "Updated Name"

print("\n--- Accessing attribute again (triggers __get__) ---")
print("p.t1 =", p.t1)

print("\n--- Deleting attribute (triggers __delete__) ---")
del p.t1

print("\n--- Accessing after delete (still triggers __get__) ---")
print("p.t1 =", p.t1)