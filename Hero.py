import pygame
from pygame.math import Vector2
class Hero( pygame.sprite.Sprite):
    def __init__(self,screen, x, y, speed):
        ''' инициализация персонажа'''
        super().__init__()
        self.image = pygame.image.load('image/hero_img/Move/Layer 1_Солянка_1.png')
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.image.set_colorkey( (255,255,255))
        self.orig_image = self.image

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.HEALTH = 100
        self.invnt = []
        self.implants = []
        self.speed = speed

        self.screen = screen
    def update(self):
        '''ёго отрисовка'''
        self.screen.blit(self.image,(self.rect.x,self.rect.y) )

    def rotate(self):
        '''поворот перса за мышкой'''
        direction = pygame.mouse.get_pos() - Vector2(self.rect.centerx, self.rect.centery)
        x = self.rect.centerx + direction.x * self.speed
        y = self.rect.centery + direction.y * self.speed
        angle = Vector2(x, y).as_polar()[1]
        self.image = pygame.transform.rotate(self.orig_image, -angle - 90)
        self.image.set_colorkey( (255,255,255))
        self.rect = self.image.get_rect(center=self.rect.center)
    def move(self):
        sprites = [f'image/hero_img/Move/Layer 1_Солянка_{i}.png' for i in range(1,5)]
        for sprite in sprites:
            self.image = pygame.image.load(sprite)
            self.image = pygame.transform.scale(self.image, (150, 150))
            self.image.set_colorkey( (255,255,255))
            self.rect = self.image.get_rect()
            self.rect.x = self.rect.x
            self.rect.y = self.rect.y
            self.screen.blit(self.image,(self.rect.x,self.rect.y) )

class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, speed):
        super().__init__()
        self.image = pygame.image.load('image/action_img/Bullet.png')
        self.image = pygame.transform.scale(self.image, (10, 10))
        self.image.set_colorkey( (255,255,255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
