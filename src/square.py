
# holds info of a square

class Square:

    # dictionary for col labels
    ALPHACOLS = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}

    def __init__(self, row, col, piece=None):
        self.row = row
        self.col = col
        self.piece = piece
        self.alphacol = self.ALPHACOLS[col]

    # if in same location, two squares are equal
    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    def square_string(self):
        s = ''
        if self.piece is not None:
            s += f'{self.piece.letter}'
        else:
            s += ' '
        return s

    # check for piece in square
    def has_piece(self):
        return self.piece != None

    # check if square is empty
    def isempty(self):
        return not self.has_piece()

    # check if square has a team piece
    def has_team_piece(self, color):
        return self.has_piece() and self.piece.color == color

    # check if square has an enemy piece
    def has_enemy_piece(self, color):
        return self.has_piece() and self.piece.color != color

    # combine isempty and enemy
    def isempty_or_enemy(self, color):
        return self.isempty() or self.has_enemy_piece(color)

    # check if square is on the board
    @staticmethod
    def in_range(*args):
        for arg in args:
            if arg < 0 or arg > 7:
                return False

        return True

    # get letter from col of square
    @staticmethod
    def get_alphacol(col):
        ALPHACOLS = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}
        return ALPHACOLS[col] 