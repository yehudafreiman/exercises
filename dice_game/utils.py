import game

def roll_two_dices():
    import random
    dice_1 = random.randint(1,6)
    dice_2 = random.randint(1, 6)
    total_points = dice_1 + dice_2
    result = [dice_1, dice_2, total_points]
    return result

