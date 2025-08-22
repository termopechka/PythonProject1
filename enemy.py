import pygame
from pygame.math import Vector2
from math import sqrt
import random

class Enemy(pygame.sprite.Sprite):
    """Класс врага, наследуется от pygame.sprite.Sprite, содержит методы для инициализации врага, атаки, обновления состояния, поворота к игроку, проверки на попадание и отрисовки полоски здоровья"""
    def __init__(self, speed,):
        super().__init__()

        self.list_sprites = []
        for i in range(3):
            img = pygame.image.load(f'image/enemy/sprite_{i}.png')
            img = pygame.transform.scale(img, (100, 100))
            img.set_colorkey((255, 255, 255))
            self.list_sprites.append(img)
        self.image = self.list_sprites[0]
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.image.set_colorkey((255, 255, 255))
        self.sprites_now = 0
        self.speed_sprites = 0.15
        self.orig_image = self.image


        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center=(random.randint(0, 800), random.randint(0, 700)))
        self.speed = speed
        self.HEALTH = 100 # Здоровье врага
        self.damage = 1

        self.angle = 0
        self.status = 'move'  # 'stand', 'move', 'shoot'

    def atack(self, player_mask, player_x, player_y):
        """Проверка на попадание в игрока
        :param player_mask: Маска игрока
        :param player_x: Координата X игрока
        :param player_y: Координата Y игрока"""
        if self.HEALTH > 0:
            offset = (self.rect.x - player_x-10, self.rect.y - player_y-10)
            self.distance = sqrt((self.rect.x - player_x) ** 2 + (self.rect.y - player_y) ** 2)
            if self.mask.overlap(player_mask, offset):
                self.status = 'attack'
                return True
            else:
                if 40 < self.distance <= 350:
                    self.status = 'move'
                elif self.distance > 350:
                    self.status = 'stand'
                    return False



    def update(self ,player_x,player_y):
        """Обновление состояния врага"""

        if self.status == 'attack':
            self.sprites_now += self.speed_sprites
            if self.sprites_now >= len(self.list_sprites):
                self.sprites_now = 0
            self.image = self.list_sprites[int(self.sprites_now)]
            self.orig_image = self.image
        if self.status == 'stand':
            self.image = self.list_sprites[0]
            self.orig_image = self.image
        if self.status == 'move':
            dx = player_x - self.rect.x
            dy = player_y - self.rect.y
            if dx != 0 or dy != 0:
                length = sqrt(dx * dx + dy * dy)
                dx ,dy =  dx / length ,dy / length


                # Двигаемся с заданной скоростью
                self.rect.x += dx * self.speed
                self.rect.y += dy * self.speed


    def rotate_to_player(self, screen,player_pos):
        """Поворот врага к игроку
        :param screen: Экран для отрисовки
        :param player_pos: Позиция игрока
        Поворачивает изображение врага к позиции игрока и отрисовывает его на экране"""
        self.angle = Vector2(player_pos) - Vector2(self.rect.center)
        self.angle = self.angle.as_polar()[1]
        self.image = pygame.transform.rotate(self.orig_image, -self.angle - 90)
        self.image.set_colorkey((255, 255, 255))
        old_center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = old_center
        screen.blit(self.image, self.rect)

    def atacble(self, bullet_group,h):
        """Проверка на попадание пули в врага
        :param bullet_group: Группа пуль
        Проверяет пересечение прямоугольника врага с прямоугольниками пуль,
        если пересечение есть, то уменьшает здоровье врага на 10 и удаляет пулю из группы.
        Если здоровье врага меньше или равно 0, то удаляет врага из группы"""
        for bullet in bullet_group:
            if self.rect.colliderect(bullet) :
                self.HEALTH -= 10
                bullet.kill()
            if self.HEALTH <= 0:
                self.kill()
                h.exp += 20
                print(h.exp)


    def draw_hp(self):
        """Отрисовка полоски здоровья врага"""
        pygame.draw.rect(self.orig_image, (181, 45, 68), (37, 80,100//2, 10))
        pygame.draw.rect(self.orig_image, (70, 181, 45), (37, 80, self.HEALTH //2, 10))



