from hungman import game
from hungman import words
from hungman import io


def play(words_list, max_tries: int):
    print("game started...")
    state = game.init_state(words.choose_secret_word(words_list), max_tries)
    max_tries = 10
    print(game.render_display(state))
    while state["secret"] != state["display"] or len(state["guesses"]) < state["max_tries"]:
        ch = io.prompt_guess()



    print("game ended...")
    return None

if __name__ == '__main__':
    play(words.words, 6)