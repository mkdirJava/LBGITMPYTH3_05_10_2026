def my_func(dir:'str', files:'list'=[]):
    pass

def print_vat(**kwargs:'VAT, gross and message'):
    pass

def calc_vat(gross:'float', vatpc:'float') -> 'list':
    pass


print(my_func.__annotations__)
print(print_vat.__annotations__)
print(calc_vat.__annotations__)
