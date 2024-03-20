import json

line ="\n"
def run():
    with open("scripts/ORDER_INDEX_BULK_TRANSITION/ORDER_INDEX_JSON_FILE/order_index_input.json") as file:
        data = json.load(file)

    for item in data:
        print(f"\"{item['uuid']}\"")

    uuids = [item["uuid"] for item in data]
    print("\nOrder states are case sensitive. Examples: 'completed', 'refunded', 'completed'")
    new_state = input("Enter the new state for the orders to transition to: ")

    output_dict = {"order_uuids": uuids, "new_state": new_state}

    with open("scripts/ORDER_INDEX_BULK_TRANSITION/ORDER_INDEX_JSON_FILE/order_index_output.json", "w") as file:
        json.dump(output_dict, file, indent=4)
        
        
import json

line ="\n"
def run():
    with open("scripts/ORDER_INDEX_BULK_TRANSITION/ORDER_INDEX_JSON_FILE/order_index_input.json") as file:
        data = json.load(file)

    for item in data:
        print(f"\"{item['uuid']}\"")

    uuids = [item["uuid"] for item in data]
    
    states = ['processing', 'completed', 'refunded', 'authorization_failed'] # Add your own states here
    
    print("\nAvailable order states are:")
    for state in states:
        print(f"- {state}")
    
    new_state = input("Enter the number of the state for the orders to transition to: ")
    
    if not new_state.isdigit() or int(new_state) < 1 or int(new_state) > len(states):
        print("Invalid input. Please enter a number from 1 to", len(states))
        return
    
    new_state = states[int(new_state) - 1]
    output_dict = {"order_uuids": uuids, "new_state": new_state}

    with open("scripts/ORDER_INDEX_BULK_TRANSITION/ORDER_INDEX_JSON_FILE/order_index_output.json", "w") as file:
        json.dump(output_dict, file, indent=4)
