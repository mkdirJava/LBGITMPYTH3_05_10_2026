iterable = ["Angie", "Brian", "Clara", "Daksh", "Ekveera"]

result = ''
for item in iterable:
    result += item
print(result)

lresult = []
for item in iterable:
    lresult.append(item)
print(result)

result = ''.join(lresult)
print(result)

result = ''.join([item for item in iterable])
print(result)

