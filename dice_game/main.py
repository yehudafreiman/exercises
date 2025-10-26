import game
from dice_game.utils import roll_two_dices
from dice_game.game import manage_turns, manage_scores, decision_selected


def play_game():

    # Start
    print("* Start game *")

    # Turn
    current_player = manage_turns()
    print(f"--- Player turn: {current_player} ---")

    # Score
    if current_player == "1":
        print(f"Your score: {manage_scores("1")} points, rival score: {manage_scores("2")} points")
    else:
        print(f"Your score: {manage_scores("2")} points, rival score: {manage_scores("1")} points")

    # Decision
    decision = decision_selected()

    # Rolling
    if decision == "r":
        rolling = roll_two_dices()
        print(f"Result of roll: {rolling[0]} & {rolling[1]} >> Total: {rolling[2]} points")

        # Update
        updated_score = manage_scores(current_player)
        updated_score += rolling[2]


    # Passing
    # if decision == "p":
    #     passing = manage_turns()

    # End
    # if current_player == '0':
    #     exit("* End game *")

play_game()











def is_target(score:int):
    pass

def is_exact_hundred(score:int):
    pass

def closer_to_target():
    pass

def tie_breaker(roller):
    pass

def display():
    pass



