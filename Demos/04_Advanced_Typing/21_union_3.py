from typing import Union, List
valid_data = Union[str, float]

# will error: '_GenericAlias' object does not support item assignment
# limitation can be addressed by using a TypeVar instead (see next example)
data = List[valid_data] = ["123", 2.50, "hello", 105.2]

