import json
import sys

line ="\n"

def run():
    
    with open("ORDER_INDEX_BULK_TRANSITION/ORDER_UUID_TEXT_FILE/order_list_uuids_input.txt") as file:
        uuids = [line.strip() for line in file]
        
    # Print the uuids to the console
    for uuid in uuids:
        print(f"\"{uuid}\"")

    print("\nOrder states are case sensitive. Example: 'completed'\n")
    new_state = input("Enter the new state for the orders to transition to: ")

    output_dict = {"order_uuids": uuids, "new_state": new_state}

    with open("ORDER_INDEX_BULK_TRANSITION/ORDER_UUID_TEXT_FILE/order_list_uuid_output.json", "w") as file:
        json.dump(output_dict, file, indent=4)
        
