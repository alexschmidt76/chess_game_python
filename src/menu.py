import pygame

from const import *

class Menu():

    def __init__(self) -> None:
        self.button_width = 3.0 * SQSIZE
        self.button_hight = 0.5 * SQSIZE

        # title screen buttons
        self.hvh_button_pos = (2.5 * SQSIZE + (1.5 * SQSIZE - 128), 4.25 * SQSIZE + (0.25 * SQSIZE - 15))
        self.hvh_bottom_right = (self.hvh_button_pos[0] + self.button_width, self.hvh_button_pos[1] + self.button_hight)
        self.hvr_button_pos = (2.5 * SQSIZE + (1.5 * SQSIZE - 128), 5.25 * SQSIZE + (0.25 * SQSIZE - 15))
        self.hvr_bottom_right = (self.hvr_button_pos[0] + self.button_width, self.hvr_button_pos[1] + self.button_hight)

        # win screen buttons

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
        surface.blit(pygame.font.SysFont('monospace', 30, bold=True).render('HUMAN vs HUMAN', 1, (56, 56, 56)), self.hvh_button_pos)

        # human v robot button
        color = (173, 173, 173)
        rect = (2.5 * SQSIZE, 5.25 * SQSIZE, self.button_width, self.button_hight)
        pygame.draw.rect(surface, color, rect)
        # text on button:                 font        size                   text                 color
        surface.blit(pygame.font.SysFont('monospace', 30, bold=True).render('HUMAN vs ROBOT', 1, (56, 56, 56)), self.hvr_button_pos)
    
    def versus_bot(self, pos):
        if (pos > self.hvh_button_pos) and (pos < self.hvh_bottom_right):
            return False, True
        elif (pos > self.hvr_button_pos) and (pos < self.hvr_bottom_right):
            return True, True
        else: return False, False
