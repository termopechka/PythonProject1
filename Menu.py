import pygame

class Button:
    """Класс кнопки для меню"""
    def __init__(self, x,y, width, height, image,hover_image,pressed_image ):
        '''Инициализация кнопки принимает координаты, размеры и изображения для состояний кнопки
        x, y - координаты верхнего левого угла кнопки
        width, height - размеры кнопки
        image - изображение кнопки в обычном состоянии
        hover_image - изображение кнопки при наведении
        pressed_image - изображение кнопки при нажатии'''

        self.rect = pygame.Rect(x, y, width, height)

        self.image_name = image
        self.image = pygame.image.load('image/menu_img/' + image)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.hover_image = pygame.image.load('image/menu_img/' + hover_image)
        self.hover_image = pygame.transform.scale(self.hover_image, (width, height))
        self.pressed_image = pygame.image.load('image/menu_img/' + pressed_image)
        self.pressed_image = pygame.transform.scale(self.pressed_image, (width, height))

        self.sound = pygame.mixer.Sound('sounds/action_sound/under_mouse.mp3')

        self.is_hovered = False

    def update(self, mouse_pos, mouse_pressed):
        '''Обновление состояния кнопки, проверка на наведение и нажатие
        mouse_pos - позиция мыши
        mouse_pressed - состояние кнопки мыши (нажата или нет)'''
        if self.rect.collidepoint(mouse_pos[0] + 23 , mouse_pos[1] + 30):
            self.is_hovered = True
            if mouse_pressed[0]:
                self.image = self.pressed_image
            else:
                self.image = self.hover_image
        else:
            self.is_hovered = False
            self.image = pygame.image.load('image/menu_img/' + self.image_name)
            self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))
    def draw(self, screen):
        '''Отрисовка кнопки на экране'''
        screen.blit(self.image, self.rect)
    def is_clicked(self, mouse_pos, mouse_pressed):
        '''Проверка нажатия кнопки мыши на кнопку
        mouse_pos - позиция мыши
        mouse_pressed - состояние кнопки мыши (нажата или нет)'''
        return self.rect.collidepoint(mouse_pos) and mouse_pressed[0]


class Menu:
    ''' Обьеденение кнопок в меню, обновление состояния кнопок и отрисовка их на экране
    screen - экран для отрисовки кнопок
    list_buttons - список кнопок для меню'''

    def __init__(self, screen,list_buttons):
        self.screen = screen
        self.list_buttons = list_buttons

        self.view = False
    def update(self, mouse_pos, mouse_pressed):
        '''Обновление состояния кнопок в меню
        mouse_pos - позиция мыши
        mouse_pressed - состояние кнопки мыши (нажата или нет)'''
        if  self.view:
            for button in self.list_buttons:
                button.update(mouse_pos, mouse_pressed)
                if button.is_clicked(mouse_pos, mouse_pressed):
                    return button

    def draw(self):
        '''Отрисовка кнопок на экране'''
        if self.view == True:
            for button in self.list_buttons:
                button.draw(self.screen)
