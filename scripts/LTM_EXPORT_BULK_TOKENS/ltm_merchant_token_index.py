import json


def read_json_file(file_path):
    with open(file_path, "r") as ltm_file:
        content = ltm_file.read()
        try:
            ltm_data = json.loads(content)
            return ltm_data
        except json.JSONDecodeError as e:
            valid_json = content[:e.pos]
            ltm_data = json.loads(valid_json)
            return ltm_data

def run():
    # Read the input JSON file
    data = read_json_file("LTM_EXPORT_BULK_TOKENS/ltm_merchant_token_index_input.json")
    line = '\n'

    # Iterate through the list and print 'merchant_name' and 'apiGUID'
    for entry in data["rows"]:
        print(f" {entry['merchantName']},{entry['apiGUID']},{entry['clientName']}")

    # Write the output to a text file with each entry on a new line
    # Clear the file if it already exists

    with open("LTM_EXPORT_BULK_TOKENS/ltm_merchant_token_index_output.txt", "w") as file:
        # If the file already exists, clear it
        file.truncate(0)
        for entry in data["rows"]:
            file.write(f"{entry['merchantName']},{entry['apiGUID']},{entry['clientName']}")
            file.write(line)

    # Write the output to a CSV file with each entry on a new line
    # Clear the file if it already exists

    with open("LTM_EXPORT_BULK_TOKENS/ltm_merchant_token_index_output.csv", "w") as file:
        file.truncate(0)
        file.write("merchantName, apiGUID, clientName")
        file.write(line)
        for entry in data["rows"]:
            file.write(f"{entry['merchantName']},{entry['apiGUID']},{entry['clientName']}")
            file.write(line)
