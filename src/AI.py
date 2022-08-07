from random import randint
from copy import deepcopy
from board import Board

from const import *

class AI:

    def __init__(self) -> None:
        self.color = 'black'

    # get pieces that have valid moves
    def get_valid_pieces(self, board):
        # copy board
        temp_board = deepcopy(board)
        valid_piece_positions = []

        # check each piece for valid moves
        for row in range(ROWS):
            for col in range(COLS):
                if temp_board.squares[row][col].has_team_piece(self.color):
                    temp_piece = deepcopy(temp_board.squares[row][col].piece)
                    temp_board.calc_moves(temp_piece, row, col)
                    if len(temp_piece.moves) > 0:
                        valid_piece_positions.append(temp_board[row][col])

    # evaluate move
    def eval(self, board, move):
        # copy board
        temp_board = deepcopy(board)

        # for captured pieces, return piece value
        if board.squares[move.final.row][move.final.col].has_enemy_piece():
            return board.squares[move.final.row][move.final.col].piece.value
        
        else: return 0

    