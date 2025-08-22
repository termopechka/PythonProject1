import pygame
from math import sqrt


class NPC(pygame.sprite.Sprite):
    def __init__(self, x:int, y:int,name = 'No have',lst_sprites = [f'image/Npc/Layer 1_test{i}.png' for i in range(1,5)],font = 'font/DIGITALPIXELV4-REGULAR.ttf',size=[100, 100],dialog = ['Hello, I am a NPC!', 'How can I help you?']):
        """Класс NPC, наследуется от pygame.sprite.Sprite, содержит методы для инициализации NPC, обновления состояния и отрисовки NPC
        :param x: Координата X NPC в int
        :param y: Координата Y NPC в int
        :param name: Имя NPC
        :param lst_sprites: Список изображений для анимации NPC
        :param font: Шрифт для отображения имени NPC
        """
        super().__init__()
        self.size = size
        self.font = font
        self.x = x
        self.y = y
        self.radius = 100
        self.icon_interaction = pygame.transform.scale(pygame.image.load('image/Npc/action0.png'), (50, 50))
        self.name = name
        self.list = []
        for img in lst_sprites:
            image = pygame.image.load(img)
            image = pygame.transform.scale(image, (self.size[0], self.size[1]))
            self.list.append(image)
        self.image = self.list[0]
        self.sprites_now = 0
        self.speed_sprites = 0.08
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect(center=(x, y))
        self.dialog = dialog
        self.dialog_index = 0
    def detect_player(self, x, y, screen):
        self.distance = sqrt((self.x - x) ** 2 + (self.y - y) ** 2)
        if self.distance <= self.radius:
            screen.blit(self.icon_interaction, (self.x+30, self.y- 30))
            return True
        else:
            return False


    def update(self):
        self.sprites_now += self.speed_sprites
        self.sprites_now %= len(self.list)
        self.image = self.list[int(self.sprites_now)]
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect(center=(0,0))

    def draw_npc(self, screen):
        pygame.font.init()
        if self.font is None:
            font = 'freesansbold.ttf'
        else:
            font = self.font
        font = pygame.font.Font(self.font, 10)
        text = font.render(self.name, True, (255, 255, 255))
        screen.blit(text, (self.x - text.get_width() // 2 + 50, self.y - text.get_height() + 30))
        screen.blit(self.image, (self.x, self.y))
    def dialogue(self,screen,harizm = 0):
        """Метод для отображения диалога NPC, в будущем можно добавить логику диалога"""
        if self.font is None:
            font = 'freesansbold.ttf'
        else:
            font = self.font
        font = pygame.font.Font(self.font, 30)
        if harizm < 3:
            self.dialog_index = 0
        elif harizm >= 3:
            self.dialog_index = 1

        text = font.render(self.name + ':' + self.dialog[self.dialog_index], True, (255, 255, 255))
        pygame.draw.rect(screen, (0,0,0), (100,668,1024,50), )
        screen.blit(text, (100,668))
    def imp(self,hero, screen):
        """Метод для импорта NPC на карту, принимает координаты и экран"""
        self.update()
        self.draw_npc(screen)
        if self.detect_player(hero.rect.x, hero.rect.y, screen) and hero.dilog: # проверка на игрока
            self.dialogue(screen,hero.harizm)
        elif not self.detect_player(hero.rect.x, hero.rect.y, screen):
            self.dialog_index = 0
            hero.dilog = False

