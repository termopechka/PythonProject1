import pygame
import sqlite3
import random
h = 1024 # 16 * 64 or 32 * 32 or 64 * 16
w = 768 # 16 * 48 or 32 * 24 or 64 * 12


'''атрибуты героя'''
x = h // 2
y = w // 2
hero_speed = 10

'''атрибуты врага'''
enemy_x = random.randint(0,800)
enemy_y = random.randint(0,700)
enemy_speed = 5

# attribute NPCs
npc_x = 300
npc_y = 200
