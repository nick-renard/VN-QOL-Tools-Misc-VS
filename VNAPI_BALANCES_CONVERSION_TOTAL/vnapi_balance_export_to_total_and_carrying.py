import json
import csv
import locale
import tkinter as tk
import pyperclip

# Set locale for currency formatting
locale.setlocale(locale.LC_ALL, '')

def run():
    # Load JSON file
    with open('VNAPI_BALANCES_CONVERSION_TOTAL/vnapi_balances.json') as f:
        data = json.load(f)

    # Print primaryID and index of first occurrence of a duplicate
    # In this format "Duplicate PrimaryID Found: <> at line <>"
    # If duplicates are found, then dup = True
    # for i in range(len(data)):
    #     for j in range(i + 1, len(data)):
    #         if data[i]['primaryID'] == data[j]['primaryID']:
    #             print("Duplicate PrimaryID Found: " + data[i]['primaryID'] + " at line " + str(i + 1))
    #             dup = True

    positive_balances = []
    for item in data:
        try:
            if item['balance'] > 0:
                positive_balances.append({'primaryID': item['primaryID'], 'balance': item['balance']})
        except KeyError:
            positive_balances.append({'primaryID': 'No Primary ID Found', 'balance': item['balance']})

    total_balance_cents = sum([item['balance'] for item in data])
    total_balance_dollars = total_balance_cents / 100
    formatted_balance = locale.currency(total_balance_dollars, grouping=True)
    
    # Print total balance
    print("")
    print('\x1b[0;30;43m' + 'Total Outstanding Balance: ' + '\x1b[0m')
    print('\x1b[0;30;43m' + formatted_balance + '\x1b[0m')

    # Export extracted accounts and balances data to CSV file
    with open('VNAPI_BALANCES_CONVERSION_TOTAL/vnapi_balance_export_accounts.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['primaryID', 'balance'])
        writer.writeheader()
        for item in positive_balances:
            writer.writerow(item)

    # Export all account ids to CSV file without balances
    with open('VNAPI_BALANCES_CONVERSION_TOTAL/vnapi_balance_export_accounts_only.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['primaryID'])
        writer.writeheader()
        for item in data:
            try:
                writer.writerow({'primaryID': item['primaryID']})
            except KeyError:
                writer.writerow({'primaryID': 'No Primary ID Found'})
            
# run the program
run()