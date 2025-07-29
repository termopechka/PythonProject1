import pygame
import Hero
pygame.init()




clock = pygame.time.Clock()
SETING = 1
h = 1200
w = 800

x = h // 2
y = w // 2

hero_speed = 50

music = pygame.mixer.music.load('music/Cyberpunk_2077_-_Johnny_Silverhand_s_Theme_Cello_Version_(SkySound.cc).mp3')
pygame.mixer.music.play(-10)


screen = pygame.display.set_mode((h,w))
pygame.display.set_caption('Live solo')


keys = pygame.key.get_pressed()
icon = pygame.image.load('image/assets_task_01k1476qdmfjsr95yxtwsdf192_1753562211_img_1.PNG')
pygame.display.set_icon(icon)


hero = Hero(x, y, hero_speed)
# hero = pygame.image.load('image/hero_img/Layer 1_hero_1.png')
# hero_shoots = [
#     pygame.image.load('image/hero_img/Layer 1_sprite_1.png'),
#     pygame.image.load('image/hero_img/Layer 1_sprite_2.png'),
#     pygame.image.load('image/hero_img/Layer 1_sprite_3.png'),
# ]
# hero = pygame.transform.scale(hero, (70, 70))
# hero.set_colorkey((255, 255, 255))

running = True
while running:

    screen.fill((100, 0, 0))
    screen.blit(hero.image, (hero.rect.x, hero.rect.y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
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
    clock.tick(60)
pygame.quit()