# how to use functools.partial and functools.wraps in Python.
# Both tools are extremely useful in trading systems, risk engines, pricing libraries, and data pipelines.

# functools.partial — Financial Examples
# partial() lets you pre‑fill some arguments of a function, creating a specialised version.
# In financial code this is extremely handy for:
# - fixing a pricing model’s parameters
# - creating preconfigured risk calculators
# - binding currency or product type
# - binding constants like discount rates
# - reducing boilerplate in data pipelines

# Example 1 — Preconfigured option pricers with fixed parameters
# Suppose you have a Black‑Scholes pricing function:
# The Black–Scholes pricing function is a mathematical formula used in finance to compute the
# fair value (theoretical price) of a European option—either a call or a put—under a specific
# set of modelling assumptions. It is one of the foundational results in quantitative finance.
# The function calculates the fair price of a European option by modelling the underlying asset
# price as a stochastic (random) process and discounting its expected payoff under the risk‑neutral measure.
# It tells you what a European call or put should be worth today based on volatility, interest rates, time to expiry,
# and the current price of the underlying asset.
# A European option is a type of financial option contract that can only be exercised at one specific time:
# on the option’s expiration date.
#
# The formula uses 5 key variables:
# # Symbol    Meaning
# S         Current price of the underlying asset
# K         Strike price
# T         Time to maturity (in years)
# r         Risk‑free interest rate
# σ (sigma) Volatility of returns
# N()       Cumulative normal distribution
from math import exp, sqrt, log
from functools import partial
import scipy.stats as stats

def black_scholes_call(S, K, r, sigma, T):
    d1 = (log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*sqrt(T))
    d2 = d1 - sigma*sqrt(T)
    return S * stats.norm.cdf(d1) - K * exp(-r*T) * stats.norm.cdf(d2)

# Instead of passing the same r, sigma, and T all day, we can create a pre‑configured pricer:
sp500_pricer = partial(black_scholes_call, r=0.02, sigma=0.18, T=0.5)

# Now the user only supplies spot and strike:
print(sp500_pricer(S=5200, K=5100))
print(sp500_pricer(S=5200, K=5300))

# Example 2 — Fixed currency FX conversion function
# Great for risk engines or trade‑capture components.
from functools import partial

def fx_convert(amount, rate, fees):
    return amount * rate * (1 - fees)

# Create a GBP→USD converter with fixed spread + fee
#gbp_usd = partial(fx_convert, rate=1.2610, fees=0.0005)

# Create a GBP→USD converter using a lambda instead of partial
# We hardcode the rate and fees, leaving 'amount' as the argument
gbp_usd = lambda amount: fx_convert(amount, rate=1.2610, fees=0.0005)

print(gbp_usd(100_000))  # convert 100k GBP to USD


# Example 3 — Pre‑configured discounting functions
def discount(cashflow, rate, years):
    return cashflow / ((1 + rate)**years)

discount_5yr = partial(discount, years=5)
discount_usd = partial(discount, rate=0.04)

# You can chain them:
discount_usd_5yr = partial(discount, rate=0.04, years=5)
print(discount_usd_5yr(1_000_000))


# Example 4 — Portfolio risk calculators with fixed parameters
def compute_var(returns, confidence, window):
    return sorted(returns)[int((1-confidence)*len(returns))]

var_99 = partial(compute_var, confidence=0.99, window=250)
# Now apply it to any asset’s return stream.


# functools.wraps — Financial Examples
# wraps is used inside decorators.
# It preserves metadata like the function name, docstring, and annotations.
# Almost every financial production system uses decorators for:
# - logging
# - timing (profiling)
# - audit and compliance
# - caching
# - authorisation checks
# - retry wrappers for market‑data APIs
#
# Example 1 — Audit/log every trade to a compliance log
from functools import wraps
from datetime import datetime, UTC
def audit_log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        ts = datetime.now(UTC).isoformat()
        print(f"[AUDIT] {ts}: called {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

# Use it to wrap order submission:
@audit_log
def submit_order(symbol, qty):
    print(f"Placing order: {symbol} x {qty}")

submit_order("AAPL", 100)

# Example 2 — Measure performance of pricing functions
import time
from functools import wraps
def timed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.perf_counter() - start:.6f}s")
        return result
    return wrapper

# Apply to a Monte‑Carlo pricer:
@timed
def price_option_mc():
    # monte-carlo steps here
    pass

# Example 3 — Retry decorator for fragile market‑data APIs
from functools import wraps
import random, time
def retry(times=3):
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if i == times - 1:
                        raise
                    time.sleep(0.2)
        return wrapper
    return decorate

# Use it around a feed call:
@retry(times=5)
def get_spot_price(symbol):
    if random.random() < 0.3:
        raise RuntimeError("Feed error")
    return 100.25

# Combined Example (partial + wraps)
# Let’s create a pre‑configured pricing function and wrap it with audit behaviour.

# wraps: audit usage of the pre-configured function
from functools import partial, wraps

def audit(func):
    @wraps(func)
    def wrapper(*args, **kw):
        print(f"Calling {func.__name__}")
        return func(*args, **kw)
    return wrapper

@audit
def fx_convert(amount, rate, fees):
    return amount * rate * (1 - fees)

# Create a pre-configured converter (partial AFTER decorating)
eurusd_pricer = partial(fx_convert, rate=1.095, fees=0.0003)

print(eurusd_pricer(10_000))  # OK, logs and converts
