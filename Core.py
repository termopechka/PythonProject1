import pygame.time
import sqlite3
from Hero import Hero,mouse
from Key_action import controls, custom_group_draw
from background import *
from Setting import h, w, enemy_x, enemy_y, enemy_speed,x, y, npc_x, npc_y,Implant,Speed,Health,Humanizm,Coldown,harizm,Level,Exp,Point
from enemy import Enemy
from pygame.sprite import LayeredUpdates
from Menu import Button, Menu
from NPC import NPC
pygame.init()
clock = pygame.time.Clock()
last_save_time = 0
save_cooldown = 500

action = False
status_music = True
if status_music:
    if action :
        music = pygame.mixer.music.load('sounds/music/samurai-never-fade-away-full-instrumental-cover_(get-tune.net).mp3')
    elif not action:
        music = pygame.mixer.music.load('sounds/music/Cyberpunk_2077_-_Johnny_Silverhand_s_Theme_Cello_Version_(SkySound.cc).mp3')
    pygame.mixer.music.play(-10)


screen = pygame.display.set_mode((h,w))
pygame.display.set_caption('Live solo')
icon = pygame.image.load('image/assets_task_01k1476qdmfjsr95yxtwsdf192_1753562211_img_1.PNG')
pygame.display.set_icon(icon)

pause = True
bullet_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
hero = Hero(screen, x, y, Implant, Speed, Health, Humanizm, Coldown, harizm, Level, Exp, Point,)
mouse = mouse(screen)
en = Enemy( (enemy_x, enemy_y), enemy_speed,)
enemy_group.add(en)



npc = NPC(400, 650,font='font/DIGITALPIXELV4-REGULAR.ttf', name='Фиксер',lst_sprites=[f'image/Npc/Layer 1_fixer{i}.png' for i in range(1,5)],size=[100, 100])

map = TileMap('untitled.csv', spritesheet=hero.image)
pygame.mouse.set_visible(False)
running = True

play = Button(x//2 +170, y//2, 200, 100, 'play.png', 'play_select.png', 'play_click.png')
save = Button(x//2 + 170, y//2 + 120, 200, 100, 'save.png', 'save_select.png', 'save_click.png')
sound_play = Button(x//2 + 170, y//2 + 240, 200, 100, 'sound.png', 'sound_select.png', 'sound_click.png')
sound_mute = Button(x//2 + 170, y//2 + 240, 200, 100, 'sound_mute.png', 'sound_mute_select.png', 'sound_mute_click.png')
menu = Menu(screen, [play, save, sound_play], )

while running:
    screen.fill((150, 100, 100))
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()
    # управление игроком
    controls(hero, bullet_group, menu)

    # кнопки
    menu.draw()
    menu.update(mouse_pos, mouse_pressed)

    if menu.view:
        for button in menu.list_buttons:
            button.update(mouse_pos, mouse_pressed)
            button.draw(screen)
            current_time = pygame.time.get_ticks()
            if button.is_clicked(mouse_pos, mouse_pressed):
                if button == play:
                    menu.view = False
                elif button == save:
                    if current_time - last_save_time > save_cooldown:
                        with sqlite3.connect('data_base/Db1.sqlite3') as con:
                            cur = con.cursor()
                            data = [
                                hero.return_main_attributes()
                            ]
                            cur.executemany("INSERT INTO SAVES VALUES(?,?,?,?,?,?,?,?,?,?)", data)
                            con.commit()
                        last_save_time = current_time

                elif button == sound_play:
                    pygame.mixer.music.pause()
                    status_music = False
                    menu = Menu(screen, [play, save, sound_mute], )
                elif button == sound_mute:
                    pygame.mixer.music.unpause()
                    status_music = True
                    menu = Menu(screen, [play, save, sound_play], )
    else:

        if enemy_group:
            for enemy in enemy_group:
                enemy.draw_hp() #хп врага
                enemy.rotate_to_player(screen, hero.rect.center) #врага к игроку
                enemy.update(hero.mask)#анимация врага
                enemy.atacble(bullet_group)  # проверка на попадание пули в врага
                enemy.atack(hero.mask, hero.rect.x, hero.rect.y)
                if  enemy.status == 'attack' and enemy.sprites_now >= len(enemy.list_sprites) - 1:
                    hero.HEALTH -= enemy.damage
        # импорт игрока
        hero.imp()
        # отрисовка пуль
        bullet_group.update()
        custom_group_draw(bullet_group, screen)
        # анимация мышки
        npc.imp(hero,screen)

        # отрисовка карты
        map.draw_map(screen)
    mouse.update()
    mouse.draw(mouse_pos)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()