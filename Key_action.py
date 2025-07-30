import pygame,sys

def controls(h):
    '''Обработка нажатий'''
    for event in pygame.event.get():

        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            return
    if not hasattr(h, 'real_x'):
        h.real_x = float(h.rect.x)
        h.real_y = float(h.rect.y)
    keys = pygame.key.get_pressed()

    dx = 0
    dy = 0
    if keys[pygame.K_a]: dx -= 1
    if keys[pygame.K_d]: dx += 1
    if keys[pygame.K_w]: dy -= 1
    if keys[pygame.K_s]: dy += 1


    if dx != 0 or dy != 0:
        length = (dx ** 2 + dy ** 2) ** 0.5
        if length > 0:
            dx = dx / length * h.speed
            dy = dy / length * h.speed

        h.real_x += dx
        h.real_y += dy

        h.rect.x = round(h.real_x)
        h.rect.y = round(h.real_y)