import math

import pygame
from pygame.math import Vector2
from pygame.transform import rotate


class Hero(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, speed):
        ''' инициализация персонажа'''
        super().__init__()
        self.image = pygame.image.load('image/hero_img/state/Layer 1_solo_01.png')
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.image.set_colorkey( (255,255,255))
        self.orig_image = self.image

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.angle = None

        self.HEALTH = 100
        self.invnt = []
        self.implants = []
        self.speed = speed
        self.sprint = speed * 2

        self.cooldown_shoot = 400
        self.shoot = None

        self.sprites_now = 0
        self.speed_sprites = 0.15
        self.status = 'stand'
        self.walk_list = []
        for i in range(1, 4):
            img = pygame.image.load(f'image/hero_img/state/Layer 1_solo_0{i}.png')
            img = pygame.transform.scale(img, (150, 150))
            img.set_colorkey( (255,255,255))
            self.walk_list.append(img)

        self.shoot_list = []
        for i in range(1, 4):
            img = pygame.image.load(f'image/hero_img/Shoot/Layer 1_solo_0{i}.png')
            img = pygame.transform.scale(img, (150, 150))
            img.set_colorkey((255, 255, 255))
            self.shoot_list.append(img)
        self.screen = screen
    def update(self):
        self.sprites_now += self.speed_sprites
        if self.sprites_now >= len(self.walk_list):
            self.sprites_now = 0
        if self.status == 'move':
            self.image = self.walk_list[int(self.sprites_now)]
            self.orig_image = self.image
        elif self.status == 'shoot':
            self.image = self.shoot_list[int(self.sprites_now)]
            self.orig_image = self.image

        elif self.status == 'stand':
            self.image = self.walk_list[0]
            self.orig_image = self.image
    def get_rotation_angle(self):
        direction = pygame.mouse.get_pos() - Vector2(self.rect.centerx, self.rect.centery)
        return -direction.as_polar()[1] - 90
    def rotate(self):
            '''Поворот персонажа к курсору мыши'''
            mouse_pos = pygame.mouse.get_pos()
            direction = Vector2(mouse_pos) - Vector2(self.rect.center)


            self.angle = direction.as_polar()[1]
            self.image = pygame.transform.rotate(self.orig_image, -self.angle - 90)
            self.image.set_colorkey((255, 255, 255))

            old_center = self.rect.center
            self.rect = self.image.get_rect()
            self.rect.center = old_center
            self.screen.blit(self.image, self.rect)
    def move(self):
                pass
    def cooldown(self):
        current_time = pygame.time.get_ticks()
        if self.shoot:
            if current_time - self.shoot_time >= self.cooldown_shoot:
                self.shoot = False
                self.status = 'stand'
    def imp(self):
        self.update()
        self.rotate()
        self.cooldown()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, start_pos, target_pos,angle):
        super().__init__()
        self.image = pygame.image.load('image/action_img/Bullet.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.image.set_colorkey((255,255,255))

        self.rect = self.image.get_rect()
        self.rect.center = start_pos
        self.bullet_speed = 70

        self.angle = angle
        direction = pygame.math.Vector2(target_pos) - pygame.math.Vector2(start_pos)
        if direction.length() != 0:
            direction = direction.normalize()
        self.speedx = direction.x * self.bullet_speed
        self.speedy = direction.y * self.bullet_speed

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

    def draw(self, screen):
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        rotated_image.set_colorkey((255, 255, 255))
        self.rect = rotated_image.get_rect(center=self.rect.center)
        screen.blit(rotated_image, self.rect)
class mouse(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.image = pygame.image.load('image/action_img/sprite_0.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.screen = screen

        self.img_lst = []
        for i in range(0,4):
            img = pygame.image.load(f'image/action_img/sprite_{i}.png')
            img = pygame.transform.scale(img, (50, 50))
            self.img_lst.append(img)
        self.sprites_now = 0
        self.speed_sprites = 0.15
    def update(self):
        self.rect.center = pygame.mouse.get_pos()

    def draw(self):
        self.sprites_now += self.speed_sprites
        self.sprites_now %= len(self.img_lst)
        self.image = self.img_lst[int(self.sprites_now)]
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect(center=self.rect.center)
        self.screen.blit(self.image, self.rect.center)