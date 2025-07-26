import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        screen.fill('red')

        # Define polygon points (a triangle)
        polygon_points = [(100, 300), (300, 100), (500, 300)]

        # Draw a filled red polygon
        pygame.draw.polygon(screen, (0, 255, 0), polygon_points)

        pygame.display.flip()

        clock.tick(60)

pygame.quit()