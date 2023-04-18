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


    total_balance_cents = sum([item['balance'] for item in data])
    total_balance_dollars = total_balance_cents / 100
    formatted_balance = locale.currency(total_balance_dollars, grouping=True)

    root = tk.Tk()
    root.title("Total Outstanding Virtual Currency")

    # Create label with total balance
    balance_label = tk.Label(root, text=formatted_balance, font=('Arial', 18))
    balance_label.pack(pady=10)

    # Create button to copy total balance to clipboard and close window
    def copy_and_close():
        pyperclip.copy(formatted_balance)
        root.destroy()

    copy_button = tk.Button(root, text="Copy Total Outstanding Balances & Close", command=copy_and_close, font=('Arial', 14))
    copy_button.pack(pady=10)

    # Run main loop
    root.mainloop()

    # Extract data for items with positive balances
    positive_balances = [{'primaryID': item['primaryID'], 'balance': item['balance']} for item in data if item['balance'] > 0]

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
            writer.writerow({'primaryID': item['primaryID']})