import pygame
from pygame.math import Vector2

class Enemy(pygame.sprite.Sprite):
    def __init__(self, position, speed,):
        super().__init__()

        self.list_sprites = []
        for i in range(1, 4):
            img = pygame.image.load(f'image/enemy/Layer 1_sprite_{i}.png')
            img = pygame.transform.scale(img, (150, 150))
            img.set_colorkey((255, 255, 255))
            self.list_sprites.append(img)
        self.image = self.list_sprites[0]
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.image.set_colorkey((255, 255, 255))
        self.sprites_now = 0
        self.speed_sprites = 0.15
        self.orig_image = self.image

        self._layer = 1

        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center=position)
        self.speed = speed
        self.HEALTH = 79
        self.damage = 0.1

        self.angle = 0
        self.status = 'move'  # 'stand', 'move', 'shoot'

    # def update(self):
    #     if self.status == 'move' and self.rect.center[1] < 800:
    #         self.rect.center = (self.rect.center[0] + self.speed, self.rect.center[1] + self.speed)
    def atack(self,player_pos):
        """Проверка на атаку"""
        # Проверяем, находится ли игрок в радиусе атаки
        # Например, радиус атаки 50 пикселей
        # Здесь player_pos - это позиция игрока (x, y)
        # self.rect - это прямоугольник врага
        if self.rect.colliderect(pygame.Rect(player_pos[0] - 50, player_pos[1] - 50, 100, 100)):
            return True
        return False
    def update(self, player_pos):

        """Обновление состояния врага"""
        # Проверяем, находится ли игрок в радиусе атаки
        # Если да, то враг атакует
        # Если нет, то враг просто движется к игроку

        if self.atack( player_pos):
            self.sprites_now += self.speed_sprites
            self.sprites_now %= len(self.list_sprites)
            self.image = self.list_sprites[int(self.sprites_now)]
            self.image.set_colorkey((255, 255, 255))
            self.rect = self.image.get_rect(center=self.rect.center)
            self.orig_image = self.image
        else:
            self.image = self.list_sprites[0]
            self.image.set_colorkey((255, 255, 255))
            self.rect = self.image.get_rect(center=self.rect.center)

    def rotate_to_player(self, screen,player_pos):

        self.angle = Vector2(player_pos) - Vector2(self.rect.center)
        self.angle = self.angle.as_polar()[1]
        self.image = pygame.transform.rotate(self.orig_image, -self.angle - 90)
        self.image.set_colorkey((255, 255, 255))
        old_center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = old_center
        screen.blit(self.image, self.rect)
    def atacble(self, bullet_group):
        for bullet in bullet_group:
            if self.rect.colliderect(bullet):
                self.HEALTH -= 10
                bullet.kill()
            if self.HEALTH <= 0:
                self.kill()
                bullet_group.remove(bullet)


    def draw_hp(self):
        pygame.draw.rect(self.orig_image, (70, 181, 45), (37, 50, self.HEALTH  , 10))
        pygame.draw.rect(self.orig_image, (181, 45, 68), (37, 50, (100 - self.HEALTH ) , 10))

