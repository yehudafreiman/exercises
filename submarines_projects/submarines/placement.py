def count_submarines(init_board):
    count = 0
    submarine = 1
    for row in init_board:
        count += row.count(submarine)
    return count

def state_game():
    state = {
        # "submarines": count_submarines((10,10))
        "shots": []
    }
    return state
