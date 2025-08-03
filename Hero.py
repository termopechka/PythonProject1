import pygame
from pygame.math import Vector2
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


            self.angle = direction.as_polar()[1]  # Угол в градусах

            self.image = pygame.transform.rotate(self.orig_image, -self.angle - 90)
            self.image.set_colorkey((255, 255, 255))

            # 5. Обновляем rect для сохранения позиции
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
    def __init__(self, screen, x, y, speed):
        super().__init__()
        self.image = pygame.image.load('image/action_img/Bullet.png')
        self.image = pygame.transform.scale(self.image, (10, 10))
        self.image.set_colorkey( (255,255,255))
        self.speed = speed
        self.x = x
        self.y = y
        self.screen = screen
    def update(self,direction_x,direction_y):
        pass