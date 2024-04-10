from cryptography.fernet import Fernet
import base64
import json


def decrypt_board(encrypted_board: str) -> list:
    """
    Decrypts the solved board for backend use
    :param encrypted_board: The encypted board
    :return: The decrypted board in type list
    """

    with open('key.key', 'rb') as file:
        key = file.read()
    fernet = Fernet(key)
    data = base64.b64decode(encrypted_board)
    decrypted_board = fernet.decrypt(data)

    decrypted_board = decrypted_board.decode()
    decrypted_board = json.loads(decrypted_board)

    return decrypted_board
