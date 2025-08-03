import pygame

class Parents(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, speed):
        super().__init__()
        self.image = pygame.image.load('image/npc_img/npc_1.png')
        self.hps = 100
        self.speed = speed
        self.screen = screen