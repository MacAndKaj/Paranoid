from pygame import Rect, display, draw
from pygame.constants import *
from Consts import *
from math import cos, sin, radians


class Ball(object):
    position = [int(0.5 * SIZEX), int(0.7 * SIZEY)]
    prevposition = [int(0.5 * SIZEX), int(0.7 * SIZEY)]
    radius = 10
    step = 10
    direction = -20  # degrees

    def __init__(self) -> None:
        self.Rectangle = Rect(self.position, (self.radius, self.radius))

    def __setPosition(self):
        self.position[0] += int(self.step * cos(radians(self.direction)))
        self.position[1] += int(self.step * sin(radians(self.direction)))

    def __borders(self):
        if self.position[0] >= SIZEX - self.radius:
            self.direction = 180-self.direction
        elif self.position[0] <= self.radius:
            self.direction = 180-self.direction
        elif self.position[1] >= SIZEY - self.radius:
            print(self.direction, '3')
            self.direction = (0-self.direction)
        elif self.position[1] <= self.radius:
            print(self.direction, '4')
            self.direction = (0-self.direction)

    def __handleDirection(self,obstacles):
        if SIZEX - self.radius > self.position[0] > self.radius and \
                SIZEY - self.radius > self.position[1] > self.radius:
            self.__setPosition()
        else:
            self.__borders()
            self.__setPosition()

    def update(self,obstacles):
        self.__handleDirection(obstacles)
        draw.circle(display.get_surface(), (0, 0, 0), self.position, self.radius)
