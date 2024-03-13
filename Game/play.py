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
    flag_list = list()
    while initial_move[2] == 'F' or initial_move == 'U':
        flag_list.append((initial_move[0], initial_move[1]))
        initial_move = make_move()

    generated_board = generate_board(gameplay_board, initial_move[0], initial_move[1], mine_count)

    # Adding all the flags that were initially there
    while len(flag_list) > 0:
        flag = flag_list.pop(0)
        mark_flag(flag[0], flag[1], gameplay_board)

    last_move = 0
    # A while loop that lasts while a mine isn't clicked and the game isn't won
    while last_move != -1 and not check_victory(gameplay_board, generated_board):
        pass


def make_move() -> (int, int, str):
    """
    A function for making a move in the game
    :return:
    """
    row_loc = int(input('Which row do you want to select: '))
    col_loc = int(input('Which column do you want to select: '))
    action = str(input('Is this field being flagged, unflagged, or clicked: (F for flag, C for , U for unmark flag): '))

    return row_loc, col_loc, action
