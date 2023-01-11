import argparse
from Utils import *


def decide_what_to_do(decision: bool):
    if decision:
        display_leaderboard()
        exit()
    else:
        main(user_name)

def main(user_name: str):
    done = True 
    greet_the_user(user_name)
    the_generated_integer_returned = generate_random_integer()
    result = game_method(the_generated_integer_returned, user_name)
    write_to_file(user_name, result)
    answer = continue_or_not(done)
    decide_what_to_do(answer)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Guessing the generated integer.")
    parser.add_argument('--user-name', help='Enter your name or a username.', required=True, type=str)
    args = parser.parse_args()

    user_name = args.user_name

    main(user_name)