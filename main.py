import ORDER_INDEX_BULK_TRANSITION.ORDER_UUID_TEXT_FILE.order_list_uuids as order_list_uuids
import ORDER_INDEX_BULK_TRANSITION.ORDER_INDEX_JSON_FILE.order_index_uuids as order_index_uuids
import STAND_UPDATE_ORG_NAME.stands_index_to_update_org_name as stands_index_to_update_org_name
import VNAPI_BALANCES_CONVERSION_TOTAL.vnapi_balance_export_to_total_and_carrying as vnapi_balance_export_to_total_and_carrying


def main():
    while True:
        print_menu()
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            while True:
                printDisclaimer()
                confirm = input("\nEnter your choice (yes/no): ")
                if confirm == "yes":
                    order_list_uuids.run()
                    printSuccess()
                    break
                elif confirm == "no":
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif choice == "2":
            while True:
                printDisclaimer()
                confirm = input("\nEnter your choice (yes/no): ")
                if confirm == "yes":
                    order_index_uuids.run()
                    printSuccess()
                    break
                elif confirm == "no":
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif choice == "3":
            while True:
                printDisclaimer()
                confirm = input("\nEnter your choice (yes/no): ")
                if confirm == "yes":
                    stands_index_to_update_org_name.run()
                    printSuccess()
                    break
                elif confirm == "no":
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif choice == "4":
            while True:
                printDisclaimer()
                confirm = input("\nEnter your choice (yes/no): ")
                if confirm == "yes":
                    vnapi_balance_export_to_total_and_carrying.run()
                    printSuccess()
                    break
                elif confirm == "no":
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif choice == "5":
            print("\nExiting the program...")
            print("")
            print('\x1b[1;36;45m' + '  Thanks for using Nicks super awesome QOL scripts! :D  ' + '\x1b[0m')
            print("")
            print("")
            break
        else:
            print("Invalid choice. Please try again.\n")
            
def print_menu():
    print("==========================================================")
    print("======================= Main Menu ========================")
    print("==========================================================\n")
    print('\x1b[0;37;41m' + 'Before running any of the scripts, please make sure you' + '\x1b[0m')
    print('\x1b[0;37;41m' + 'have added the required information to the input files!' + '\x1b[0m')
    print("")
    print("Please select an option:")
    print("1. Order State Transitions -- List of UUIDs in a text file")
    print("2. Order State Transitions -- JSON response in a JSON file")
    print("3. Stand Organization Name Update")
    print("4. VNAPI Response Conversion to CSV")
    print("5. Exit\n")

def printSuccess():
    print("")
    print('\x1b[0;30;42m' + 'The JSON file has been created. Please copy the contents from' + '\x1b[0m')
    print('\x1b[0;30;42m' + 'the output file and paste into the body of your Postman request.' + '\x1b[0m')
    print("")
    print("")
    
def printDisclaimer():
    print("\nPlease make sure you have updated the input files.")
    print("If you have updated the input files, please type 'yes' to continue.")
    print("If you have not updated the input files, please type 'no' to go back to the main menu.")
            
if __name__ == "__main__":
    main()