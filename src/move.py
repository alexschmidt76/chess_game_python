
class Move:

    def __init__(self, initial, final) -> None:
        # initial and final are squares
        self.initial = initial
        self.final = final
    
    def __str__(self):
        s = ''
        s += f'({self.initial.row}, {self.initial.row})'
        s += f' -> ({self.final.col}, {self.final.col})'
        return s

    def __eq__(self, other) -> bool:
        return self.initial == other.initial and self.final == other.final