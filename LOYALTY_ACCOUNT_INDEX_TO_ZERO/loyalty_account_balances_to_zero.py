import json

def run():
    # Read the JSON file
    with open('LOYALTY_ACCOUNT_INDEX_TO_ZERO/loyalty_accounts_index.json') as file:
        data = json.load(file)

    # Filter accounts with a positive balance
    positive_accounts = [account for account in data['accounts'] if account['balance'] > 0]

    # Create a new JSON object for API request
    api_request = {
        "organization_name": positive_accounts[0]['user_details'][0]['organization_name'],
        "adjustments": []
    }

    i = 0
    # Iterate over positive accounts and add them to the API request
    for account in positive_accounts:
        i += 1
        api_request['adjustments'].append({
            "account_id": account['user_details'][0]['external_user_id'],
            "description": "Resetting Virtual Currency Balance for Season",
            "set_amount": 0,
            "hidden_transaction": False,
            "instance": account['instance']
        })
        
    print('\x1b[0;30;42m' + 'Total accounts to be set to zero: ' + str(i) + '\x1b[0m')

    # Write the API request JSON to a file
    with open('LOYALTY_ACCOUNT_INDEX_TO_ZERO/postman_request.json', 'w') as file:
        json.dump(api_request, file, indent=4)

run()