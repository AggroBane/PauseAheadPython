import pygame
from enum import Enum


class TileType(Enum):
    BACKGROUND_TILE = -1
    BLOCK_TILE = 1
    SPIKE_TILE = 2


class TilePrototype:
    def __init__(self, tile_type: TileType, img, friction_coeff: int):
        self.img = img
        self.tile_type = tile_type
        self.friction_coeff = friction_coeff


class Tile(pygame.sprite.Sprite):
    TILE_WIDTH = 32

    def __init__(self, prototype: TilePrototype, x: int, y: int):
        self.prototype = prototype
        self.rect = self.prototype.img.get_rect()
        self.rect = pygame.Rect(x, y, Tile.TILE_WIDTH, Tile.TILE_WIDTH)

    def render(self, screen):
        screen.blit(self.prototype.img, (self.rect.x, self.rect.y))