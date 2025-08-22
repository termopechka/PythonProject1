import sqlite3

with sqlite3.connect('data_base/Db1.sqlite3') as db:
    cursor = db.cursor()

    cursor.execute('SELECT MAX("SaveId "), *  FROM SAVES ')
    tpl = cursor.fetchall()[0][2:]
h = 1024 # 16 * 64 or 32 * 32 or 64 * 16
w = 768 # 16 * 48 or 32 * 24 or 64 * 12


'''атрибуты героя'''
x = h // 2
y = w // 2
Implant = tpl[0]
Speed,Health,Humanizm,Coldown,harizm,Level,Exp,Point = tpl[1:]

'''атрибуты врага'''
enemy_count = 10

enemy_speed = 3

# attribute NPCs
npc_x = 300
npc_y = 200
