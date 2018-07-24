from pygame import Rect, display, draw
from pygame.constants import *
from Consts import *
from math import cos, sin


class Ball(object):
    position = [int(0.5 * SIZEX), int(0.7 * SIZEY)]
    prevposition = [int(0.5 * SIZEX), int(0.7 * SIZEY)]
    radius = 10
    step = 10
    direction = 30  # degrees

    def __init__(self) -> None:
        self.Rectangle = Rect(self.position, (self.radius, self.radius))

    def __setPosition(self):
        self.position[0] += int(self.step * cos(self.direction))
        self.position[1] -= int(self.step * sin(self.direction))

    def __borders(self):
        print(self.position)
        if self.position[0] == SIZEX - self.radius or self.position[0] == self.radius:
            print(self.direction,'SIZEX')
            self.direction *= (-1)
        elif self.position[1] == SIZEY - self.radius or self.position[1] == self.radius:
            print(self.direction,'SIZEY')
            self.direction = 90 - (-1*self.direction)

    def __handleDirection(self):
        if SIZEX - self.radius > self.position[0] > self.radius and \
                SIZEY - self.radius > self.position[1] > self.radius:
            self.__setPosition()
        else:
            self.__borders()
            self.__setPosition()

    def update(self):
        self.__handleDirection()
        draw.circle(display.get_surface(), (0, 0, 0), self.position, self.radius)
