from Game.generation import generate_board
empty_board = [[0 for _ in range(5)] for _ in range(5)]
board = generate_board(empty_board, 2, 2, 5)

for row in board:
    print(row)

