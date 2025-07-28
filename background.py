import pygame

# tiles
ASPHALT = 0

class Tower:
    def __init__(self):
        self.sprite = pygame.transform.scale(pygame.image.load('assets/sprites/tower/tower.png'),(125,125))
        self.x = 200
        self.y = 150

textures = {
    ASPHALT: pygame.image.load('image/asphalt.png'),
}

# config
tilesize = 50
mapwidth = 20
mapheight = 10

