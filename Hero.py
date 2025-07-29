import pygame
from Core import screen
class Hero( pygame.sprite.Sprite):
    def __init__(self, dx, dy, speed):
        super().__init__()
        self.image = pygame.image.load('image/hero_img/Layer 1_hero_1.png')
        self.image = pygame.transform.scale(self.image, (70, 70)).set_colorkey( (255,255,255))

        x,y,width,height = self.image.get_rect()

        self.rect = self.image.get_rect()
        self.rect.x = dx
        self.rect.y = dy
        self.speed = speed
        self.health = 100

        screen.blit(self.image, (self.rect.x, self.rect.y))

    def DISCRIPTION(self):
        pass

