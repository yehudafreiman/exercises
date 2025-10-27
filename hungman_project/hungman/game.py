from hungman_project import main
from hungman_project import hungman

def init_state(secret, max_tries = 10):
    stat_game = {"secret": secret,
            "display": [],
            "guesses": (),
            "wrong_guesses": 0,
            "max_tries": max_tries
    }
    return stat_game


def validate_guess(ch: str, guesses: set[str]):
    if isinstance(ch, str) and len(ch) == 1:
        return True
    else:
        return False

def apply_guess(state: dict, ch: str):
    return

def is_won(state: dict):
    return

def is_lost(state: dict):
    return

def render_display(state: dict):
    return

def render_summary(state: dict):
    return




