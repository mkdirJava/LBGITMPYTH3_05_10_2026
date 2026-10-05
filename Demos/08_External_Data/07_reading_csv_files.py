import csv

with open('accounts.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        for field in row:
            print(f"{field}: {row[field]}")
