# The default parameter trap in Python refers to a common and subtle bug
# that occurs when you use mutable objects (like lists or dictionaries) as
# default function arguments.
# It happens because default parameter values are evaluated
# once—at function definition time—not each time the function is called.
# This means a default list, dict, or other mutable object is
# shared across all calls, often causing surprising behaviour.

# The Problem: Mutable Defaults Are Persistent
# Bad Example (The Trap)
def add_trade(trade, trade_list=[]):
    trade_list.append(trade)
    return trade_list

# Call it multiple times
print(add_trade("T1"))
print(add_trade("T2"))
print(add_trade("T3"))
# Output!!!!!!:
# ['T1']
# ['T1', 'T2']
# ['T1', 'T2', 'T3']

# Why Does This Happen?
# - The list [] is created at definition time, not call time
# - The same list is reused on every call
# - Mutating it persists the mutation across calls
# # This behaviour is intentional (for performance and consistency) but often surprising.

# Correct Pattern: Use None, then create a new object
def add_trade(trade, trade_list=None):
    if trade_list is None:
        trade_list = []
    trade_list.append(trade)
    return trade_list

print(add_trade("T1"))
print(add_trade("T2"))
print(add_trade("T3"))
# output:
# ['T1']
# ['T2']
# ['T3']

# Example: Risk Factor Accumulation Bug
def accumulate_factors(factor, bucket=[]):
    bucket.append(factor)
    return bucket

accumulate_factors("IR01")  # interest rate delta
accumulate_factors("CR01")  # credit spread delta
accumulate_factors("FX01")  # FX sensitivit
# output:
# ['IR01', 'CR01', 'FX01']y

# Example: Market Data Cache Growing Unexpectedly
def cache_tick(tick, cache=[]):
    cache.append(tick)
    return cache

# Multiple subsystems might call cache_tick() expecting isolation:
# - Algo engine
# - Market surveillance
# - OMS
#
# But they all share the same cache list.
# You get cross‑contamination between components → very dangerous.

