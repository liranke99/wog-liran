import random
from utils import screen_cleaner


def play(difficulty):
    sequence_length = difficulty + 2
    sequence = [random.randint(1, 101) for _ in range(sequence_length)]

    screen_cleaner()
    print("Memorize the sequence:")
    print(sequence)
    input("Press Enter when you are ready to proceed...")

    screen_cleaner()
    guess = input("Enter the sequence, separated by spaces: ").split()
    guess = [int(num) for num in guess]

    if guess == sequence:
        print("Congratulations! You won!")
        return True
    else:
        print(f"Sorry, the correct sequence was {sequence}.")
        return False
