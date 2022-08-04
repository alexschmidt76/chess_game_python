# stroes piece that is being dragged by mouse

import pygame

from const import *

class Dragger:

    def __init__(self):
        self.piece = None
        self.dragging = False
        self.mouseX = 0
        self.mouseY = 0
        self.initial_row = 0
        self.initial_col = 0

    # blit method

    def update_blit(self, surface):
        # texture
        self.piece.set_texture(size=128)
        texture = self.piece.texture
        # img
        img = pygame.image.load(texture)
        # rect
        img_center = (self.mouseX, self.mouseY)
        self.piece.texture_rect = img.get_rect(center=img_center)
        # blit
        surface.blit(img, self.piece.texture_rect)

    # other methods

    # track mouse position
    def update_mouse(self, pos):
        self.mouseX, self.mouseY = pos # (xcor, ycor)

    # save initial position
    def save_initial(self, pos):
        self.initial_row = pos[1] // SQSIZE
        self.initial_col = pos[0] // SQSIZE

    # set dragging to true and store piece in dragger
    def drag_piece(self, piece):
        self.piece = piece
        self.dragging = True

    # set dragging to false and remove piece from dragger
    def undrag_piece(self):
        self.piece = None
        self.dragging = False