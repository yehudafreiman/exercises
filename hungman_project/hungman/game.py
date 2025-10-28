from hungman_project import main
from hungman_project import hungman

def init_state(secret, max_tries):
    state_game = {"secret": secret,
            "display": '',
            "guesses": [],
            "wrong_guesses": 0,
            "max_tries": max_tries
    }
    return state_game

def validate_guess(ch: str, state: dict):
    letters = ["א", "ב", "ג", "ד", "ה", "ו", "ז", "ח", "ט", "י", "כ", "ל", "מ", "נ", "ס", "ע", "פ", "צ", "ק", "ר", "ש", "ת"]
    if ch not in state["guesses"] and ch in letters and len(ch) == 1:
        return True
    else:
        if ch in state["guesses"]:
            print("You have already tried this letter")
        elif len(ch) > 1:
            print("Only one letter is required")
        else:
            print("This is not a letter")
        return False

def apply_guess(state: dict, ch: str):
    if ch in state["secret"]:
        for i in range(len(state["display"])):
            state["display"][i] == ch
        return True
    else:
        return False

def is_won(state: dict):
    if state["secret"] == state["display"]:
        return True
    return False

def is_lost(state: dict):
    if state["wrong_guesses"] >= state["max_tries"]:
        return True
    return False

def render_display(state: dict):
    for i in range(len(state["secret"])):
        state["display"] += "_ "
    return state["display"]

def render_summary(state: dict):
    return state["secret"]




