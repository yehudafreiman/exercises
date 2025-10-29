import random

def create_board(row, col):
    init_board = []
    for i in range(row):
        row = []
        for j in range(col):
            row.append(random.randint(0,1))
        init_board.append(row)
    return init_board
print(create_board(10,10))

def count_submarines(init_board):
    count = 0
    submarine = 1
    for row in init_board:
        count += row.count(submarine)
    return count
print(count_submarines(create_board(10,10)))

def state_game():
    state = {
        "shots": []
    }
    return state
# print(state_game())

def player_shooting():
    index_1 = int(input("Enter a number for a row index (1-10): "))
    index_2 = int(input("Enter a number for column index (1-10): "))
    shoot_point = index_1, index_2
    state_game()["shots"].append(index_1)
    state_game()["shots"].append(index_2)
    return shoot_point
# print(player_shooting())

def valid_shot(shoot_point):
    return

def shoot_result(init_board, shoot_point):
    shoot_point = init_board[shoot_point[0]][shoot_point[1]]
    if shoot_point == 1:
        return "hit"
    else:
        return "miss"
print(shoot_result(create_board(10,10), player_shooting()))



