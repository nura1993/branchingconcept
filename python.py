import random

def guess_number():
    number_to_guess = random.randint(1, 10)
    attempts = 0

    print("Welcome Guessing Game!")
    print("I'm thinking of a number between 1 and 10.")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess == number_to_guess:
            print(f"🎉 Congratulations! You guessed it in {attempts} tries.")
            break
        elif guess < number_to_guess:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

# Run the game
guess_number()
