import pygame

from const import *

class Menu():

    def __init__(self) -> None:
        self.button_width = 3.0 * SQSIZE
        self.button_hight = 0.5 * SQSIZE

        # button text positions
        self.hvh_button_text_pos = (2.5 * SQSIZE + (1.5 * SQSIZE - 128), 4.25 * SQSIZE + (0.25 * SQSIZE - 15))
        self.hvr_button_text_pos = (2.5 * SQSIZE + (1.5 * SQSIZE - 128), 5.25 * SQSIZE + (0.25 * SQSIZE - 15))

        # bottom right positions for buttons
        self.hvh_bottom_right = (2.5 * SQSIZE + self.button_width, 4.25 * SQSIZE + self.button_hight)
        self.hvr_bottom_right = (2.5 * SQSIZE + self.button_width, 5.25 * SQSIZE + self.button_hight)

    def show_title_screen(self, surface, win_screen=False, winner=None):

        # background
        color = (43, 82, 255)
        s = pygame.Surface((5 * SQSIZE, 5 * SQSIZE))  # size of screen
        s.set_alpha(200)                              # alpha level
        s.fill(color)                                 # this fills the entire surface
        surface.blit(s, (1.5 * SQSIZE, 1.5 * SQSIZE)) # top-left coordinates

        # title
        if win_screen:
            # text on button:                 font        size                         text                  color            palcement
            surface.blit(pygame.font.SysFont('monospace', SQSIZE, bold=True).render(winner.capitalize(), 1, (201, 176, 12)), (3 * SQSIZE - 50, 2 * SQSIZE))
            surface.blit(pygame.font.SysFont('monospace', SQSIZE, bold=True).render('Wins', 1, (201, 176, 12)), (3 * SQSIZE - 25, 3 * SQSIZE))
        else:
            # text on button:                 font        size                   text            color            palcement
            surface.blit(pygame.font.SysFont('monospace', SQSIZE, bold=True).render('CHESS', 1, (201, 176, 12)), (2.5 * SQSIZE, 2.5 * SQSIZE))

        # human v human button
        color = (173, 173, 173)
        rect = (2.5 * SQSIZE, 4.25 * SQSIZE, self.button_width, self.button_hight)
        pygame.draw.rect(surface, color, rect)
        # text on button:                 font        size                   text                 color
        surface.blit(pygame.font.SysFont('monospace', 30, bold=True).render('HUMAN vs HUMAN', 1, (56, 56, 56)), self.hvh_button_text_pos)

        # human v robot button
        color = (173, 173, 173)
        rect = (2.5 * SQSIZE, 5.25 * SQSIZE, self.button_width, self.button_hight)
        pygame.draw.rect(surface, color, rect)
        # text on button:                 font        size                   text                 color
        surface.blit(pygame.font.SysFont('monospace', 30, bold=True).render('HUMAN vs ROBOT', 1, (56, 56, 56)), self.hvr_button_text_pos)
    
    # check which button is clicked, returns tuple of bools:
    # computer_playing and game_occurring
    def versus_bot(self, pos):
        print(pos)
        if pos[0] > (2.5 * SQSIZE) and pos[0] < (2.5 * SQSIZE + self.button_width):
            print('x-click correct')
            if pos[1] > (4.25 * SQSIZE) and pos[1] < (4.25 * SQSIZE + self.button_hight):
                print('person')
                return False, True

            elif pos[1] > (5.25 * SQSIZE) and pos[1] < (5.25 * SQSIZE + self.button_hight):
                print('bot')
                return True, True

            else: return False, False

        else: return False, False
