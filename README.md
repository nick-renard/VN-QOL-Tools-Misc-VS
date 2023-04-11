# Instructions
Use these instructions as a guide when you are first starting out with the tools.

## Bulk Transition Orders Tool (**NOT IN PRODUCTION YET**)
This tool contains two folders, [ORDER_INDEX_JSON_FILE](https://github.com/nick-renard/VN-QOL-Tools-Misc-VS/tree/main/ORDER_INDEX_BULK_TRANSITION/ORDER_INDEX_JSON_FILE) and [ORDER_UUID_TEXT_FILE](https://github.com/nick-renard/VN-QOL-Tools-Misc-VS/tree/main/ORDER_INDEX_BULK_TRANSITION/ORDER_UUID_TEXT_FILE). 

The ORDER_INDEX_JSON_FILE folder is used when you are dropping the Orders Index (from PostMan or Orders App) response into the input file. When you run the program, it will parse the JSON into the proper request format. It will also ask you what order state you want the orders to be placed in. The order state is case-sensitive so be cautious. 

The ORDER_UUID_TEXT_FILE allows you to drop order UUIDs into the input file instead of the JSON response from the Orders Index. Each UUID should be on it's own line.


### PostMan Request Format to Transition Orders
_Operator App APIs > Orders > Bulk Order State Transition_

Request:
```
PUT Bulk Order State Transition
```

Body:
```JSON
{
    "order_uuids": [ 
        "order_uuid_1", 
        "order_uuid_2"
        ],
    "new_state": "completed"
}
```

## Update Stand Org Name

The [STAND_UPDATE_ORG_NAME](https://github.com/nick-renard/VN-QOL-Tools-Misc-VS/tree/main/STAND_UPDATE_ORG_NAME) tool allows you to drop the Stand Index (from PostMan or Menu Manager) response into the input file where it will output the request neccessary to change the **organization_name**. When running the program, it will ask you what the new **organization_name** should be. 

### PostMan Request Format to Update Stand Organization Name
_VenueNext Integrator APIs > Content Management > Stands_

Request:
```
PUT Stand Update V1
```

Body:
```JSON
{
  "stands": [
    {
      "id": 3501,
      "organization_name": "this_new_org_name",
      "uuid": "4e2e0762-b782-467f-9c69-9a80c8919f48"
    },
    {
      "id": 3498,
      "organization_name": "this_new_org_name",
      "uuid": "6e42a86b-5a6d-4937-8df5-bea2c0916ed2"
    }
    ]
}
```

## VNAPI True Loyalty Balances

The [VNAPI_BALANCES_CONVERSION_TOTAL](https://github.com/nick-renard/VN-QOL-Tools-Misc-VS/tree/main/VNAPI_BALANCES_CONVERSION_TOTAL) folder allows you to drop the VNAPI balance request into the input file where it will generate a CSV file with the Account ID and the associated balance. This will also create a modal with the total outstanding balance for that instance. Clicking the "Copy to Clipboard and Close" will copy the total outstanding balance to your clipboard. 

### PostMan Request Format to RETRIEVE the Information from VNAPI
_Operator App APIs > Loyalty_

Request:
```
GET Account Balances (VNAPI)
```
Note for above: this is instance specific, you will need to supply 'null' or each instance for every request

Body:
```JSON
NONE
```


## LTM Exports

This tool will not be used that often but will be nice to have if many merchants need to be created at once. 

The [LTM_EXPORT_BULK_TOKENS](https://github.com/nick-renard/VN-QOL-Tools-Misc-VS/tree/main/LTM_EXPORT_BULK_TOKENS) folder allows you to drop the API Settings response from LTM in the "input" file to generate a CSV of the MID Names, Merchant Token, and Platform (VNBackend or Ordernext).

If you need help with this tool, please ask @nick-renard
