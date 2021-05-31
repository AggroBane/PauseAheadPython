import os
import sys
import pygame


def load_img(name):
    """ Load image and return image object"""
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error as message:
        print('Cannot load image: ', fullname)
        raise SystemExit(message)

    return image


class SpriteSheet:
    def __init__(self, filename: str, tile_width: int, tile_height: int):
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.sheet = load_img(filename)

    def image_at(self, pos_x, pos_y, color_key = None):
        rect = pygame.Rect(pos_x * self.tile_width, pos_y * self.tile_height, self.tile_width, self.tile_height)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)

        if color_key is not None:
            if color_key == -1:
                color_key = image.get_at((0, 0))

            image.set_colorkey(color_key, pygame.RLEACCEL)

        return image
