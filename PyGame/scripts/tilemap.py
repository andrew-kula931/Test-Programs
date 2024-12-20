import pygame

TILE_OFFSET = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (-1, 1), (0, 1), (1, 1)]
PHYSICS_TILES = {'ground'}

class Tilemap:
    def __init__(self, game, tile_size=32):
        self.game = game
        self.tile_size = tile_size
        self.tilemap = {}
        self.offgrid_tiles = []

        for i in range(30):
            #This one is for creating a horizontal line
            self.tilemap[str(3 + (i)) + ';15'] = {'type': 'ground', 'variant': 0, 'pos': (3 + (i), 15)}

            #And this one is for a vertical line
            self.tilemap['10;' + str(5 + i)] = {'type': 'ground', 'variant': 0, 'pos': (10, 5 + i)}

    def tiles_around(self, pos):
        tiles = []
        tile_loc = (int(pos[0] // self.tile_size), int(pos[1] // self.tile_size))
        for offset in TILE_OFFSET:
            check_loc = str(tile_loc[0] + offset[0]) + ';' + str(tile_loc[1] + offset[1])
            if check_loc in self.tilemap:
                tiles.append(self.tilemap[check_loc])
        return tiles

    def physics_rects_around(self, pos):
        rects = []
        for tile in self.tiles_around(pos):
            if tile['type'] in PHYSICS_TILES:
                rects.append(pygame.Rect(tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size, self.tile_size, self.tile_size))
        return rects

    def render(self, surf):
        for tile in self.offgrid_tiles:
            surf.blit(self.game.assets[tile['type']][tile['variant']], tile['pos'])

        for loc in self.tilemap:
            tile = self.tilemap[loc]
            surf.blit(self.game.assets[tile['type']][tile['variant']], (tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size))

