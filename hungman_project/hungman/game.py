import io, words, main

def init_state(secret, max_tries = 10):
    return {"secret": secret,
            "display": [],
            "guesses": (),
            "wrong_guesses": 0,
            "max_tries": max_tries
    }

def validate_guess(ch: str, guessed: set[str]):
    return

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




