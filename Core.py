import pygame.time
import sqlite3
import os
import pytmx
from pytmx.util_pygame import load_pygame
from Hero import Hero,mouse
from Key_action import controls, custom_group_draw
from background import *
from Setting import h, w, enemy_count, enemy_speed, x, y, Implant, Speed, Health, Humanizm, Coldown, harizm, Level, Exp, Point
from enemy import Enemy
from pygame.sprite import LayeredUpdates
from Menu import Button, Menu
from NPC import NPC

from camera import create_screen
from camera import camera
from Implants import Implants
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




screen = create_screen(h, w, 'Live solo')
icon = pygame.image.load('image/assets_task_01k1476qdmfjsr95yxtwsdf192_1753562211_img_1.PNG')
pygame.display.set_icon(icon)

pause = True
bullet_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
objects = pygame.sprite.Group()
hero = Hero(screen, x, y, Implant, Speed, Health, Humanizm, Coldown, harizm, Level, Exp, Point,)
mouse = mouse(screen)
for i in  range(enemy_count):
    en = Enemy(enemy_speed,)
    enemy_group.add(en)



fixer = NPC(400, 650,font='font/DIGITALPIXELV4-REGULAR.ttf', name='Фиксер',lst_sprites=[f'image/Npc/Layer 1_fixer{i}.png' for i in range(1,5)],size=[100, 100], dialog=['Hey!'])




map = load_pygame(os.path.join('image', 'back', 'city.tmx'))
map_width = map.width * map.tilewidth
map_height = map.height * map.tileheight

pygame.mouse.set_visible(False)
running = True

play = Button(x//2 +170, y//2-60, 200, 100, 'play.png', 'play_select.png', 'play_click.png')
save = Button(x//2 + 170, y//2 + 60, 200, 100, 'save.png', 'save_select.png', 'save_click.png')
sound_play = Button(x//2 + 170, y//2 + 180, 200, 100, 'sound.png', 'sound_select.png', 'sound_click.png')
sound_mute = Button(x//2 + 170, y//2 + 180, 200, 100, 'sound_mute.png', 'sound_mute_select.png', 'sound_mute_click.png')
about_us = Button(x//2 + 170 , y//2 + 300 , 200 ,100,'about_us.png','about_us_select.png','about_us_click.png')
menu = Menu(screen, [play, save, sound_play,about_us],)

while running:
    implnt = Implants(hero.implants)
    screen.fill((51, 97, 125))
    screen.fill((150, 100, 100))
    for layer in map.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            for x, y, gid in layer:
                tile = map.get_tile_image_by_gid(gid)
                if tile:
                    screen.blit(tile, (x * map.tilewidth - camera.x,
                                       y * map.tileheight - camera.y))

    for obj in map.objects:
        Sprite((obj.x, obj.y), obj.image, objects)
        screen.blit(obj.image, (obj.x - camera.x,
                                obj.y - camera.y))
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()
    # управление игроком
    controls(hero, bullet_group, menu,implnt)

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
                    menu = Menu(screen, [play, save, sound_mute,about_us], )
                elif button == sound_mute:
                    pygame.mixer.music.unpause()
                    status_music = True
                    menu = Menu(screen, [play, save, sound_play,about_us], )
                elif button == about_us:
                    screen.blit(pygame.transform.scale(pygame.image.load('image/action_img/dream_comand.png'),size=(1024,768)), (0, 0))
    else:

        if enemy_group:
            for enemy in enemy_group:
                enemy.draw_hp() #хп врага
                enemy.rotate_to_player(screen, hero.rect.center) #врага к игроку
                enemy.update(hero.rect.x,hero.rect.y)#анимация врага
                enemy.atacble(bullet_group,hero)  # проверка на попадание пули в врага
                enemy.atack(hero.mask, hero.rect.x, hero.rect.y)
                if  enemy.status == 'attack' and enemy.sprites_now >= len(enemy.list_sprites) - 1:
                    hero.HEALTH -= enemy.damage
        # импорт игрока
        hero.imp()
        # отрисовка пуль
        bullet_group.update()
        custom_group_draw(bullet_group, screen)
        # анимация мышки
        # npc.imp(hero,screen)
        lst_with_box = [pygame.transform.scale(pygame.image.load(i), (90, 90)) for i in ['image/hero_img/Imlants/Layer 1_for_imlants1.png',
                        'image/hero_img/Imlants/Layer 1_for_imlants2.png',
                        'image/hero_img/Imlants/Layer 1_for_imlants3.png',
                        'image/hero_img/Imlants/Layer 1_for_imlants4.png']]
        for i in range(len(lst_with_box)):
            screen.blit(lst_with_box[i], (900, 200+(i*100)))
        fixer.imp(hero,screen)

        if implnt.get_implants():
            implants = implnt.get_implants()
            if 'cyber arm' in implants:
                screen.blit(pygame.image.load('image/hero_img/Imlants/cyber_arm.png'), (914, 203))
            if 'sandevistan' in implants:
                screen.blit(pygame.image.load('image/hero_img/Imlants/sandvestan.png'), (913, 310))
            if 'cyber legs' in implants:
                screen.blit(pygame.image.load('image/hero_img/Imlants/cyber_legs.png'), (840, 347))
            if 'cyber face' in implants:
                screen.blit(pygame.image.load('image/hero_img/Imlants/maska0.png'), (840, 447))

    mouse.update()
    mouse.draw(mouse_pos)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()