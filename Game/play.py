from generation import generate_board
from actions import mark_flag, unmark_flag, clicked_cell, check_victory


def game():
    """
    Actually plays the game locally to test everything (Will be altered for the online gameplay)
    :return: None
    """
    row_size = int(input('How many rows should our minefield have: '))
    col_size = int(input('How many columns should our minefield have: '))
    mine_count = int(input('How many mines do you want in the field: '))

    gameplay_board = [['+' for _ in range(row_size)] for _ in range(col_size)]
    initial_move = make_move()

    # Incase for some reason someone spams flag before picking an initial cell
    move_list = list()
    while initial_move[2] == 'F' or initial_move == 'U':
        move_list.append((initial_move[0], initial_move[1]))
        initial_move = make_move()

    generated_board = generate_board(gameplay_board, initial_move[0], initial_move[1], mine_count)
    # Adding all the flags that were initially there
    while len(move_list) > 0:
        move = move_list.pop(0)
        if move[2] == 'F':
            mark_flag(move[0], move[1], gameplay_board)
        elif move[2] == 'U':
            unmark_flag(move[0], move[1], gameplay_board, generated_board)

    result = clicked_cell(initial_move[0], initial_move[1], generated_board)
    if type(result) == list:
        pass
    else:

    last_move = 0
    # A while loop that lasts while a mine isn't clicked and the game isn't won
    while last_move != -1 and not check_victory(gameplay_board, generated_board):
        pass


def make_move() -> (int, int, str):
    """
    A function for making a move in the game
    :return: (row, col, action)
    """
    row_loc = int(input('Which row do you want to select: '))
    col_loc = int(input('Which column do you want to select: '))
    action = str(input('Is this field being flagged, unflagged, or clicked: (F for flag, C for , U for unmark flag): '))

    return row_loc - 1, col_loc - 1, action


def modify_game_board(game_board: list, state_board: list, result: list or int, row: int = 0, col: int = 0) -> None:
    """
    Adjust the game-board after a given move
    :param game_board: The playing board
    :param state_board: The backend board generated
    :param result: The results from the initial move
    :param row: The row of the clicked tile
    :param col: The column of the clicked tile
    :return: None
    """
    if type(result) == int:
        game_board[row][col] = result
    elif type(game_board) == list:
        for entry in result:
            game_board[entry[0]][entry[1]] = state_board[entry[0]][entry[1]]