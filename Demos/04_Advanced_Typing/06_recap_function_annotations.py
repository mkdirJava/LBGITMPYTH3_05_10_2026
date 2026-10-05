def print_vat (*,
           gross:   "Gross amount (including VAT)"=0,
           vatpc:   "VAT in percentage terms"=17.5,
           message: "Free text"='Summary:') \
           -> "No usable return value":
    pass

for kv in print_vat.__annotations__.items():
    print(kv)

print_vat(gross=20)

# FIXED for VSC
from typing import Annotated

def print_vat(*,
              gross: Annotated[float, "Gross amount (including VAT)"] = 0,
              vatpc: Annotated[float, "VAT in percentage terms"] = 17.5,
              message: Annotated[str, "Free text"] = 'Summary:') -> Annotated[None, "No usable return value"]:
    gross = gross + gross * vatpc
    print(gross)


for kv in print_vat.__annotations__.items():
    print(kv)

print_vat(gross=20, vatpc=0.2, message="Boo")
