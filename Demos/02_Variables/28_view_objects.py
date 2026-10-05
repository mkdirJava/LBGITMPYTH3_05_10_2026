acronyms = {"APR":"Annual Percentage Rate",
         "APY":"Annual Percentage Yield",
         "BACS":"Banker's Automated Clearing Services (UK)",
         "ROI":"Return On Investment"}

for kv in acronyms.items():
    print(kv)

lkeys = list(acronyms.keys())
print(lkeys)

new_acronyms = acronyms.keys() | {'ACH', 'BACS', 'SWIFT'}
print(new_acronyms)
