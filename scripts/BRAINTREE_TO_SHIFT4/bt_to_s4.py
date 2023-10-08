import json

def process_stands(input_file, output_file, merchant_id):
    # Load the input JSON file
    with open(input_file, 'r') as infile:
        data = json.load(infile)
    
    # Extract stands and create a new list with the desired fields
    stands = data.get('stands', [])
    processed_stands = []

    for stand in stands:
        processed_stand = {
            "id": stand.get("id"),
            "uuid": stand.get("uuid"),
            "apple_pay_merchant_id": None,
            "android_pay_merchant_id": None,
            "merchant_account_id": None,
            "merchant_id": merchant_id
        }
        processed_stands.append(processed_stand)

    # Create the output JSON structure
    output_data = {"stands": processed_stands}

    # Write the output JSON to a file
    with open(output_file, 'w') as outfile:
        json.dump(output_data, outfile, indent=4)

if __name__ == "__main__":
    # Input and output file paths
    input_file = "input.json"
    output_file = "output.json"

    # Ask the user for the merchant_id to apply to all stands
    merchant_id = input("Enter the merchant_id to apply to all stands: ")

    # Process the stands data and write to the output file
    process_stands(input_file, output_file, merchant_id)

    print(f"Processed data written to {output_file}")
