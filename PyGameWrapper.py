import pygame
from Consts import *

class PyGameWrapper(object):

    def __init__(self) -> None:
        super().__init__()
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("PARANOID", "PARANOID")

    def resetScreen(self):
        self.screen.fill((255, 255, 255))

    def updateScreen(self):
        pygame.display.flip()




