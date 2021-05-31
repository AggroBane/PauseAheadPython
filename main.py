try:
    import sys
    import random
    import math
    import os
    import abc
    import pygame
    from pygame.locals import *
except ImportError as err:
    print("Couldn't load necessary modules.")
    sys.exit(2)

from game.game import Game


def main():
    clock: pygame.time.Clock = pygame.time.Clock()

    game: Game = Game()

    # Event loop
    while 1:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                return

        game.update()
        game.render()


if __name__ == '__main__':
    main()
