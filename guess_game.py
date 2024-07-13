import random

def generate_number(difficulty):
    return random.randint(0, difficulty)

def get_guess_from_user(difficulty):
    while True:
        try:
            guess = int(input(f"Guess a number between 0 and {difficulty}: "))
            if 0 <= guess <= difficulty:
                return guess
            else:
                print(f"Please enter a number between 0 and {difficulty}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def compare_results(secret_number, user_guess):
    return secret_number == user_guess

def play(difficulty):
    secret_number = generate_number(difficulty)
    user_guess = get_guess_from_user(difficulty)
    if compare_results(secret_number, user_guess):
        print("You guessed correctly!")
        return True
    else:
        print("Sorry, that was incorrect.")
        return False
