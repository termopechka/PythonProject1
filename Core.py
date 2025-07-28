import pygame

pygame.init()


running = True
h = 1200
w = 800
screen = pygame.display.set_mode((h,w))
pygame.display.set_caption('Live solo')



icon = pygame.image.load('image/assets_task_01k1476qdmfjsr95yxtwsdf192_1753562211_img_1.JPG')
pygame.display.set_icon(icon)
hero = pygame.image.load('image/hero_img/Layer 1_sprite_1.png')
hero = pygame.transform.scale(hero, (70, 70))
hero.set_colorkey((255, 255, 255))
x = h // 2
y = w // 2
while running:

    screen.fill((100, 0, 0))
    screen.blit(hero, (x, y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                x -= 50
            elif event.key == pygame.K_d:
                x += 50
            elif event.key == pygame.K_w:
                y -= 50
            elif event.key == pygame.K_s:
                y += 50

            elif event.key == pygame.K_ESCAPE:
                running = False
    pygame.display.flip()

pygame.quit()