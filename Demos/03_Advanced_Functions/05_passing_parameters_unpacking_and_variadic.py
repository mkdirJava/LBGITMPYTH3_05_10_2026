# Unpacking
def calc_product(x, y, z):
    print(f"product: {x * y * z}")

numbers_tuple = 2, 4, 6
calc_product(*numbers_tuple)

# Variadic
def calc_products(a, *nums):
    res = ""
    for n in nums:
        res += f"{str(a * n)} "
    print(res)

calc_products(5, 1, 2, 3, 4)
