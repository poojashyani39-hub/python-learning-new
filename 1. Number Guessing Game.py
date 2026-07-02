import random #for generating random numbers


def get_valid_guess():
    #use for valid input from user between 1 and 100
    while True:
        try:
            guess = int(input("Enter your guess (1-100): ")) 

            if 1 <= guess <= 100: 
                return guess
            else: #if input is not in range, print error message
                print("Please enter a number between 1 and 100.")

        except ValueError: #if input is not an integer, print error message
            print("Invalid input! Please enter a valid integer.")


def number_guessing_game(): 
    #main function for number guessing game
    secret_number = random.randint(1, 100) #generate a random number between 1 and 100
    attempts = 0

    
    print(" Welcome to the Number Guessing Game")
    print(" Guess a number between 1 and 100")

    while True:
        guess = get_valid_guess()
        attempts += 1 #increment attempts for each guess

        if guess < secret_number: #if the guess is less than the secret number, print "Too Low" otherwise too high
            print("Too Low\n")
        elif guess > secret_number:
            print("Too High\n")
        else:
            print("\nCorrect!")
            print("Congratulations!")
            print(f"You guessed the number in {attempts} attempts.")
            break


if __name__ == "__main__":
    number_guessing_game() #call the main function to start the game