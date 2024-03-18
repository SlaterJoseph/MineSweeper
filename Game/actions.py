def mark_flag(row: int, col: int, board: list) -> None:
    """
    Marks a given cell as a flag
    :param row: The row of the flagged cell
    :param col: The column of the flagged cell
    :param board: The board of cells
    :return: None
    """
    board[row][col] = -2
    return None


def unmark_flag(row: int, col: int, game_board: list, state_board: list) -> None:
    """
    Sets a flagged cell back, so it is unflagged
    :param row: The row of the cell
    :param col: The col of the cell
    :param game_board: The board the user is playing on
    :param state_board: The saved original board
    :return: None
    """
    game_board[row][col] = state_board[row][col]
    return None


def clicked_cell(row: int, col: int, board: list) -> int or list:
    """
    Checks the given cell, showing the proper value
    :param row: The row of the selected cell
    :param col: The column of the selected cell
    :param board: The board
    :return: Either the value of the cell (-1 for mine or the number of mines
    surrounding the cell) or a list of empty cells
    """
    result = board[row][col]

    # We need to find all cells with a value of 0, and return all of those cells as well as those touching
    if result == 0:
        result = [(row, col)]
        queue = [(row, col)]
        checked = set()

        # Check all surrounding cells if they are blank or have a numeric value
        while len(queue) > 0:
            r, c = queue.pop(0)

            # No need to check a cell already checked
            if (r, c) in checked:
                continue

            # Add the cell since it is now being checked
            checked.add((r, c))

            # Add all cells which need to revealed
            for i in range(r - 1, r + 2):
                if i < 0 or i > len(board) - 1:
                    continue

                for j in range(c - 1, c + 2):
                    if j < 0 or j > len(board[i]) - 1 or (i, j) in checked:
                        continue

                    cell = board[i][j]

                    # Add empty cells to the queue
                    if cell == 0 and (i, j) not in checked:
                        queue.append((i, j))

                    # Ignore flags -- If one is here it's the players fault so they must unflag it
                    if cell == -2:
                        continue

                    result.append((i, j))
    else:
        result = board[row][col]

    return result


def check_victory(back_board: list, front_board: list):
    """
    Check if a player has one
    :param back_board: The board saved to remember the state
    :param front_board: The board altered by the player
    :return: True or false based on if the boards match
    """
    for i in range(len(back_board)):
        for j in range(len(back_board[0])):
            if back_board[i][j] != front_board[i][j]:
                if back_board[i][j] not in [-1, -2] or front_board[i][j] not in [-1, -2]:
                    return False
    return True
