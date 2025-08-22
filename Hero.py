import math

import pygame
from pygame.math import Vector2
from pygame.transform import rotate


class Hero(pygame.sprite.Sprite):
    '''Класс персонажа, наследуется от pygame.sprite.Sprite, содержит методы для инициализации персонажа, обновления состояния, поворота к курсору мыши, проверки на время перезарядки стрельбы и отрисовки полосок здоровья и человечности'''
    def __init__(self, screen, x=512, y=384,Implants = None, speed=4,health=100, humanize=100,cooldown_shoot=400,harizm = 0, level=1, exp=0, point=0):
        ''' инициализация персонажа принимает екран для отрисовки изображения, координаты и скорость
        внутри метода есть , 5 основных атрибутов как в рпг, здоровье, человечность, скорость, харизма
        и уровень, также есть атрибуты для инвентаря, имплантов и снаряжения, а также атрибуты для стрельбы
        и анимации персонажа, такие как список изображений для ходьбы и стрельбы, скорость смены кадров и статус персонажа'''
        super().__init__()
        self.image = pygame.image.load('image/hero_img/state/Layer 1_sprite_01.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.image.set_colorkey((255, 255, 255))
        self.orig_image = self.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.angle = None
        self.mask = pygame.mask.from_surface(self.image)



        self.implants = [] if Implants == None else Implants.split(',')  # Импланты персонажа

        self.HEALTH = health  # Здоровье
        self.humanize = humanize - len(self.implants) * 20 # Человечность
        self.cooldown_shoot_baze = cooldown_shoot
        self.cooldown_shoot = self.cooldown_shoot_baze  # Время перезарядки стрельбы
        self.speed = speed # Скорость движения
        self.harizm = harizm  # Харизма


        self.level = 1
        self.exp = 0 if exp >= 80 + level * 20 else exp
        self.point = 0


        self.HEALTH1 = self.HEALTH  # Здоровье для отрисовки полоски здоровья

        self.sprint = speed * 1.5  # Ускорение
        self.sprint_with_sandevistan = speed * 3
        self.sprint_without_sandevistan = speed * 1.5
        self.shoot = None
        self.sandevistan_time = 0

        self.trail = []
        self.sandevistan_activite = False
        self.cooldown_trail = 200


        self.dilog = False
        self.dilog_now = 0
        self.sprites_now = 0
        self.speed_sprites = 0.15
        self.status = 'stand'
        self.walk_list = []
        for i in range(1, 5):
            img = pygame.image.load(f'image/hero_img/state/Layer 1_sprite_0{i}.png')
            img = pygame.transform.scale(img, (100, 100))
            img.set_colorkey( (255,255,255))
            self.walk_list.append(img)

        self.shoot_list = []
        for i in range(6, 10):
            img = pygame.image.load(f'image/hero_img/Shoot/Layer 1_sprite_0{i}.png')
            img = pygame.transform.scale(img, (100, 100))
            img.set_colorkey((255, 255, 255))
            self.shoot_list.append(img)
        self.screen = screen
    def return_main_attributes(self):
        return  None,','.join(self.implants) if self.implants != [] else None, self.speed+1, self.HEALTH , self.humanize,  self.cooldown_shoot,   self.harizm, self.level,self.exp, self.point

    def update(self):
        '''Обновление состояния персонажа, смена кадров анимации в зависимости от статуса'''
        self.sprites_now += self.speed_sprites
        if self.sprites_now >= len(self.walk_list):
            self.sprites_now = 0
        if self.status == 'move':
            self.image = self.walk_list[int(self.sprites_now)]
            self.orig_image = self.image
        elif self.status == 'shoot' :
            self.image = self.shoot_list[int(self.sprites_now)]
            self.orig_image = self.image

        elif self.status == 'stand':
            self.image = self.walk_list[0]
            self.orig_image = self.image
    def get_rotation_angle(self):
        '''Получение угла поворота персонажа к курсору мыши'''
        direction = pygame.mouse.get_pos() - Vector2(self.rect.centerx, self.rect.centery)
        return -direction.as_polar()[1] - 90
    def rotate(self):
            '''Поворот персонажа к курсору мыши по средству вычетания вектора координат центра персонажа и вектора курсора мыши,'''
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
        '''Проверка на время перезарядки стрельбы, если время перезарядки прошло, то статус персонажа меняется на "stand"'''
        current_time = pygame.time.get_ticks()
        if self.shoot:
            if current_time - self.shoot_time >= self.cooldown_shoot:
                self.shoot = False
                self.status = 'stand'

    def draw_track(self):

        if self.sandevistan_activite:
            self.sandevistan_time += 0.15
            self.sprint = self.sprint_with_sandevistan
            self.trail.append({
                'x': self.rect.x,
                'y': self.rect.y,
                'rotation':-self.angle-90,
                'image':self.orig_image
            })
            if len(self.trail) > 20:
                del self.trail[0]
            for i in range(len(self.trail) - 1):
                self.trail[i]['image'].set_alpha(100)
                self.screen.blit(pygame.transform.rotate(self.trail[i]['image'], self.trail[i]['rotation']), (self.trail[i]['x'], self.trail[i]['y']))
        else:
            self.sprint = self.sprint_without_sandevistan
            self.orig_image.set_alpha(255)
            self.trail = []




    def draw_hp_image(self):
        '''Меняет лицо игрока в зависимости от уровня здоровья, если здоровье больше 80, то лицо без повреждений, если меньше 80, но больше 40, то лицо разбито, если меньше 40, то лицо в мясо'''
        if self.HEALTH1 > 0:
            self.hp = None
            if self.HEALTH > 80:
                self.hp = pygame.image.load('image/hero_img/hp/Layer 1_Hero_hp1.png')
            elif self.HEALTH > 40:
                self.hp = pygame.image.load('image/hero_img/hp/Layer 1_Hero_hp2.png')
            elif self.HEALTH > 0:
                self.hp = pygame.image.load('image/hero_img/hp/Layer 1_Hero_hp3.png')
            self.hp = pygame.transform.scale(self.hp, (90, 90))
            self.screen.blit(self.hp, (10, 10))


    def draw_humanizm(self):
        '''рисует человечность игрока и отображает ее в виде заполнености шприцов с имунодипресантами, если человечность больше 100, то рисуется 5 полных шприцов , если меньше 100, то рисуется столько изображений, сколько человечности деленное на 20'''
        self.hmnz = []
        print(self.implants)
        for i in range(5 - len(self.implants)):
            img = pygame.image.load(f'image/hero_img/humanizm/shprc_0.png')
            img = pygame.transform.scale(img, (100, 100))
            self.hmnz.append(img)
        if len(self.hmnz) < 5:
            for i in range(5 - len(self.hmnz)):
                img = pygame.image.load(f'image/hero_img/humanizm/shprc_1.png')
                img = pygame.transform.scale(img, (100, 100))
                self.hmnz.append(img)
        for i in self.hmnz:
            self.screen.blit(i, (10, (self.hmnz.index(i) * 20) + 80))


    def draw_hp(self):
        '''Рисует полоску здоровья игрока, если здоровье меньше 100, то рисуется желтая полоска, которая уменьшается в зависимости от здоровья, если здоровье больше 100, то рисуется зеленая полоска'''
        if self.HEALTH1 != self.HEALTH:
            pygame.draw.rect(self.screen, (252, 186, 3), (97, 25, (self.HEALTH1 * 2)  , 20))
            self.HEALTH1 -= 0.5 if self.HEALTH1 > self.HEALTH else 0
        pygame.draw.rect(self.screen, (70, 181, 45), (97, 25, (self.HEALTH * 2) , 20))


    def imp(self):
        '''Импорт персонажа, обновление состояния персонажа, поворот персонажа к курсору мыши, проверка на время перезарядки стрельбы, отрисовка полоски здоровья и человечности'''
        self.draw_track()
        self.update()
        self.rotate()
        self.cooldown()
        self.draw_hp_image()
        self.draw_hp()
        self.draw_humanizm()

class Bullet(pygame.sprite.Sprite):
    '''Класс пули, наследуется от pygame.sprite.Sprite, содержит методы для инициализации пули, обновления состояния и отрисовки пули'''
    def __init__(self, start_pos, target_pos, angle):
        '''Инициализация пули, принимает начальную позицию, конечную позицию и угол поворота пули'''
        super().__init__()
        self.image = pygame.image.load('image/action_img/pyla_vrag0.png')
        self.image = pygame.transform.scale(self.image, (10, 10))
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
        '''Обновление состояния пули, перемещение пули в зависимости от скорости и угла поворота'''
        self.rect.x += self.speedx
        self.rect.y += self.speedy

    def draw(self, screen):
        '''Отрисовка пули, поворот пули в зависимости от угла поворота'''
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        rotated_image.set_colorkey((255, 255, 255))
        self.rect = rotated_image.get_rect(center=self.rect.center )
        screen.blit(rotated_image, self.rect)

class mouse(pygame.sprite.Sprite):
    '''Класс мыши, наследуется от pygame.sprite.Sprite, содержит методы для инициализации мыши, отрисовки анимации мыши'''
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


    def draw(self,mouse_pos):
        '''Отрисовка мыши, смена кадров анимации в зависимости от времени'''
        self.rect.center = (mouse_pos[0]-25, mouse_pos[1]-23)

        self.sprites_now += self.speed_sprites
        self.sprites_now %= len(self.img_lst)
        self.image = self.img_lst[int(self.sprites_now)]
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect(center=self.rect.center)
        self.screen.blit(self.image, self.rect.center)
