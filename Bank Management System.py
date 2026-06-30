
# List to store all bank accounts
accounts = []


# Function to create a new account
def create_account():

    # Validate Account Number
    while True:
        account_number = input("Enter Account Number: ").strip()

        if account_number == "":
            print("Account Number cannot be empty.")
        elif not account_number.isdigit():
            print("Account Number should contain only digits.")
        else:
            break

    # Validate Account Holder Name
    while True:
        account_holder = input("Enter Account Holder Name: ").strip()

        if account_holder == "":
            print("Account Holder Name cannot be empty.")
        elif not account_holder.replace(" ", "").isalpha():
            print("Name should contain only letters and spaces.")
        else:
            break

    # Validate Opening Balance
    while True:
        balance = input("Enter Opening Balance: ").strip()

        try:
            balance = float(balance)

            if balance < 0:
                print("Balance cannot be negative.")
            else:
                break

        except ValueError:
            print("Please enter a valid amount.")

    # Create account dictionary
    account = {
        "account_number": account_number,
        "account_holder": account_holder,
        "balance": balance
    }

    # Add account to the list
    accounts.append(account)

    print("Account Created Successfully.")


# Function to deposit money
def deposit_money():

    # Check if accounts exist
    if len(accounts) == 0:
        print("No accounts found.")
        return

    account_number = input("Enter Account Number: ").strip()

    found = False

    # Search account
    for account in accounts:

        if account["account_number"] == account_number:

            while True:
                amount = input("Enter Deposit Amount: ").strip()

                try:
                    amount = float(amount)

                    if amount <= 0:
                        print("Amount must be greater than zero.")
                    else:
                        break

                except ValueError:
                    print("Please enter a valid amount.")

            # Add amount to balance
            account["balance"] += amount

            print("Money Deposited Successfully.")
            print("Current Balance:", account["balance"])

            found = True
            break

    if found == False:
        print("Account not found.")


# Function to withdraw money
def withdraw_money():

    if len(accounts) == 0:
        print("No accounts found.")
        return

    account_number = input("Enter Account Number: ").strip()

    found = False

    # Search account
    for account in accounts:

        if account["account_number"] == account_number:

            while True:
                amount = input("Enter Withdraw Amount: ").strip()

                try:
                    amount = float(amount)

                    if amount <= 0:
                        print("Amount must be greater than zero.")
                    elif amount > account["balance"]:
                        print("Insufficient Balance.")
                    else:
                        break

                except ValueError:
                    print("Please enter a valid amount.")

            # Deduct amount
            account["balance"] -= amount

            print("Money Withdrawn Successfully.")
            print("Current Balance:", account["balance"])

            found = True
            break

    if found == False:
        print("Account not found.")


# Function to check account balance
def check_balance():

    if len(accounts) == 0:
        print("No accounts found.")
        return

    account_number = input("Enter Account Number: ").strip()

    found = False

    # Search account
    for account in accounts:

        if account["account_number"] == account_number:

            print("\nAccount Details")
            print("Account Number :", account["account_number"])
            print("Account Holder :", account["account_holder"])
            print("Balance        :", account["balance"])

            found = True
            break

    if found == False:
        print("Account not found.")


# Function to display all accounts
def display_accounts():

    if len(accounts) == 0:
        print("No accounts found.")
        return

    print("\n----- Account List -----")

    # Display every account
    for account in accounts:

        print("Account Number :", account["account_number"])
        print("Account Holder :", account["account_holder"])
        print("Balance        :", account["balance"])
        print("----------------------------")


# Main Menu
while True:

    print("\n===== Bank Management System =====")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Display All Accounts")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    # Create Account
    if choice == "1":
        create_account()

    # Deposit Money
    elif choice == "2":
        deposit_money()

    # Withdraw Money
    elif choice == "3":
        withdraw_money()

    # Check Balance
    elif choice == "4":
        check_balance()

    # Display All Accounts
    elif choice == "5":
        display_accounts()

    # Exit Program
    elif choice == "6":
        print("Thank you for using Bank Management System.")
        break

    # Invalid Choice
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")

