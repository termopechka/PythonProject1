from Hero import Hero,mouse
from Key_action import *
from background import *
from Setting import *
pygame.init()
clock = pygame.time.Clock()


'''Включение шансона в жигулях'''
# music = pygame.mixer.music.load('music/Cyberpunk_2077_-_Johnny_Silverhand_s_Theme_Cello_Version_(SkySound.cc).mp3')
# # music = pygame.mixer.music.load('music/samurai-never-fade-away-full-instrumental-cover_(get-tune.net).mp3')
# pygame.mixer.music.play(-10)

'''Обявление екрана екраном, выдача кликухи окну итд'''
screen = pygame.display.set_mode((h,w))
pygame.display.set_caption('Live solo')
icon = pygame.image.load('image/assets_task_01k1476qdmfjsr95yxtwsdf192_1753562211_img_1.PNG')
pygame.display.set_icon(icon)

bullet_group = pygame.sprite.Group()
hero = Hero(screen,x, y, hero_speed)
mouse = mouse(screen)

# Кушать какашки не причмокивая
map = TileMap('untitled.csv', spritesheet=hero.image)

pygame.mouse.set_visible(False)
running = True
while running:
    screen.fill((100,100,100))
    mouse.update()
    mouse.draw()
    hero.imp()
    map.draw_map(screen)
    controls(hero, bullet_group)
    bullet_group.update()
    custom_group_draw(bullet_group, screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()