import json
import csv

def json_to_csv(json_file, csv_file):
    # Read the JSON file
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Extract the keys from the JSON data
    keys = set()
    for item in data.values():
        keys.update(item.keys())

    # Write the JSON data to CSV
    with open(csv_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data.values())

    print(f"CSV file '{csv_file}' created successfully.")

# Example usage
json_file = 'JSON_TO_CSV/json_input.json'
csv_file = 'JSON_TO_CSV/json_output.csv'
json_to_csv(json_file, csv_file)

