import pygame, os
from pytmx.util_pygame import load_pygame

class Objects:
    def __init__(self, x, y, image, image_tmx):
        self.x = x
        self.y = y
        self.image = image
        self.image_tmx = image_tmx

    def setup(self):
        map = load_pygame(os.path.join('image', 'back', 'untitled.tmx'))
        print(map)
        # for obj in map.get_layer_by_name('Object Layer 1'):

class Collision(pygame.sprite.Sprite):
    def __init__(self, pos, surface, group):
        super().__init__(group)
        self.image = surface
        self.rect = self.image.get_rect(center = pos)




# class Tile:
#     def __init__(self, name, image, is_solid):
#         self.name = name
#         self.image = pygame.image.load(image)
#         self.is_solid = is_solid
#
# class TileMap:
#     def __init__(self, map_file, tiles, tile_size):
#         self.tiles = tiles
#         self.tile_size = tile_size
#         self.map_file = map_file
#         self.tile_list = []
#
#     def read_csv(self, map_file):
#         map = []
#         with open(os.path.join(map_file)) as data:
#             data = csv.DictReader(data, delimiter=',')
#             for row in data:
#                 map.append(list(row))
#         return map
#
#     def draw(self, screen, map_file):
#         for y, row in enumerate (self.read_csv(map_file)):
#             for x, tile in enumerate(row):
#                 location = (x * self.tile_size, y * self.tile_size)
#                 image = self.tiles[self.tiles.index(tile)].image
#                 screen.blit(image, location)



# class TileMap():
#     def __init__(self, filename, spritesheet):
#         self.tile_size = 32
#         self.start_x, self.start_y = 0, 0
#         self.spritesheet = spritesheet
#        self.tiles = self.load_tiles(filename)
#        self.map_surface = pygame.Surface((self.map_w, self.map_h))
#        self.map_surface.set_colorkey((0, 0, 0))
#        self.load_map()

    # def draw_map(self, surface):
    #     surface.blit(self.map_surface, (self.start_x, self.start_y))
    #
    # def load_map(self):
    #     for tile in self.tiles:
    #         tile.draw(self.map_surface)

    # def read_csv(self, filename):
    #     map = []
    #     with open(os.path.join(filename)) as data:
    #         data = csv.DictReader(data, delimiter=',')
    #         for row in data:
    #             map.append(list(row))
    #     return map

    # def load_tiles(self, filename):
    #     tiles = []
    #     map = self.read_csv(filename)
    #     x, y = 0, 0
    #     for row in map:
    #         x = 0
    #         for tile in row:
    #             if tile == '0':
    #                 self.start_x, self.start_y = x * self.tile_size, y * self.tile_size
    #             elif tile == '184':
    #                 tiles.append(Tile('image/back/grey.png', x * self.tile_size, y * self.tile_size))
    #             elif tile == '2':
    #                 tiles.append(Tile('asphalt2.png', x * self.tile_size, y * self.tile_size))
    #                 # дальше загружать текстурки (32х32 файлы)
    #             x += 1
    #             #  ряд (не лезь, просто загрузи текстурки)
    #         y += 1
    #         # сохраняем размерчики для нашой мапы
    #     self.map_w, self.map_h = x * self.tile_size, y * self.tile_size
    #     # возвращаем 1749
    #     return tiles