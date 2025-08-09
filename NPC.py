import pygame, math

# class Parents(pygame.sprite.Sprite):
#     def __init__(self, string):
#         super().__init__()
#         self.lst = []
#         for i in range(0,4):
#             img = pygame.image.load(f'image/action_img/{string}_{i}.png')
#             img = pygame.transform.scale(img, (50, 50))
#             self.lst.append(img)
#         self.sprites_now = 0
#         self.speed_sprites = 0.15
#     def update(self):
#         self.sprites_now += self.speed_sprites
#         self.sprites_now %= len(self.lst)
#         self.image = self.lst[int(self.sprites_now)]
#         self.image.set_colorkey((255, 255, 255))
#         self.rect = self.image.get_rect(center=self.rect.center)
#     def draw(self, screen):
#         screen.blit(self.image, self.rect.center)
#

class NPC(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.radius = 10
        self.isdialogactive = False
        self.icon_interaction = pygame.transform.scale(pygame.image.load('image/images.jpg'), (50, 50))
        self.list = []
        for i in range(0,4):
            img = pygame.image.load(f'image/images.jpg')
            img = pygame.transform.scale(img, (150, 150))
            self.list.append(img)
        self.sprites_now = 0
        self.speed_sprites = 0.15
    def detect_player(self, x, y, screen):
        self.distance = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)
        if self.distance <= self.radius:
            screen.blit(self.icon_interaction, (50, 50))

    def update(self):
        self.sprites_now += self.speed_sprites
        self.sprites_now %= len(self.list)
        self.image = self.list[int(self.sprites_now)]
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect(center=(0,0))

    def draw_npc(self, screen):
        screen.blit(self.image, (50, 50))

