import random


def play(difficulty):
    secret_number = random.randint(1, 100)
    attempts = 10 - difficulty

    print(f"Guess the number between 1 and 100. You have {attempts} attempts.")

    for attempt in range(attempts):
        guess = int(input("Enter your guess: "))
        if guess == secret_number:
            print("Congratulations! You won!")
            return True
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")

    print(f"Sorry, you didn't guess the number. The correct number was {secret_number}.")
    return False
