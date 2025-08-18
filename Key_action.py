import pygame,sys

from Hero import Bullet


def controls(h, bullet_group,menu,):
    '''Управление персонажем и обработка событий
    :param h: объект персонажа
    :param bullet_group: группа пуль
    :param menu: объект меню'''

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


    # move
    if not hasattr(h, 'real_x'):
        h.real_x = float(h.rect.x)
        h.real_y = float(h.rect.y)


    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pressed()
    dx = 0
    dy = 0
    if keys[pygame.K_ESCAPE]:
            menu.view = True

    if keys[pygame.K_e] :
        h.dilog = True

    if keys[pygame.K_a] and h.rect.x > 0 : dx -= 1
    h.status = 'move'
    if keys[pygame.K_d]  and h.rect.x < 850 : dx += 1
    h.status = 'move'
    if keys[pygame.K_w] and h.rect.y > 0 : dy -= 1
    h.status = 'move'
    if keys[pygame.K_s] and h.rect.y < 700 : dy += 1
    h.status = 'move'
    if keys[pygame.K_LSHIFT]: h.speed = h.sprint
    else:h.speed = h.sprint // 2
    if dx != 0 or dy != 0:
        length = (dx ** 2 + dy ** 2) ** 0.5
        if length > 0:
            dx = dx / length * h.speed
            dy = dy / length * h.speed

        h.real_x += dx
        h.real_y += dy

        h.rect.x = round(h.real_x)
        h.rect.y = round(h.real_y)
    
    if dx != 0 or dy != 0:
        h.status = 'move'
    else:
        h.status = 'stand'

    if mouse[0] and not h.shoot:
        h.status = 'shoot'
        start_pos = h.rect.center
        target_pos = pygame.mouse.get_pos()
        bullet = Bullet(start_pos, target_pos, h.get_rotation_angle())
        bullet_group.add(bullet)
        h.shoot_time = pygame.time.get_ticks()
        h.shoot = True



def custom_group_draw(group, screen):
    '''Отрисовка группы спрайтов на экране
    group - группа спрайтов, screen - экран для отрисовки'''
    for sprite in group:
        sprite.draw(screen)
