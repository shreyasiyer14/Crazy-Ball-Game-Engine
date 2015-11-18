import pygame

class Brick:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 32
        self.height = 32

    def render(self, window):
        pygame.draw.rect(window, (55,155,0),(self.x, self.y, self.width, self.height))