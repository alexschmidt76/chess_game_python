# stores info of an attempted move

class Move:

    def __init__(self, initial, final) -> None:
        # initial and final are squares
        self.initial = initial
        self.final = final
    
    # bug testing purposes
    def __str__(self):
        s = ''
        s += f'({self.initial.row}, {self.initial.col})'
        s += f' -> ({self.final.row}, {self.final.col})'
        return s

    # if self.initial and self.final are equal in two Moves, the two Moves are equal
    def __eq__(self, other) -> bool:
        return self.initial == other.initial and self.final == other.final