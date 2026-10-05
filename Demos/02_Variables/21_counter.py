from collections import Counter

lst = ["current", "deposit", "current", "mortgage"]
cl = Counter(lst)
print(cl)
print("No. of currents:", cl['current'])

cl2 = Counter(current=44, deposit=293, mortgage=73)
print("Accounts:", sum(cl2.values()))


text1 = "the quick brown fox jumps over the lazy dog"
text2 = "quick nymph bugs vex fjord waltz"
text3 = "cwm fjord-bank glyphs vext quiz"
texts = [text1, text2, text3]
for text in texts:
    print(Counter(text))

