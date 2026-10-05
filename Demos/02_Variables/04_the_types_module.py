# Python’s types module is part of the standard library and provides names for many
# internal types and helpers for creating or inspecting dynamic types. It’s extremely useful when:
# - You want to check whether an object is a specific kind of function, generator, coroutine, etc.
# - You are working with dynamic code (e.g., execution environments, metaprogramming).
# - You need to create new dynamic types or manipulate classes programmatically.
#
# types is a module that exposes Python’s internal type objects—things like:
# - FunctionType
# - LambdaType
# - GeneratorType
# - CoroutineType
# - ModuleType
# - MappingProxyType
# - SimpleNamespace
# - MethodType
import time
# Using isinstance() with built‑ins doesn’t always work cleanly.
# Because, There is no built‑in Generator class. So this is invalid:
# isinstance(x, Generator)  # doesn’t exist line will error

# However, the following uses the types model and works :-)
import types
x = print
x(isinstance(x, types.GeneratorType))  #  correct format doesn't error (but returns false)
#x(isinstance(x, Generator)) # doesn’t exist line will error

# Can check if something is a function:
def f(): pass
print(isinstance(f, types.FunctionType)) # True

# Check for lambdas
print(isinstance(lambda x: x + 1, types.LambdaType))

# Check for generators:
def gen():
    yield 1

g = gen()
print(isinstance(g, types.GeneratorType))

import asyncio
# Check for coroutines (async):
async def coro():
    await asyncio.sleep(0.1)
    return "coro is all done!"

c = coro()
print(isinstance(c, types.CoroutineType))
print(asyncio.run(c))# needed to avoid Runtime warning of "coroutine 'coro' was never awaited"

# Create dynamic classes with new_class()
# This dynamically constructs a class at runtime—similar to type("MyClass", ...) but more flexible.
MyClass = types.new_class("MyClass", (object,))
obj = MyClass()
print(type(obj))

# Use SimpleNamespace as a lightweight dynamic object
# SimpleNamespace is great when you want “object-like access” to dynamic data
# — very useful in ETL and finance pipelines.
from types import SimpleNamespace

trade = SimpleNamespace(
    trade_id="T1",
    symbol="AAPL",
    qty=100,
    price=175.5,
)

print(trade.symbol)  # AAPL - It behaves like a dict but with attributes.

# Use MappingProxyType for read‑only dictionaries
# Useful when protecting:
# - FX rate tables
# - configuration
# - risk parameters
# This is commonly used in financial systems to enforce immutability on reference data.
from types import MappingProxyType

fx_rates = MappingProxyType({
    "USD": 0.79,
    "GBP": 1.00,
})

# fx_rates["EUR"] = 0.9  # TypeError (read‑only)
print(fx_rates["USD"])

# Check module objects
import math
print(isinstance(math, types.ModuleType))  # True

# Financial Example
# Building an ETL pipeline where input can be:
# - a function generating trades,
# - a generator streaming trades, or
# - a module providing a trade feed.
# # You can inspect the incoming object:
import types

# This replaces ugly if isinstance(...): chains.
def classify_source(source):
    match source:
        case types.FunctionType():
            return "Function feed"
        case types.GeneratorType():
            return "Generator feed"
        case types.ModuleType():
            return "Module providing data"
        case _:
            return "Unknown source"

print(f"what type is math: {classify_source(math)}")
print(f"what type is gen: {classify_source(gen)}")
print(f"what type is g: {classify_source(g)}")

import types

def myfunc(p):
    if isinstance(p, types.FunctionType):
        p() # invokes the passed in function
    else:
        print(p * 0.2) # assume variable

def greeting():
    print("Hi there!")

myfunc(5)
myfunc(greeting) # calling myfunc passing it the name of another function as a parameter


