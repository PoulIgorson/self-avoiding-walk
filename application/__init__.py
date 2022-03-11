import pygame

from .controllers import PGController


class PGApplication:
    SIZE = WIDTH, HEIGHT = 1080, 720
    FPS = 30
    def __init__(self):
        pygame.init()
        settings = {
            'SIZE': self.SIZE,
            'FPS': self.FPS,
        }
        self.controller = PGController(**settings)
    
    def start(self):
        self.controller.start()
