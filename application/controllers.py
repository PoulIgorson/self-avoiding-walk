import pygame

from .models import PGModel
from .views import PGView


class PGController:
    settings = ['SIZE', 'FPS', 'model']
    def __init__(self, **settings):
        for key in settings:
            if key in PGController.settings:
                setattr(self, key, settings[key])
        if not hasattr(self, 'model'):
            self.model = PGModel()
        if self.SIZE == 'dynamic':
            self.SIZE = [
                self.model.SIZE * self.model.ROW,
                self.model.SIZE * (self.model.COL + 2) + 1
            ]
        self.view = PGView(self.model, self.SIZE)
        self.clock = pygame.time.Clock()
        self.run = False

    def start(self):
        self.run = True
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

                self.view.button.process_event(event)

            self.model.process_logic()

            self.view.process_draw()

            self.clock.tick(self.FPS)

        pygame.quit()
