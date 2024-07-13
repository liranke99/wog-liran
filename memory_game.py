import random
import time

def generate_sequence(difficulty):
    return [random.randint(1, 101) for _ in range(difficulty)]

def get_list_from_user(difficulty):
    user_input = input(f"Enter the sequence of {difficulty} numbers separated by space: ")
    return list(map(int, user_input.split()))

def is_list_equal(sequence, user_sequence):
    return sequence == user_sequence

def clear_screen():
    # Simulate clearing the screen by printing newlines
    print("\n" * 100)

def play(difficulty):
    sequence = generate_sequence(difficulty)
    print(f"Remember this sequence: {sequence}")
    time.sleep(0.7)
    clear_screen()  # Simulate clearing the screen after showing the sequence
    user_sequence = get_list_from_user(difficulty)
    if is_list_equal(sequence, user_sequence):
        print("You remembered the sequence correctly!")
        return True
    else:
        print("Sorry, that was incorrect.")
        return False
