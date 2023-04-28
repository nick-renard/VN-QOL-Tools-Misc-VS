import json

def run():
    # Open the JSON file and load the data
    with open('VNAPI_SET_ALL_ACCOUNTS_TO_ZERO/vnapi_balances.json', 'r') as f:
        data = json.load(f)

    # Get a list of all primaryIDs
    primary_ids = [d['primaryID'] for d in data]

    # Write the list of primaryIDs to a file
    with open('VNAPI_SET_ALL_ACCOUNTS_TO_ZERO/primary_ids.txt', 'w') as f:
        for primary_id in primary_ids:
            f.write(primary_id + '\n')

    # Filter the data to only include accounts with a balance
    accounts_with_balance = [d['primaryID'] for d in data if d['balance'] > 0]

    # Ask the user for input
    instance = input("Enter the instance (leave blank for null): ")
    organization_name = input("Enter the organization name: ")

    # Set the instance name to null if the user didn't enter a value
    if not instance:
        instance = None

    # Create the JSON request
    request_data = {
        "organization_name": organization_name,
        "adjustments": []
    }

    # Add the adjustments for each account with a balance to the request
    for account_id in accounts_with_balance:
        adjustment = {
            "account_id": account_id,
            "description": "Admin Expiration",
            "set_amount": 0,
            "hidden_transaction": False,
            "instance": instance
        }
        request_data["adjustments"].append(adjustment)

    # Write the request data to a file
    with open('VNAPI_SET_ALL_ACCOUNTS_TO_ZERO/request.json', 'w') as f:
        json.dump(request_data, f, indent=2)
