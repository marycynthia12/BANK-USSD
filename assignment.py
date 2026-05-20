# name = "mary"
# print(name)
print("ACCESS BANK")
print("1. Check Balance")
print("2. Transfer")
print("3. Airtime")
print("4. Buy Data")
print("5. Pay Bills")
print("6. Enquiry Service")

option = input("Select an option: ")
if option == "1":
    print("Check Balance")
if option == "2":
    print("transfer")
if option == "3":
    print("Airtime")
if option == "4":
    print("Buy Data")
if option == "5":
    print("Pay Bills")
if option == "6":
    print("Enquiry Service")
else:
    print("Invalid option")

if option == "1":

        print("\nSelect Account")
        print("1. 1919xxxxxx65")
        print("2. 8773xxxxxx88")
        print("3. 3578xxxxxx73")

        account = input("Choose account: ")

        pin = input("Enter pin: ")

        if account == "1":
            print("Your balance on account 1919xxxxxx65 is 2000")

        elif account == "2":
            print("Your balance on account 8773xxxxxx88 is 1000000")

        elif account == "3":
            print("Your balance on account 3578xxxxx73 is 800000")

        else:
            print("Invalid account selected")

elif option == "2":

        amount = input("Enter amount: ")
        account_number = input("Enter account number: ")

        print("\nSelect Bank")
        print("1. Kuda Bank")
        print("2. Mkudi")
        print("3. First Bank")

        bank = input("Choose bank: ")

        pin = input(
            "Transfer amount to Udeh Marycynthia, to continue enter your pin: "
        )

        print("Transfer Successful")

elif option == "3":

        print("\n1. Self")
        print("2. Others")

        airtime = input("Choose option: ")

        if airtime == "1":

            print("\nSelect Account")
            print("1. 1919xxxxxx65")
            print("2. 8773xxxxxx88")
            print("3. 3578xxxxx73")

            account = input("Choose account: ")

            amount = input("Enter amount: ")

            print("Recharge Successful")

        elif airtime == "2":

            print("\nSelect Account")
            print("1. 1919xxxxxx65")
            print("2. 8773xxxxxx88")
            print("3. 3578xxxxx73")

            account = input("Choose account: ")

            amount = input("Enter amount: ")
            phone = input("Enter phone number: ")

            print("Recharge Successful")

        else:
            print("Invalid option")

elif option == "4":

        print("\n1. Self")
        print("2. Others")

        data = input("Choose option: ")

        if data == "1":

            print("\nSelect Account")
            print("1. 1919xxxxxx65")
            print("2. 8773xxxxxx88")
            print("3. 3578xxxxx73")

            account = input("Choose account: ")

            amount = input("Enter amount: ")

            print("Recharge Successful")

        elif data == "2":

            print("\nSelect Account")
            print("1. 1919xxxxxx65")
            print("2. 8773xxxxxx88")
            print("3. 3578xxxxx73")

            account = input("Choose account: ")

            amount = input("Enter amount: ")
            phone = input("Enter phone number: ")

            print("Recharge Successful")

        else:
         print("Invalid option")

elif option == "5":

        print("\n1. DSTV")
        print("2. GOTV")

        bill = input("Choose option: ")

        if bill == "1":

            print("\nSelect Account")
            print("1. 1919xxxxxx65")
            print("2. 8773xxxxxx88")
            print("3. 3578xxxxx73")

            account = input("Choose account: ")

            print("\nSelect Option")
            print("1. Asis Standalone for 11300 naira")
            print("2. Compact for 19000")

            package = input("Choose package: ")

            decoder = input("Enter decoder number: ")

            amount = input("Enter amount: ")

            print("Successful")

        elif bill == "2":

            print("\nSelect Account")
            print("1. 1919xxxxxx65")
            print("2. 8773xxxxxx88")
            print("3. 3578xxxxx73")

            account = input("Choose account: ")

            print("\nSelect Option")
            print("1. GOTV Smallie Monthly for 1300")
            print("2. GOTV Max for 9000")
            print("3. Jinjer for 110000")

            package = input("Choose package: ")

            decoder = input("Enter decoder number: ")

            amount = input("Enter amount: ")

            print("Successful")

        else:
            print("Invalid option")


elif option == "6":

        print("\n====== ACCESS BANK ENQUIRY SERVICE ======")
        print("1. Mini Statement")
        print("2. BVN Enquiry")
        print("3. A/C Number Enquiry")

        enquiry = input("Choose option: ")

        if enquiry == "1":

            account = input("Enter account: ")
            pin = input("Enter pin: ")

            print("An SMS will be sent to you shortly")

        elif enquiry == "2":

            pin = input(
                "To get Bank Verification Number, enter pin: "
            )

            print("Your BVN is 3648364830")

        elif enquiry == "3":

            pin = input(
                "Get account number, enter pin: "
            )

            print("An SMS will be sent shortly")

        else:
            print("Invalid option")
            
elif option == "7":

        print("Thank you for banking with ACCESS BANK")
else:
        print("Invalid option selected")

