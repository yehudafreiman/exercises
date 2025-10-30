def player_shooting():
    index_1 = int(input("Enter a number for a row index (1-10): "))
    index_2 = int(input("Enter a number for column index (1-10): "))
    shoot_point = index_1, index_2
    return shoot_point

def valid_shot(state, shoot_point):
    state["shots"].append(shoot_point)
    return state

def shoot_result(init_board, shoot_point):
    shoot_point = init_board[shoot_point[0]][shoot_point[1]]
    if shoot_point == 1:
        return "hit"
    else:
        return "miss"
