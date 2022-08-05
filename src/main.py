import pygame
import sys

from const import *
from game import Game
from square import Square
from move import Move
from menu import Menu
from ai import AI

# controls the flow of the game

class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
        pygame.display.set_caption('Chess')
        self.game = Game()

    def mainloop(self):

        game_occurring = False
        is_win = False
        winner = None
        computer_playing = False
        screen = self.screen
        game = self.game
        board = game.board
        dragger = game.dragger
        title = Menu()

        while True:
            # menu
            while not game_occurring:
                if not is_win:
                    game.show_bg(screen)
                    title.show_title_screen(screen)
                else:
                    game.show_bg(screen)
                    game.show_last_move(screen)
                    game.show_pieces(screen)
                    title.show_title_screen(screen, win_screen=True, winner=winner)

                for event in pygame.event.get():

                    # click
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        computer_playing, game_occurring = title.versus_bot(event.pos)
                        if game_occurring:
                            game.reset()
                            game = self.game
                            board = self.game.board
                            dragger = self.game.dragger

                    # quit application
                    elif event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                       
                pygame.display.update()

            # show methods
            game.show_bg(screen)
            game.show_last_move(screen)
            game.show_moves(screen)
            game.show_pieces(screen)
            game.show_hover(screen)

            if dragger.dragging:
                dragger.update_blit(screen)

            # check if next player is human
            if not computer_playing or game.next_player == 'white':
                for event in pygame.event.get():

                    # click
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        dragger.update_mouse(event.pos)

                        clicked_row = dragger.mouseY // SQSIZE
                        clicked_col = dragger.mouseX // SQSIZE

                        # if clicked square has a piece ?
                        if board.squares[clicked_row][clicked_col].has_piece():
                            piece = board.squares[clicked_row][clicked_col].piece
                            # valid piece (color) ?
                            if piece.color == game.next_player:
                                board.calc_moves(piece, clicked_row, clicked_col, bool=True)
                                dragger.save_initial(event.pos)
                                dragger.drag_piece(piece)
                                # show methods 
                                game.show_bg(screen)
                                game.show_last_move(screen)
                                game.show_moves(screen)
                                game.show_pieces(screen)

                    # mouse motion
                    elif event.type == pygame.MOUSEMOTION:
                        motion_row = event.pos[1] // SQSIZE
                        motion_col = event.pos[0] // SQSIZE

                        game.set_hover(motion_row, motion_col)

                        if dragger.dragging:
                            dragger.update_mouse(event.pos)
                            # show methods
                            game.show_bg(screen)
                            game.show_last_move(screen)
                            game.show_moves(screen)
                            game.show_pieces(screen)
                            game.show_hover(screen)
                            dragger.update_blit(screen)

                    # click release
                    elif event.type == pygame.MOUSEBUTTONUP:

                        if dragger.dragging:
                            dragger.update_mouse(event.pos)

                            released_row = dragger.mouseY // SQSIZE
                            released_col = dragger.mouseX // SQSIZE

                            # create possible move
                            initial = Square(dragger.initial_row, dragger.initial_col)
                            final = Square(released_row, released_col)
                            move = Move(initial, final)

                            # valid move ?
                            if board.valid_move(dragger.piece, move):
                                # normal capture
                                captured = board.squares[released_row][released_col].has_piece()
                                board.move(dragger.piece, move)

                                board.set_true_en_passant(dragger.piece)                            

                                # sounds
                                game.play_sound(captured)

                                # show methods
                                game.show_bg(screen)
                                game.show_last_move(screen)
                                game.show_pieces(screen)

                                # next turn
                                if not game.next_turn(board):
                                    game_occurring = False
                                    is_win = True
                                    winner = 'white' if game.next_player == 'black' else 'black'
                                                                    
                                else:
                                    print(f'{dragger.piece.color}: {dragger.piece.name} {Square(released_row, released_col).get_alphacol(released_col)}{ROWS - released_row}')

                            dragger.undrag_piece()

                    # key press
                    elif event.type == pygame.KEYDOWN:

                        # changing themes
                        if event.key == pygame.K_t:
                            game.change_theme()

                        # reset game
                        if event.key == pygame.K_r:
                            game.reset()
                            game = self.game
                            board = self.game.board
                            dragger = self.game.dragger

                    # quit application
                    elif event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

            # check if next player is ai
            elif computer_playing and game.next_player == 'black':
                ai = AI(board)

                # make ai move here
                move = ai.chose_random_move()
                piece = board.squares[move.initial.row][move.initial.col].piece

                captured = board.squares[move.final.row][move.final.col].has_piece()
                board.move(piece, move)

                board.set_true_en_passant(piece)                            

                # sounds
                game.play_sound(captured)
                print(f'captured: {captured}')

                # show methods
                game.show_bg(screen)
                game.show_last_move(screen)
                game.show_pieces(screen)

                # next turn
                if not game.next_turn(board):
                    game_occurring = False
                    is_win = True
                    winner = 'white' if game.next_player == 'black' else 'black'
                                                    
                else:
                    print(f'black: {piece.name} {Square(move.final.row, move.final.col).get_alphacol(move.final.col)}{ROWS - move.final.row}')

            pygame.display.update()

main = Main()
main.mainloop() 