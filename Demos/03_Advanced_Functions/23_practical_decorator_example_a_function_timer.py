import time
import functools

def my_timer(fn):
    """Display execution time of decorated function"""
    def timer_wrapper_func(*args, **kwargs):
        # Start the timer
        start_t = time.perf_counter()
        # Call the function
        result = fn(*args, **kwargs)
        # End timer and work out elapsed time
        end_t = time.perf_counter()
        duration = end_t - start_t
        print(f"{fn.__name__ !r} execution time {duration:.5f} s")
        return result
    return timer_wrapper_func

@my_timer
def calc_cubes(qty):
    """Return sum of cubes from 1 to n inclusive"""
    value = sum([num ** 3 for num in range(1, qty)])
    return value

# Calling with decoration is completely transparent
print(calc_cubes(100000))
