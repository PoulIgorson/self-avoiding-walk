import pygame

from .objects.button import ButtonObject as Button

from constants import *


class PGView:
    def __init__(self, model, size):
        pygame.display.set_caption('Self Avoiding walk')
        self.SIZE = size
        self.model = model
        self.screen = pygame.display.set_mode(self.SIZE)
        self.font = pygame.font.SysFont('arial', 32)
        self.founding = self.font.render('Founding', True, WHITE)
        self.finish = self.font.render('Path found', True, WHITE)
        self.pos_founding = (self.SIZE[0]//2 - self.founding.get_size()[0]//2, 0)
        self.pos_finish = (self.SIZE[0]//2 - self.finish.get_size()[0]//2, 0)
        
        self.button = Button(
            self.SIZE[0]//2 - 60, self.model.SIZE * self.model.COL + self.model.path[0].size, 
            120, 30, modRED, self.model.reset, 'reset'
        )
    
    def process_draw(self):
        self.screen.fill(BLACK)
        self.button.process_draw(self.screen)
        self.model.process_draw(self.screen)
        if self.model.finish:
            self.screen.blit(self.finish, self.pos_finish)
        else:
            self.screen.blit(self.founding, self.pos_founding)
        pygame.display.flip()
