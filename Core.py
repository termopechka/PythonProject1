import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Live solo')


try:
    icon = pygame.image.load('image/assets_task_01k1476qdmfjsr95yxtwsdf192_1753562211_img_1.JPG')
    pygame.display.set_icon(icon)
except:
    print("Ошибка загрузки иконки! Проверьте путь к файлу")

running = True
while running:
    screen.fill((66,135,245))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()