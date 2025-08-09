import math

import pygame
from pygame.math import Vector2
from pygame.transform import rotate


class Hero(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, speed):
        ''' инициализация персонажа'''
        super().__init__()
        self.image = pygame.image.load('image/hero_img/state/Layer 1_sprite_01.png')
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.image.set_colorkey((255, 255, 255))
        self.orig_image = self.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.angle = None

        self._layer = 10

        self.HEALTH1 = 100
        self.HEALTH = 100
        self.invnt = []
        self.implants = []
        self.speed = speed
        self.sprint = speed * 2
        self.humanize = 100  # Человечность
        self.cooldown_shoot = 400
        self.shoot = None

        self.sprites_now = 0
        self.speed_sprites = 0.15
        self.status = 'stand'
        self.walk_list = []
        for i in range(1, 5):
            img = pygame.image.load(f'image/hero_img/state/Layer 1_sprite_0{i}.png')
            img = pygame.transform.scale(img, (150, 150))
            img.set_colorkey( (255,255,255))
            self.walk_list.append(img)

        self.shoot_list = []
        for i in range(6, 10):
            img = pygame.image.load(f'image/hero_img/Shoot/Layer 1_sprite_0{i}.png')
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
    def cooldown(self):
        current_time = pygame.time.get_ticks()
        if self.shoot:
            if current_time - self.shoot_time >= self.cooldown_shoot:
                self.shoot = False
                self.status = 'stand'

    def draw_hp_image(self):

        self.hp = None
        if self.HEALTH > 80:
            self.hp = pygame.image.load('image/hero_img/hp/Layer 1_Hero_hp1.png')
        elif self.HEALTH > 40:
            self.hp = pygame.image.load('image/hero_img/hp/Layer 1_Hero_hp2.png')
        elif self.HEALTH > 0:
            self.hp = pygame.image.load('image/hero_img/hp/Layer 1_Hero_hp3.png')
        self.hp = pygame.transform.scale(self.hp, (200, 200))
        self.screen.blit(self.hp, (10, 10))


    def draw_humanizm(self):
        self.hmnz = []
        for i in range(self.humanize // 20):
            img = pygame.image.load(f'image/hero_img/humanizm/shprc_0.png')
            img = pygame.transform.scale(img, (50, 50))
            self.hmnz.append(img)
        if len(self.hmnz) < 5:
            for i in range(5 - len(self.hmnz)):
                img = pygame.image.load(f'image/hero_img/humanizm/shprc_1.png')
                img = pygame.transform.scale(img, (50, 50))
                self.hmnz.append(img)
        for i in self.hmnz:
            self.screen.blit(i, (90, (self.hmnz.index(i) * 10) + 90))


    def draw_hp(self):
        if self.HEALTH1 != self.HEALTH:
            pygame.draw.rect(self.screen, (252, 186, 3), (90, 65, (self.HEALTH1 * 2)  , 20))
            print(self.HEALTH1)
            self.HEALTH1 -= 0.5 if self.HEALTH1 > self.HEALTH else 0
        pygame.draw.rect(self.screen, (70, 181, 45), (90, 65, (self.HEALTH * 2) , 20))


    def imp(self):
            self.update()
            self.rotate()
            self.cooldown()
            self.draw_hp_image()
            self.draw_hp()
            self.draw_humanizm()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, start_pos, target_pos, angle):
        super().__init__()
        self.image = pygame.image.load('image/action_img/New Piskel-1.png (3).png')
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.image.set_colorkey((255,255,255))

        self.mask = pygame.mask.from_surface(self.image)
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
        self.rect = rotated_image.get_rect(center=self.rect.center )
        screen.blit(rotated_image, self.rect)

class mouse(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.image = pygame.image.load('image/action_img/Layer 1_Cursor1.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.screen = screen
        self._layer = 20
        self.img_lst = []
        for i in range(0,8):
            img = pygame.image.load(f'image/action_img/sprite_{i}.png')
            img = pygame.transform.scale(img, (100, 100))
            self.img_lst.append(img)
        self.sprites_now = 0
        self.speed_sprites = 0.15


    def draw(self):
        self.rect.center = (pygame.mouse.get_pos()[0]-25, pygame.mouse.get_pos()[1]-23)

        self.sprites_now += self.speed_sprites
        self.sprites_now %= len(self.img_lst)
        self.image = self.img_lst[int(self.sprites_now)]
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect(center=self.rect.center)
        self.screen.blit(self.image, self.rect.center)
