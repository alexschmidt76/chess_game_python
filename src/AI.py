from random import randint
from copy import deepcopy

from const import *

class AI:

    def __init__(self, board) -> None:
        self.board = deepcopy(board)
        board.print_board()
        self.color = 'black' # as of now, ai is always black

    # return list of valid moves for ai
    def valid_moves(self):
        board = self.board
        valid_moves = []

        # find all valid moves
        for row in range(ROWS):
            for col in range(COLS):
                if board.squares[row][col].has_team_piece(self.color):
                    piece = deepcopy(board.squares[row][col].piece)
                    board.calc_moves(piece, row, col)
                    if len(piece.moves) > 0:
                        for move in piece.moves:
                            valid_moves.append(move)

        return valid_moves

    def chose_random_move(self):
        moves = self.valid_moves()
        return moves[randint(0, len(moves) - 1)]

 