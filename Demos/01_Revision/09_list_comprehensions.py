import os
import glob
import pprint

principal = 10_000
annual_rate = 0.06
years = 10
n = 12  # compounding periods per year

# Year-end balances using a list comprehension
year_end_balances = [
    principal * (1 + annual_rate / n) ** (n * t)
    for t in range(1, years + 1)
]

for year, balance in enumerate(year_end_balances, start=1):
    print(f"Year {year:2}: £{balance:,.2f}")

# Find first year you hit target
target = 15_000
# Find the earliest month index where balance >= target (if any)
hit_years = [i for i, bal in enumerate(year_end_balances, start=1) if bal >= target]
first_hit = hit_years[0] if hit_years else None
print(f"£{target} target reached in year: {first_hit}")


print("****************************************************************")

pattern = './*'
sizes = [os.path.getsize(fname) for fname in glob.iglob(pattern)]
print(sizes)

# search for sub folders
pattern = '../*'
dirs = [fname for fname in glob.iglob(pattern) if os.path.isdir(fname)]
print(dirs)

# Or putting it all together:
pattern = './*'
sizes = [(fname, os.path.getsize(fname)) for fname in glob.iglob(pattern)]
pprint.pprint(sizes)