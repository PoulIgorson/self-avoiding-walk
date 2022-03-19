import pygame

from libs.button import Button

from constants import modBLUE, modGREEN, BLACK, ORANGE


class ButtonObject:
    BUTTON_STYLE = {
        "hover_color": modBLUE,
        "clicked_color": modGREEN,
        "clicked_font_color": BLACK,
        "hover_font_color": ORANGE,
    }

    def __init__(self, x, y, width, height, color, function, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.function = function
        self.text = text
        self.rect = pygame.rect.Rect(x, y, width, height)
        self.BUTTON_STYLE['text'] = text
        self.button = Button((x, y, width, height), color, function, self.BUTTON_STYLE)

    def process_event(self, event):
        self.button.check_event(event)

    def process_draw(self, screen):
        self.button.update(screen)

    def update(self):
        self.button = Button((self.x, self.y, self.width, self.height), self.color, self.function, text=self.text,
                             **self.BUTTON_STYLE)

    def reset_text(self, new_text):
        self.button = Button((self.x, self.y, self.width, self.height), self.color, self.function, text=new_text,
                             **self.BUTTON_STYLE)
    
    @property
    def pos(self):
        return self.x, self.y
    
    @property
    def size(self):
        return self.width, self.height
