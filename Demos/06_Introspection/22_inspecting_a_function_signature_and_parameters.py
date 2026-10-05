import inspect

def myfunc(text: str, qty: int = 5) -> str:
    return text * qty

args = inspect.signature(myfunc)
print(args.__slots__)
print(args._return_annotation)
print(args._parameters)
print(args._parameters['text'])
print(args._parameters['text']._name)
print(args._parameters['text']._annotation)
print(args._parameters['qty']._default)


