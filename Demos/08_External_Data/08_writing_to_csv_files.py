import csv

new_accounts = (('Kamran Liaqat', 'ACC100247', 104.67), ('Sadia Saleem', 'ACC100248', 233.28))
# Open the file for writing
with open('accounts2.csv', 'w', newline='') as csvfile:
    # Set up the writer and the csv settings
    mywriter = csv.writer(csvfile, delimiter=',',
                          quotechar='"', quoting=csv.QUOTE_NONNUMERIC)

    # Write the csv headings
    mywriter.writerow(['account_name', 'id', 'balance'])

    for account in new_accounts:
        mywriter.writerow(account)
        # mywriter.writerow([account[0], account[1], account[2]])

