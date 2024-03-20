import json
import os

def generate_json_blob(uuids, venue_uuid, merchant_token):
    stands = []
    for uuid in uuids:
        stand = {
            "uuid": uuid.strip(),
            "merchant_token": merchant_token,
            "venue_uuid": venue_uuid
        }
        stands.append(stand)

    json_blob = {
        "stands": stands
    }

    return json_blob

def save_json_blob(json_blob, filename):
    with open(filename, 'w') as file:
        json.dump(json_blob, file, indent=4)

def main():
    file_path = "scripts/STANDS_MERCH/uuid_file.txt"  # Specify the path to the text file containing UUIDs
    venue_uuid = "6184bec2-cdc5-4dc0-b57f-a3f603f99d0e"  # Specify the venue_uuid to apply to all objects
    merchant_token = "<<REDACTED>>"  # Specify the merchant token to apply to all objects
    output_filename = "output.json"  # Specify the desired output filename

    with open(file_path, 'r') as file:
        uuids = file.readlines()

    json_blob = generate_json_blob(uuids, venue_uuid, merchant_token)

    output_directory = os.path.dirname(file_path)
    output_path = os.path.join(output_directory, output_filename)

    os.makedirs(output_directory, exist_ok=True)  # Create the output directory if it doesn't exist
    save_json_blob(json_blob, output_path)

    print("JSON blob saved as:", output_path)

main()
