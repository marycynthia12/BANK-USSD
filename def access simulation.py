pin = 2009

# ================= ACCOUNTS ================= #
accounts = {
    "1": {
        "number": "1919xxxxxx65",
        "balance": 200000
    },

    "2": {
        "number": "8773xxxxxx88",
        "balance": 1000000
    },

    "3": {
        "number": "3578xxxxxx73",
        "balance": 800000
    }
}

# ================= FUNCTIONS ================= #

def check_pin():
    user_pin = int(input("Enter your pin: "))
    if user_pin == pin:
        return True
    else:
        print("Invalid pin")
        return False

def select_account():
    print("""
    \nSelect Account
    1. 1919xxxxxx65
    2. 8773xxxxxx88
    3. 3578xxxxxx73
    """)
    return input("Choose account: ")

def transaction_success():
    print("Transaction Successful")

def recharge_success():
    print("Recharge Successful")

# ================= MAIN MENU ================= #
print("""
ACCESS BANK
1. Check Balance
2. Transfer
3. Airtime
4. Buy Data
5. Pay Bills
6. Enquiry Service
7. Exit
""")
option = input("Choose option: ")

# ================= CHECK BALANCE ================= #
if option == "1":
    account = select_account()
    if account in accounts:
        if check_pin():
            print(
                f"Your balance on account "
                f"{accounts[account]['number']} is "
                f"{accounts[account]['balance']}"
            )
    else:
        print("Invalid account selected")

# ================= TRANSFER ================= #
elif option == "2":
    amount = int(input("Enter amount: "))
    account_number = input("Enter account number: ")
    account = select_account()
    if account in accounts:
        if check_pin():
            if amount > accounts[account]["balance"]:
                print("Insufficient funds")
            else:
                accounts[account]["balance"] -= amount
                print(
                    f"{amount} has been transferred "
                    f"to account number {account_number}"
                )
                print(
                    f"Your new balance is "
                    f"{accounts[account]['balance']}"
                )
                transaction_success()
    else:
        print("Invalid account selected")

# ================= AIRTIME ================= #
elif option == "3":
    print("""
    \n1. Self
    2. Others
    """)
    airtime = input("Choose option: ")
    if airtime == "1":
        account = select_account()
        amount = int(input("Enter amount: "))
        if account in accounts:
            if check_pin():
                if amount > accounts[account]["balance"]:
                    print("Insufficient funds")
                else:
                    accounts[account]["balance"] -= amount
                    recharge_success()
                    print(
                        f"Your new balance is "
                        f"{accounts[account]['balance']}"
                    )
    elif airtime == "2":
        account = select_account()
        phone = input("Enter phone number: ")
        amount = int(input("Enter amount: "))
        if account in accounts:
            if check_pin():
                if amount > accounts[account]["balance"]:
                    print("Insufficient funds")
                else:
                    accounts[account]["balance"] -= amount
                    recharge_success()
                    print(
                        f"Your new balance is "
                        f"{accounts[account]['balance']}"
                    )
    else:
        print("Invalid option")

# ================= BUY DATA ================= #
elif option == "4":
    print("""
    \n1. Self
    2. Others
    """)
    data = input("Choose option: ")
    if data == "1":
        account = select_account()
        amount = int(input("Enter amount: "))
        if account in accounts:
            if check_pin():
                if amount > accounts[account]["balance"]:
                    print("Insufficient funds")
                else:
                    accounts[account]["balance"] -= amount
                    recharge_success()
                    print(
                        f"Your new balance is "
                        f"{accounts[account]['balance']}"
                    )
    elif data == "2":
        account = select_account()
        phone = input("Enter phone number: ")
        amount = int(input("Enter amount: "))
        if account in accounts:
            if check_pin():
                if amount > accounts[account]["balance"]:
                    print("Insufficient funds")
                else:
                    accounts[account]["balance"] -= amount
                    recharge_success()
                    print(
                        f"Your new balance is "
                        f"{accounts[account]['balance']}"
                    )
    else:
        print("Invalid option")

# ================= PAY BILLS ================= #

elif option == "5":
    print("""
    \n1. DSTV
    2. GOTV
    """)
    bill = input("Choose option: ")
    if bill == "1":
        account = select_account()
        print("""
        \nSelect Package
        1. Access Standalone - 11300
        2. Compact - 19000
        """)
        package = input("Choose package: ")
        decoder = input("Enter decoder number: ")
        amount = int(input("Enter amount: "))
        if account in accounts:
            if check_pin():
                if amount > accounts[account]["balance"]:
                    print("Insufficient funds")
                else:
                    accounts[account]["balance"] -= amount
                    transaction_success()
                    print(
                        f"Your new balance is "
                        f"{accounts[account]['balance']}"
                    )
    elif bill == "2":
        account = select_account()
        print("""
        \nSelect Package
        1. GOTV Smallie Monthly - 1300
        2. GOTV Max - 9000
        3. Jinjer - 11000
        """)
        package = input("Choose package: ")
        decoder = input("Enter decoder number: ")
        amount = int(input("Enter amount: "))
        if account in accounts:
            if check_pin():
                if amount > accounts[account]["balance"]:
                    print("Insufficient funds")
                else:
                    accounts[account]["balance"] -= amount
                    transaction_success()
                    print(
                        f"Your new balance is "
                        f"{accounts[account]['balance']}"
                    )
    else:
        print("Invalid option")

# ================= ENQUIRY SERVICE ================= #

elif option == "6":
    print("""
    \nACCESS BANK ENQUIRY SERVICE
    1. Mini Statement
    2. BVN Enquiry
    3. A/C Number Enquiry
    """)
    enquiry = input("Choose option: ")
    if enquiry == "1":
        account = select_account()
        if check_pin():
            print("An SMS will be sent to you shortly")
    elif enquiry == "2":
        if check_pin():
            print("Your BVN is 3648364830")
    elif enquiry == "3":
        if check_pin():
            print("An SMS will be sent shortly")
    else:
        print("Invalid option")

# ================= EXIT ================= #

elif option == "7":

    print("Thank you for banking with ACCESS BANK")

# ================= INVALID OPTION ================= #

else:
    print("Invalid option selected")