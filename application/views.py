import pygame

from constants import *


class PGView:
    def __init__(self, model, size):
        self.model = model
        self.SIZE = size
        self.screen = pygame.display.set_mode(self.SIZE)
    
    def process_draw(self):
        self.screen.fill(BLACK)
        self.model.process_draw(self.screen)
        pygame.display.flip()
