import utils


def manage_turns():
    print()
    print("new turn:")
    current_player = input("enter current player ('1'/'2'/'0' for end): ")
    return current_player


def decision_selected():
    decision = input("select your decision ('r' for roll/'p' for pass): ")
    return decision





    # extra_points = roll_two_dices()

    # for player, score in player_scores.items():
    #     print(f"{player}: {score}")
