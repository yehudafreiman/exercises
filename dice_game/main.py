import game
from dice_game.utils import roll_two_dices
from dice_game.game import manage_turns, decision_selected


def play_game():
    p1_score = 0
    p2_score = 0

    # Start
    print("* Start game *")

    run = True
    while run:

        # Turn
        current_player = manage_turns()
        print(f"- Player turn: {current_player} -")

        # Score
        if current_player == "1":
            print(f"Your score: {p1_score} points, rival score: {p2_score} points")
        else:
            print(f"Your score: {p2_score} points, rival score: {p1_score} points")

        # Decision
        decision = decision_selected()

        # Rolling
        if decision == "r":
            rolling = roll_two_dices()
            print(f"Result of roll: {rolling[0]} & {rolling[1]} >> Total: {rolling[2]} points")

            # Update
            if current_player == "1":
                p1_score += rolling[2]
                print(f"Your score now: {p1_score} points")
            else:
                p2_score += rolling[2]
                print(f"Your score now: {p2_score} points")

        # Passing
        # if decision == "p":
        #     passing = manage_turns()

    # End
    # if game.manage_turns == '0':
    #     print("* End game *")
    #     exit()

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



