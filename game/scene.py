from game.loading import SpriteSheet
from enum import Enum
import os
from game.tile import Tile, TileType, TilePrototype

class Scene:
    TILES_IN_SCREEN = 20

    def __init__(self, scene_num: int, spritesheet: SpriteSheet, screen):
        self.screen = screen
        self.spritesheet = spritesheet

        # TODO: Maybe load images and prototypes in game instead? Because scene is loaded at each level, and tile always are the same

        # Loading all images only one time
        self.all_tile_img = [
            self.spritesheet.image_at(0, 0),
            self.spritesheet.image_at(1, 0),
            self.spritesheet.image_at(2, 0),
        ]

        # Load all tile prototype (Index correspond to the number in the csv scene file)
        self.all_tile_prototypes = [
            TilePrototype(TileType.BLOCK_TILE, self.all_tile_img[0], 1), # Ground
            TilePrototype(TileType.BLOCK_TILE, self.all_tile_img[1], 1), # Brick
            TilePrototype(TileType.SPIKE_TILE, self.all_tile_img[2], 0)  # Spike
        ]

        # Reading csv file for this scene
        f = open('game/levels/level' + str(scene_num) + '.csv', 'r')
        self.all_tiles = []
        i = 0
        for line in f:
            cur_row = []
            j = 0
            for prototype_num in line.split(','):
                # Check that its not -1 (-1 means empty)
                if int(prototype_num) != -1:
                    cur_prototype: TilePrototype = self.all_tile_prototypes[int(prototype_num)]
                    cur_tile: Tile = Tile(cur_prototype, j * Tile.TILE_WIDTH, i * Tile.TILE_WIDTH)
                    cur_row.append(cur_tile)
                j += 1
            i += 1

            self.all_tiles.append(cur_row)

    def render(self):
        for cols in self.all_tiles:
            for tile in cols:
                tile.render(self.screen)

    def update(self):
        pass
