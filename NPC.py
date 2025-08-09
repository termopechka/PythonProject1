import pygame

class Parents(pygame.sprite.Sprite):
    def __init__(self, string):
        super().__init__()
        self.lst = []
        for i in range(0,4):
            img = pygame.image.load(f'image/action_img/{string}_{i}.png')
            img = pygame.transform.scale(img, (50, 50))
            self.lst.append(img)
        self.sprites_now = 0
        self.speed_sprites = 0.15
    def update(self):
        self.sprites_now += self.speed_sprites
        self.sprites_now %= len(self.lst)
        self.image = self.lst[int(self.sprites_now)]
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect(center=self.rect.center)
    def draw(self, screen):
        screen.blit(self.image, self.rect.center)

