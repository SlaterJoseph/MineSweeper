from Gameplay.generation import generate_board
from Gameplay.play import move


def generation(row_count: int, col_count: int, mine_count: int, row: int, col: int) -> (list, list):
    """
    Calls the proper functions to generate a game board, solved board, and input the first move
    :param row_count: The amount of rows
    :param col_count: The amount of columns
    :param mine_count: The amount of mines in the board
    :param row: The row of the initial move
    :param col: The column of the initial move
    :return: A list of the game board, solve board
    """
    solved_board = generate_board(row_count, col_count, row, col, mine_count)
    game_board = [[-10 for _ in range(row_count)] for _ in range(col_count)]
    move(game_board, solved_board, row, col, 'C')

    return game_board, solved_board


def make_move(row: int, col: int, action: str, game_board: list, solved_board: list) -> (list, bool):
    """
    Takes the action of the user to the game board
    :param row: The row of the clicked cell
    :param col: The col of the clicked cell
    :param action: The action taken by the user
    :param game_board: The board the user is solving
    :param solved_board: The completed board
    :return:
    """
    game_lost = move(game_board, solved_board, row, col, action)
    return game_board, game_lost
