import json

def run():
    print()
    print("Data Source Menu:")
    print("1. JSON input")
    print("2. Text file")
    print("3. Exit")
    print()
    choice = input("Enter the number corresponding to your choice: ")

    if choice == '1':
        # Read the JSON file
        with open('scripts/LOYALTY_ACCOUNT_INDEX_TO_AMOUNT/loyalty_accounts_index.json') as file:
            data = json.load(file)
    elif choice == '2':
        instance = input("Enter the instance: ")
        organization_name = input("Enter the organization name: ")
        with open('scripts/LOYALTY_ACCOUNT_INDEX_TO_AMOUNT/loyalty_accounts_text.txt') as file:
            accounts = file.read().splitlines()
        data = {
            "accounts": []
        }
        for account_id in accounts:
            account = {
                "user_details": [
                    {
                        "external_user_id": account_id
                    }
                ],
                "instance": instance
            }
            data["accounts"].append(account)
        data["accounts"][0]["user_details"][0]["organization_name"] = organization_name
    else:
        print("Exiting...")
        return

    # Create a new JSON object for API request
    api_request = {
        "organization_name": data['accounts'][0]['user_details'][0]['organization_name'],
        "adjustments": []
    }

    i = 0
    # Iterate over accounts and add them to the API request
    for account in data['accounts']:
        i += 1
        instance = account['instance']
        adjustment = {
            "account_id": account['user_details'][0]['external_user_id'],
            "description": "2023-24 STH Credit",
            "amount": 25000,
            "hidden_transaction": False,
            "instance": instance
        }
        api_request['adjustments'].append(adjustment)

    print('\x1b[0;30;42m' + 'Total accounts to be awarded: ' + str(i) + '\x1b[0m')

    # Write the API request JSON to a file
    with open('scripts/LOYALTY_ACCOUNT_INDEX_TO_AMOUNT/postman_request.json', 'w') as file:
        json.dump(api_request, file, indent=4)

run()
