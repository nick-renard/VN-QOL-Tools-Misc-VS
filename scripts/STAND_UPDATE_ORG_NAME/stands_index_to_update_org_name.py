import json

def run():
    # Load JSON file
    with open('scripts/STAND_UPDATE_ORG_NAME/stands_index_input.json') as f:
        data = json.load(f)

    # Prompt user for new organization name
    new_org_name = input("Enter the new organization name: ")

    # Prompt user if they want to update the organization name for all stands
    update_all = input("Do you want to update the organization name for all stands? (y/n)")

    # Extract fields for each stand
    stands = []
    for stand in data['stands']:
        stand_data = {
            'id': stand['id'],
            'organization_name': stand['organization_name'] if update_all.lower() == 'n' else new_org_name,
            'uuid': stand['uuid']
        }
        stands.append(stand_data)

    output_data = {'stands': stands}

    # Export extracted data to JSON file
    with open('scripts/STAND_UPDATE_ORG_NAME/stands_index_output.json', 'w') as f:
        json.dump(output_data, f, indent=2)
