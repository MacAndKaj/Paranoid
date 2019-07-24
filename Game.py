import pygame
from pygame.time import Clock
from pygame import key, event

from PyGameWrapper import PyGameWrapper
from Objects.Ball import Ball
from Objects.Desk import Desk


class Game:
    done = False
    ball = Ball()
    desk = Desk()
    pygameWrapper = PyGameWrapper()
    obstacles = []

    def run(self):
        while not self.done:
            for currentEvent in event.get():
                if currentEvent.type == pygame.QUIT:
                    self.done = True
            keys = key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                self.done = True

            self.pygameWrapper.resetScreen()
            self.desk.update(keys)
            self.ball.update(self.obstacles)
            self.pygameWrapper.updateScreen()
            Clock().tick(40)
