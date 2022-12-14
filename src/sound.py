from importlib.resources import path
import pygame

# hold info for a sound

class Sound:

    def __init__(self, path) -> None:
        self.path = path
        self.sound = pygame.mixer.Sound(path)

    def play(self):
        pygame.mixer.Sound.play(self.sound)