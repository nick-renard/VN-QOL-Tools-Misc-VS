import json

line ="\n"
def run():
    with open("ORDER_INDEX_BULK_TRANSITION/ORDER_INDEX_JSON_FILE/order_index_input.json") as file:
        data = json.load(file)

    for item in data:
        print(f"\"{item['uuid']}\"")

    uuids = [item["uuid"] for item in data]
    print("Order states are case sensitive. Examples: 'completed', 'refunded', 'completed'")
    new_state = input("Enter the new state for the orders to transition to: ")

    output_dict = {"order_uuids": uuids, "new_state": new_state}

    with open("ORDER_INDEX_BULK_TRANSITION/ORDER_INDEX_JSON_FILE/order_index_output.json", "w") as file:
        json.dump(output_dict, file, indent=4)