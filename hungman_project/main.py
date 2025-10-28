from hungman import game
from hungman import words
from hungman import io


def play(words_list, max_tries: int):
    print("game started...")
    state = game.init_state(words.choose_secret_word(words_list), max_tries)
    max_tries = 10
    print(game.render_display(state))
    while state["secret"] != state["display"] or (len(state["guesses"]) + state["wrong_guesses"]) < state["max_tries"]:
        guess_input = io.prompt_guess()
        is_valid = game.validate_guess(guess_input, state)
        if is_valid:
            for l in state["secret"]:
                if guess_input == l:
                    state["display"].replace("_", guess_input)
                    print("success")
                else:
                    print("fail")
                    state["wrong_guesses"] += 1
        else:
            continue
    print("game ended...")
    return None

if __name__ == '__main__':
    play(words.words, 6)