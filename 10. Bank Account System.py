
# Class to create a Bank Account
class BankAccount:

    # Constructor to initialize account details
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    # Method to deposit money
    def deposit(self):

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
        self.balance += amount

        print("Amount Deposited Successfully.")
        print("Current Balance:", self.balance)

    # Method to withdraw money
    def withdraw(self):

        while True:
            amount = input("Enter Withdraw Amount: ").strip()

            try:
                amount = float(amount)

                if amount <= 0:
                    print("Amount must be greater than zero.")

                elif amount > self.balance:
                    print("Insufficient Balance.")

                else:
                    break

            except ValueError:
                print("Please enter a valid amount.")

        # Deduct amount from balance
        self.balance -= amount

        print("Amount Withdrawn Successfully.")
        print("Current Balance:", self.balance)

    # Method to check account balance
    def check_balance(self):

        print("\n----- Account Details -----")
        print("Account Number :", self.account_number)
        print("Account Holder :", self.account_holder)
        print("Current Balance:", self.balance)


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


# Create object of BankAccount class
account = BankAccount(account_number, account_holder, balance)


# Main Menu
while True:

    print("\n===== Bank Account System =====")
    print("1. Deposit Amount")
    print("2. Withdraw Amount")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    # Deposit Money
    if choice == "1":
        account.deposit()

    # Withdraw Money
    elif choice == "2":
        account.withdraw()

    # Check Balance
    elif choice == "3":
        account.check_balance()

    # Exit Program
    elif choice == "4":
        print("Thank you for using Bank Account System.")
        break

    # Invalid Choice
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")

