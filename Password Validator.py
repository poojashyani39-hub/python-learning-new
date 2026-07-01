# Function to check password strength
def validate_password():

    # Take password input from user
    password = input("Enter Password: ")

    # Variables to check each rule
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    # List of special characters
    special_characters = "!@#$%^&*()-_=+[]{};:'\",.<>?/\\|"

    # Check password length
    if len(password) < 8:
        print("Invalid Password")
        print("Password must contain at least 8 characters.")
        return

    # Check each character in password
    for char in password:

        # Check uppercase letter
        if char.isupper():
            has_upper = True

        # Check lowercase letter
        elif char.islower():
            has_lower = True

        # Check digit
        elif char.isdigit():
            has_digit = True

        # Check special character
        elif char in special_characters:
            has_special = True

    # Check all password rules
    if has_upper and has_lower and has_digit and has_special:
        print("Valid Password")
    else:
        print("Invalid Password")

        if has_upper == False:
            print("- Password must contain at least one uppercase letter.")

        if has_lower == False:
            print("- Password must contain at least one lowercase letter.")

        if has_digit == False:
            print("- Password must contain at least one digit.")

        if has_special == False:
            print("- Password must contain at least one special character.")


# Call the function
validate_password()