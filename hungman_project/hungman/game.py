from hungman_project import main
from hungman_project import hungman

def init_state(secret, max_tries):
    state_game = {"secret": secret,
            "display": [],
            "guesses": (),
            "wrong_guesses": 0,
            "max_tries": max_tries
    }
    return state_game

def validate_guess(ch: str, state: dict):
    if ch not in state["guesses"] and isinstance(ch, str) and len(ch) == 1:
        return True
    else:
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
    word = state["secret"]
    for i in state["secret"]:
        word.replace(state["secret"][i], "_")
    state["display"] = word
    return state["display"]

def render_summary(state: dict):
    return state["secret"]




