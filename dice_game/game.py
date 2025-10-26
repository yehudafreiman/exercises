import utils


def manage_turns():
    run = True
    current_player = input("enter current player ('1'/'2'/'0' for end): ")
    if current_player == 0:
        run = False
    return current_player


def manage_scores(current_player):
    scores_data = [0, 0]
    if current_player == "1":
        return scores_data[0]
    else:
        return scores_data[1]


def decision_selected():
    decision = input("select your decision ('r' for roll/'p' for pass): ")
    return decision





    # extra_points = roll_two_dices()

    # for player, score in player_scores.items():
    #     print(f"{player}: {score}")
