# The Walrus operator (:=) is a Python operator introduced in Python 3.8
# that lets you assign a value to a variable as part of an expression.
# It’s called the “walrus operator” because := looks like a walrus’s eyes and tusks
my_list = [1,2,3,4,5,6,7,8,9,10,11]

# with walrus operator
if (n := len(my_list)) > 10:
    print(f"List is too long ({n} elements)")

# without walrus operator
n = len(my_list)
if n > 10:
    print(f"List is too long ({n} elements)")

# Finance example:
# Suppose you process live ticks and want to alert when a move exceeds a threshold.
from walrus_get_price_tick import get_price_update

while tick := get_price_update():
    if (delta := tick.price - tick.prev_close) > 1.5:
        print(f"Large move detected: {delta}")