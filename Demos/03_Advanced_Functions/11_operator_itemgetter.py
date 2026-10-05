import operator

countries = [["United Kingdom", 44, "Pounds"],
             ["Canada", 1, "Dollar"],
             ["Japan", 7, "Yen"],
             ["France", 34, "Euro"]]

# Sort by name using a lambda
c = sorted(countries, key=lambda c: c[0])
print(c)

# Sort by currency using itemgetter
c = sorted(countries, key=operator.itemgetter(2))
print(c)
