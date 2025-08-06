import pygame
from pygame.math import Vector2

class Enemy(pygame.sprite.Sprite):
    def __init__(self, image_path, position, speed):
        super().__init__()
        self.image = pygame.image.load('image/enemy/' + image_path + '.png')
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.image.set_colorkey((255, 255, 255))
        self.orig_image = self.image

        self.rect = self.image.get_rect(center=position)
        self.speed = speed

        self.angle = 0
        self.status = 'move'  # 'stand', 'move', 'shoot'
    def update(self):
            match self.status:
                case 'stand':
                    self.image = self.orig_image
                case 'move':
                    self.rect.x += self.speed[0]
                    self.rect.y += self.speed[1]
    def rotate_to_player(self, screen, player_pos):
        self.angle = Vector2(self.rect.center) - Vector2(player_pos)
        self.angle = self.angle.as_polar()[1]
        self.image = pygame.transform.rotate(self.orig_image, -self.angle - 90)
        self.image.set_colorkey((255, 255, 255))
        old_center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = old_center
        screen.blit(self.image, self.rect)


