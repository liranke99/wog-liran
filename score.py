import os
from utils import SCORES_FILE_NAME, BAD_RETURN_CODE


def add_score(difficulty):
    points_of_winning = (difficulty * 3) + 5
    try:
        if os.path.exists(SCORES_FILE_NAME):
            with open(SCORES_FILE_NAME, 'r') as file:
                current_score = int(file.read().strip())
        else:
            current_score = 0

        new_score = current_score + points_of_winning
        with open(SCORES_FILE_NAME, 'w') as file:
            file.write(str(new_score))
    except Exception as e:
        print(f"Error updating score: {e}")
        return BAD_RETURN_CODE
