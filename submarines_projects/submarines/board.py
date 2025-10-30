import random

def create_board(row, col):
    init_board = []
    for i in range(row):
        row = []
        for j in range(col):
            row.append(random.randint(0,1))
        init_board.append(row)
    return init_board

def update_board(board, shoot_point):
    for row in range(len(board)):
        for col in row:
            print(1)
    return
update_board(create_board(10,10), player_shooting())










