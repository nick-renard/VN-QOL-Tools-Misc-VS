import os
import pandas as pd
import json

def csv_to_json(csv_filename, object_type):
    # Build the path to the CSV file in the same directory as the Python file
    csv_path = os.path.join(os.path.dirname(__file__), csv_filename)
    
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_path)
    
    # Convert DataFrame to a list of dictionaries
    records_list = df.to_dict(orient='records')
    
    # Create the JSON object
    json_obj = {object_type: records_list}
    
    # Convert to a JSON-formatted string
    json_str = json.dumps(json_obj, indent=4)
    
    # Build the path to save the JSON file in the same directory
    json_filename = csv_filename.replace('.csv', '.json')
    json_path = os.path.join(os.path.dirname(__file__), json_filename)
    
    # Save the JSON string to a file
    with open(json_path, 'w') as f:
        f.write(json_str)
    
    return json_path

# User input for CSV file name and object type
csv_filename = input("Enter the name of the CSV file (located in the same directory as this Python file): ")
object_type = input("Enter the object type (key) for the JSON (ex: affiliations): ")

# Perform the conversion
json_path = csv_to_json(csv_filename, object_type)
print(f"JSON file has been saved to: {json_path}")

csv_to_json()