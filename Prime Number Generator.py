# Function to generate prime numbers
def generate_prime_numbers():

    # Get start number from user
    while True:
        start = input("Enter Start Number: ").strip()

        if start == "":
            print("Start number cannot be empty.")
        elif not start.isdigit():
            print("Start number should contain only digits.")
        else:
            start = int(start)
            break

    # Get end number from user
    while True:
        end = input("Enter End Number: ").strip()

        if end == "":
            print("End number cannot be empty.")
        elif not end.isdigit():
            print("End number should contain only digits.")
        else:
            end = int(end)
            break

    # Check valid range
    if start > end:
        print("Start number should be less than or equal to End number.")
        return

    print("\nPrime Numbers:")

    # Check every number in the range
    for number in range(start, end + 1):

        # Skip numbers less than 2
        if number < 2:
            continue

        is_prime = True

        # Check if number is divisible
        for i in range(2, number):

            if number % i == 0:
                is_prime = False
                break

        # Print prime number
        if is_prime:
            print(number)


# Call the function
generate_prime_numbers()