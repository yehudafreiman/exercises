def scores():
    player_scores = {
        'player 1': 0,
        'player 2': 0
    }
    for player, score in player_scores.items():
        print(f"{player}: {score}")

def roll_two_dices():
    import random
    dice_1 = random.randint(1,6)
    dice_2 = random.randint(1, 6)
    total = dice_1 + dice_2
    return f'{dice_1}, {dice_2}, total: {total}'

def play_game():
    pass

def is_target(score:int):
    pass

def is_exact_hundred(score:int):
    pass

def closer_to_target():
    pass

def tie_breaker(roller):
    pass

def turn_decision(player):
    is_running = True
    while is_running:
        decision = input("choose 'roll' or 'pass': ")
        if decision == 'roll':
            roll_two_dices()
        else:
            player_1_turn = False


def display():
    pass



