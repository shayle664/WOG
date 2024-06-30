import utils
import os


def add_score(difficulty_level):
    try:
        if os.path.exists(utils.SCORES_FILE_NAME):
            with open(utils.SCORES_FILE_NAME, 'r') as file:
                current_score = int(file.readline())
        else:
            current_score = 0
    except (FileNotFoundError, ValueError):
        current_score = 0

    new_score = current_score + (difficulty_level * 3) + 5
    with open(utils.SCORES_FILE_NAME, 'w') as file:
        file.write(str(new_score))

