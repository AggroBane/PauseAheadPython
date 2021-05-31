import pygame
import abc
from game.loading import SpriteSheet
from .scene import Scene


class GameState(abc.ABC):
    @abc.abstractmethod
    def update(self):
        pass

    @abc.abstractmethod
    def render(self):
        pass


class PlayingState(GameState):
    def __init__(self, screen):
        self.screen = screen
        self.spritesheet: SpriteSheet = SpriteSheet("C:\\Users\\willi\\Desktop\\Workspace\\python\\pause-ahead\\res"
                                                    "\\spritesheet.png", 32, 32)
        self.scene: Scene = self.load_scene(1)

    def load_scene(self, scene_num: int) -> Scene:
        return Scene(scene_num, self.spritesheet, self.screen)

    def update(self):
        if self.scene is not None:
            self.scene.update()

    def render(self):
        if self.scene is not None:
            self.scene.render()


class MenuState(GameState):
    def __init__(self, screen):
        self.screen = screen

    def update(self):
        pass

    def render(self):
        pass


class Game:
    WIDTH: int = 1280
    HEIGHT: int = 720
    GAME_NAME = "Pause ahead - Python version"
    PLAYING_STATE: PlayingState = None
    MENU_STATE: MenuState = None

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((Game.WIDTH, Game.HEIGHT))
        pygame.display.set_caption(Game.GAME_NAME)

        self.background: pygame.Surface = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0, 0, 0))

        Game.PLAYING_STATE = PlayingState(self.screen)
        Game.MENU_STATE = MenuState(self.screen)

        self.state: GameState = Game.PLAYING_STATE

    def update(self):
        self.state.update()

    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.state.render()
        pygame.display.flip()
