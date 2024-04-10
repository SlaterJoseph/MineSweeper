from flask import Blueprint, request, jsonify
from Web.Game.service import generation, make_move
from cryptography.fernet import Fernet
from ..utils import decrypt_board
import base64
import json


gameplay_bp = Blueprint('gameplay', __name__)
with open('key.key', 'rb') as file:
    key = file.read()
fernet = Fernet(key)


@gameplay_bp.route('/generate', methods=['GET'])
def generate():
    """
    Generates the board of minesweeper
    :return: The game board, encrypted solved board, and a return code
    """
    data = request.json

    row_count = int(data.get('row_count'))
    col_count = int(data.get('col_count'))
    mine_count = int(data.get('mine_count'))
    row = int(data.get('row'))
    col = int(data.get('col'))
    game_board, solved_board = generation(row_count, col_count, mine_count, row, col)

    encrypted = fernet.encrypt(str(solved_board).encode())
    encrypted = base64.b64encode(encrypted).decode()

    return jsonify({
        'game_board': game_board,
        'solved_board': encrypted
    }), 201


@gameplay_bp.route('/receive_move', methods=['POST'])
def make_move():
    """
    Receives the most recent move from minesweeper
    :return:
    """
    data = request.json

    row = int(data.get('row'))
    col = int(data.get('col'))
    action = str(data.get('action'))
    game_board = json.loads(str(data.get('game_board')))
    solved_board = decrypt_board(json.loads(str(data.get('solved_board'))))

    game_board, game_lost = make_move(row, col, action, game_board, solved_board)

    return jsonify({
        'game_board': game_board,
        'solved_board': data.get('solved_board'),
        'game_lost': game_lost
    }), 201
