from Hero import Hero
from Key_action import *
pygame.init()




clock = pygame.time.Clock()
SETING = 1
h = 1200
w = 800
'''атрибуты героя'''
x = h // 2
y = w // 2
hero_speed = 5
'''Включение шансона в жигулях'''
music = pygame.mixer.music.load('music/Cyberpunk_2077_-_Johnny_Silverhand_s_Theme_Cello_Version_(SkySound.cc).mp3')
# music = pygame.mixer.music.load('music/samurai-never-fade-away-full-instrumental-cover_(get-tune.net).mp3')
pygame.mixer.music.play(-10)

'''Обявление екрана екраном, выдача кликухи окну итд'''
screen = pygame.display.set_mode((h,w))
pygame.display.set_caption('Live solo')
icon = pygame.image.load('image/assets_task_01k1476qdmfjsr95yxtwsdf192_1753562211_img_1.PNG')
pygame.display.set_icon(icon)


hero = Hero(screen,x, y, hero_speed)

running = True
while running:
    screen.fill((100,0,0))
    hero.update()
    hero.rotate()
    controls(hero)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()