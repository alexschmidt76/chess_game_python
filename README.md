
CHESS GAME IN PYTHON
by Alex Schmidt

This program is a chess game that can be played between two people locally.

I am currently working on the AI aspect, which will use minimax and alpha-beta pruning.
Currently, the AI is completely random.

Run main.py to play game.

KNOWN BUGS:
    white loss not being detected in:
        white: pawn f3
        black: pawn e6
        white: pawn g4
        black: pawn f5
        white: pawn h3
        black: queen h4
    incorrect white win in:
        white: pawn e4
        black: pawn e6
        white: bishop c4
        black: pawn c6
        white: queen h5
        black: bishop a3

TODO:
    build AI:
        build move-evaluator function that rates a move depending on its value
        build searcher to find best move
        learn alpha beta pruning
    fix bugs:
        seems to have something to do with the in_check() method in the board class
