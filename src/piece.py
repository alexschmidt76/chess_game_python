from math import inf
import os

# used to store info about individual pieces

class Piece:

    def __init__(self, letter, name, color, value, texture=None, texture_rect=None):
        self.name = name
        self.letter = letter
        self.color = color
        value_sign = 1 if color == 'black' else -1
        self.value = value * value_sign
        self.moves = []
        self.moved = False
        self.texture = texture
        self.set_texture()
        self.texture_rect = texture_rect

    # set piece texture
    def set_texture(self, size=80):
        self.texture = os.path.join(
            f'assets/images/imgs-{size}px/{self.color}_{self.name}.png')

    # add move to list of moves
    def add_move(self, move):
        self.moves.append(move)

    # clear list of moves
    def clear_moves(self):
        self.moves = []

# create instances of Piece for each piece type

class Pawn(Piece):

    def __init__(self, color):
        self.dir = -1 if color == 'white' else 1
        self.en_passant = False
        super().__init__('p', 'pawn', color, 1.0)

class Knight(Piece):

    def __init__(self, color):
        super().__init__('n', 'knight', color, 3.0)

class Bishop(Piece):

    def __init__(self, color):
        super().__init__('b', 'bishop', color, 3.001)

class Rook(Piece):

    def __init__(self, color):
        super().__init__('r', 'rook', color, 5.0)

class Queen(Piece):

    def __init__(self, color):
        super().__init__('q', 'queen', color, 9.0)

class King(Piece):

    def __init__(self, color):
        self.left_rook = None
        self.right_rook = None
        super().__init__('k', 'king', color, inf)