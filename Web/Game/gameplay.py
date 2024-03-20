from flask import Blueprint, request, jsonify
from ...Game.generation import generate_board

actions_bp = Blueprint('gameplay', __name__)


# Json format {row: int, col: int, type: int}
@actions_bp.route('/gameplay', methods=['GET'])
def get_move():
    """
    Handles a new move from the client side
    :return: return new board, status code
    """
    new_move = request.json()


@actions_bp.route('/generate', methods=['POST'])
def generate_board():
    data = request.json

    row_count = data.get('row_count')
    col_count = data.get('col_count')
    row = data.get('row')
    col = data.get('col')
    mine_count = data.get('mine_count')

    board = generate_board(row_count, col_count, row, col, mine_count)


