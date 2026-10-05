grid = [[0] * 3] * 3     # BAD: all 3 rows are the SAME list object
grid[0][0] = 1
print(grid)  # [[1, 0, 0], [1, 0, 0], [1, 0, 0]]  <- oops

#Better to use a list comprehension so each row is a distinct object:
grid = [[0] * 3 for _ in range(3)]   # correct: independent rows
grid[0][0] = 1
print(grid)  # [[1, 0, 0], [0, 0, 0], [0, 0, 0]]  <- better :-)
