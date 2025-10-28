import game

def prompt_guess():
    ch = input("enter one letter: ")
    return ch

def print_status(state: dict):
    hidden_word = state["display"]
    num_correct_guesses = len(state["guesses"])
    num_guesses_left = len(state["max_tries"]) - (len(state["max_tries"]) + len(state["wrong_guesses"]))
    print(f"hidden word: {hidden_word}, num correct guesses: {num_correct_guesses}, num guesses left{num_guesses_left}",end="\n")
    return None


def print_result(state: dict):
    if game.is_won(state):
        print("you won!")
    if game.is_lost(state):
        print("you lost")
    print(state["display"])
    print(state["guesses"])
    return None


