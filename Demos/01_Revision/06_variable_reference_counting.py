import sys
my_data = []
my_data2 = my_data

print(sys.getrefcount(my_data)) # 3

# 3 ? !!!!!!
# One for each reference created…
# And, of course, one more for the argument passed to the getrefcount() function!

# life = lambda t : "hi"

# print(life("thing"))



