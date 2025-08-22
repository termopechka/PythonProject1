import pygame

class Objects:
    def __init__(self, x, y, image, image_tmx):
        self.x = x
        self.y = y
        self.image = image
        self.image_tmx = image_tmx

class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, surface, group):
        super().__init__(group)
        self.image = surface
        self.rect = self.image.get_rect(center=pos)