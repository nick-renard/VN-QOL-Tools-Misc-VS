# Instructions
Use these instructions as a guide when you are first starting out with the tools.

## Bulk Transition Orders Tool
This tool contains two folders, [ORDER_INDEX_JSON_FILE](https://github.com/nick-renard/VN-QOL-Tools-Misc-VS/tree/main/ORDER_INDEX_BULK_TRANSITION/ORDER_INDEX_JSON_FILE) and [ORDER_UUID_TEXT_FILE](https://github.com/nick-renard/VN-QOL-Tools-Misc-VS/tree/main/ORDER_INDEX_BULK_TRANSITION/ORDER_UUID_TEXT_FILE). 

The ORDER_INDEX_JSON_FILE folder is used when you are dropping the Orders Index response into the input file. When you run the program, it will parse the JSON into the proper request format. It will also ask you what order state you want the orders to be placed in. The order state is case-sensitive so be cautious. 

The ORDER_UUID_TEXT_FILE allows you to drop order UUIDs into the input file instead of the JSON response from the Orders Index. Each UUID should be on it's own line.

## Update Stand Org Name

The [STAND_UPDATE_ORG_NAME](https://github.com/nick-renard/VN-QOL-Tools-Misc-VS/tree/main/STAND_UPDATE_ORG_NAME) tool allows you to drop the Stand Index response into the input file where it will output the request neccessary to change the **organization_name**. When running the program, it will ask you what the new **organization_name** should be. 

## VNAPI True Loyalty Balances

The [VNAPI_BALANCES_CONVERSION_TOTAL](https://github.com/nick-renard/VN-QOL-Tools-Misc-VS/tree/main/VNAPI_BALANCES_CONVERSION_TOTAL) folder allows you to drop the VNAPI balance request into the input file where it will generate a CSV file with the Account ID and the associated balance. This will also create a modal with the total outstanding balance for that instance. Clicking the "Copy to Clipboard and Close" will copy the total outstanding balance to your clipboard. 


## LTM Exports

This tool will not be used that often but will be nice to have if many merchants need to be created at once. 

The [LTM_EXPORT_BULK_TOKENS](https://github.com/nick-renard/VN-QOL-Tools-Misc-VS/tree/main/LTM_EXPORT_BULK_TOKENS) folder allows you to drop the API Settings response from LTM in the "input" file to generate a CSV of the MID Names, Merchant Token, and Platform (VNBackend or Ordernext).

If you need help with this tool, please ask @nick-renard

