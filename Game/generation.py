import random


def generate_board(board: list, row: int, col: int, mine_count: int) -> list or int:
    """
    Generates the playing board for minesweeper
    :param board: A board of 0s to be altered to our gameboard
    :param row: The first cell's row (MUST BE SAFE)
    :param col: The first cell's column (MUST BE SAFE)
    :param mine_count: The amount of mines the user selected
    :return: The generated board
    """

    # Flag for invalid mine count on the small end
    if mine_count <= 0:
        return -1

    # Flag for invalid mine count on the large end
    if mine_count > row * col:
        return -2

    total_cells = row * col
    mines = 0

    # Placing the mines
    while mines < mine_count:
        r = random.randint(0, len(board) + 1)
        c = random.randint(0, len(board[0]) + 1)

        # Prevent our initial cell from being a mine
        if r == row and c == col:
            continue

        if board[r][c] != -1:
            board[r][c] = -1
            mines += 1

            # Iterate over all surrounding cells, incrementing by 1
            for i in range(row - 1, row + 2):
                for j in range(col - 1, col + 2):
                    if 0 <= i < len(board) and 0 <= j < len(board[i]) and board[i][j] != -1:
                        board[i][j] += 1




