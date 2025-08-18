import pygame
import sqlite3
import random
from Hero import Hero

with sqlite3.connect('data_base/Db1.sqlite3') as db:
    cursor = db.cursor()

    cursor.execute('SELECT MAX("SaveId "), *  FROM SAVES ')
    tpl = cursor.fetchall()[0][2:]
print(tpl)
h = 1024 # 16 * 64 or 32 * 32 or 64 * 16
w = 768 # 16 * 48 or 32 * 24 or 64 * 12


'''атрибуты героя'''
x = h // 2
y = w // 2
Implant,Speed,Health,Humanizm,Coldown,harizm,Level,Exp,Point = tpl
print(Implant,Speed,Health,Humanizm,Coldown,harizm,Level,Exp,Point)

'''атрибуты врага'''
enemy_x = random.randint(0,800)
enemy_y = random.randint(0,700)
enemy_speed = 2.5
enemy_speed = 5

# attribute NPCs
npc_x = 300
npc_y = 200
