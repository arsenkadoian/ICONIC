import random

def greet_the_user(username: str):
    """[This function greets the user by the typed-in name.]
    """
    print("Hello:", username.capitalize() + "!")

def generate_random_integer() -> int:
    """[This function will generate an integer between a pre-specified interval and returns that integer.]

    Returns:
        int: [The generated integer.]
    """
    generated_integer = random.randint(0, 5)
    return generated_integer

def game_method(generated_integer_recieved: int, username: str):    
    """[This is function takes two input arguments and gives the player the opportunity to guess the generated integer.]

    Args:
        generated_integer_recieved (int): [The generated integer by the previous function.]
        username (str): [The name that the user has typed in.]

    Returns:
        [type]: [The number of total guesses by the player.]
    """
    total_guesses = 0
    while True:
        try:
            guessed_integer = int(input("Make a guess: "))
            if guessed_integer < generated_integer_recieved:
                print("The guessed value is lower than the generated one. Try again.")
                total_guesses +=1
            elif guessed_integer > generated_integer_recieved:
                print("The guessed value is higher than the generated one. Try again.")
                total_guesses +=1
            else guessed_integer == generated_integer_recieved:
                print("CORRECT!")
                total_guesses +=1 
                print(f"{username.capitalize()}: Guesses {total_guesses}")
                break
        except ValueError:
            print("The argument is not an integer. Please type in one.")
    return total_guesses


def write_to_file(name_of_player: str, total_trials: int):
    f = open("High score.txt", "a")
    f.write(f"{name_of_player.capitalize()}: Guesses {str(total_trials)}.\n" )
    f.close()

def continue_or_not(done: bool) -> bool:
    """[This function asks the user whether hen wants to re-play or not.]
    
    Args:
        done (bool): [THe boolean variable that is going to be set whether 
        the player wants to player another round or not.]

    Returns:
        bool: [The boolean value that is also an answer whether the 
            player wants to player another round or not.]
    """
    IDontKnow = True
    while IDontKnow:
        answer = str(input("Play again? Make your choice: \n [Y]ES \n [N]O \n Choice: "))
        if answer.upper() == 'Y':
            print("Alright! Lets see if it will take you less trials this time ;)")
            done = False
            IDontKnow = False
        elif answer.upper() =='N':
            print("HAVE A NICE DAY! BYE!")
            IDontKnow = False
        else:
            print("Answer only by [Y]es or [N]o.")
    return done

def display_leaderboard():
    """[This method will sort the leaderboard and display it.]
    """
    f = open("High score.txt", "r")
    lines = f.readlines()
    sorted_scorelist = sorted(lines, key = lambda line: line.split()[-1])
    for leader in sorted_scorelist:
        print(leader.strip())