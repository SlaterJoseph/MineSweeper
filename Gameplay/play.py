from .generation import generate_board
from .actions import mark_flag, unmark_flag, clicked_cell, check_victory


def game(row_size: int, col_size: int, mine_count: int):
    """
    Actually plays the game locally to test everything (Will be altered for the online gameplay)
    :param row_size: The amount of rows on the board
    :param col_size: The amount of columns on the board
    :param mine_count: THe amount of mines on the board
    :return: None
    """
    gameplay_board = [['+' for _ in range(row_size)] for _ in range(col_size)]
    initial_move = make_move()

    # Incase for some reason someone spams flag before picking an initial cell
    move_list = list()
    while initial_move[2] == 'F' or initial_move == 'U':
        move_list.append((initial_move[0], initial_move[1]))
        initial_move = make_move()

    generated_board = generate_board(row_size, col_size, initial_move[0], initial_move[1], mine_count)

    # Adding all the flags that were initially there
    while len(move_list) > 0:
        move = move_list.pop(0)
        if move[2] == 'F':
            mark_flag(move[0], move[1], gameplay_board)
        elif move[2] == 'U':
            unmark_flag(move[0], move[1], gameplay_board)

    result = clicked_cell(initial_move[0], initial_move[1], generated_board)
    if type(result) == int:
        modify_board_single(gameplay_board, result, initial_move[0], initial_move[1])
    else:
        modify_board_list(gameplay_board, generated_board, result)

    print_board(gameplay_board)
    last_move = 0
    # A while loop that lasts while a mine isn't clicked and the game isn't won
    while last_move != -1 and not check_victory(gameplay_board, generated_board):
        new_move = make_move()

        # Checks if the move is a click, flag, unflag or show the board
        if new_move[2] == 'C':
            result = clicked_cell(new_move[0], new_move[1], generated_board)

            # To differentiate when a single cell or empty cell is clicked
            if type(result) == int:
                modify_board_single(gameplay_board, result, new_move[0], new_move[1])
            else:
                modify_board_list(gameplay_board, generated_board, result)
            last_move = result
        elif new_move[2] == 'F':
            mark_flag(new_move[0], new_move[1], gameplay_board)
        elif new_move[2] == 'U':
            unmark_flag(new_move[0], new_move[1], gameplay_board)
        else:
            print_board(gameplay_board)

    # Check if the player won or lost
    if check_victory(gameplay_board, generated_board):
        print('Congrats! You won!')
    else:
        print('You hit a mine. You Lose')

    print('Gameplay Board')
    print_board(gameplay_board)
    print('Generated Board')
    print_board(generated_board)


def make_move() -> (int, int, str):
    """
    A function for making a move in the game
    :return: (row, col, action)
    """
    row_loc = int(input('Which row do you want to select: '))
    col_loc = int(input('Which column do you want to select: '))
    action = str(input('Is this field being flagged, unflagged, clicked or do you want the board shown: (F for flag, '
                       'C for clicked, U for unmark flag, S for board show): ')).upper()

    return row_loc - 1, col_loc - 1, action


def modify_board_list(game_board: list, state_board: list, result: list) -> None:
    """
    Modification for empty cells. Make all nearby cells which should be made visible, visible
    :param game_board: The board the user sees
    :param state_board: The board the backend references
    :param result: The result of a given move (A list of none mine squares)
    :return: None
    """
    for entry in result:
        game_board[entry[0]][entry[1]] = state_board[entry[0]][entry[1]]


def modify_board_single(game_board: list, result: int, row: int, col: int) -> bool:
    """
    Modification for a single cell. Make the given cell appear as its defined value
    :param game_board: The board the user sees
    :param result: The result from the clicked cell
    :param row: The row of the clicked cell
    :param col: The col of the clicked cell
    :return: None
    """
    game_board[row][col] = result
    return result == -1


def print_board(board: list) -> None:
    """
    Prints a given board
    :param board: The board to be printed out
    :return: None
    """
    for row in board:
        print(row)


def move(curr_board: list, solved_board: list, row: int, col: int, move_type: str) -> bool:
    """
    A method which applies the most recent move to the users game board
    :param curr_board: The board the player is viewing
    :param solved_board: The solved board
    :param row: The row the move was made in
    :param col: The col the move was made in
    :param move_type: The type of move (click, flag, unflag)
    :return: Return the updated curr board
    """
    game_lost = False

    if move_type == 'C':
        action = clicked_cell(row, col, solved_board)

        # To differentiate between 0s or numbered cells
        if type(action) == list:
            modify_board_list(curr_board, solved_board, action)
        else:
            game_lost = modify_board_single(curr_board, action, row, col)

    elif move_type == 'F':
        mark_flag(row, col, curr_board)
    elif move_type == 'U':
        unmark_flag(row, col, curr_board)

    return game_lost
