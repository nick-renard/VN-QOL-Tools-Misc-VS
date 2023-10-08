import json

def run():
    # Define the input and output file paths
    input_file_path = "input.json"
    output_file_path = "output.json"

    # Load data from the input JSON file
    with open(input_file_path, "r") as input_file:
        data = json.load(input_file)

    # Process the data to set "price" to null for each item and include "uuid"
    output_data = {"menu_items": []}
    for item in data.get("menu_items", []):
        output_item = {
            "uuid": item["uuid"],
            "price": None
        }
        output_data["menu_items"].append(output_item)

    # Create the output JSON file with the updated data
    with open(output_file_path, "w") as output_file:
        json.dump(output_data, output_file, indent=4)

    print(f"Processed data and saved it to {output_file_path}")

run()