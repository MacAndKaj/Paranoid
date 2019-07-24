from pygame import Rect, display, draw
from Consts import *
from math import cos, sin, radians


class Ball(object):
    position = [int(0.5 * SCREEN_WIDTH), int(0.7 * SCREEN_HEIGHT)]
    radius = 10
    step = 10
    angleOfDirection = -45  # degrees

    def __init__(self) -> None:
        self.Rectangle = Rect(self.position, (self.radius, self.radius))

    def __setPosition(self):
        self.position[0] += int(self.step * cos(radians(self.angleOfDirection)))
        self.position[1] += int(self.step * sin(radians(self.angleOfDirection)))

    def __borders(self):
        if self.position[0] >= SCREEN_WIDTH - self.radius:
            self.angleOfDirection = STRAIGHT_ANGLE - self.angleOfDirection
        elif self.position[0] <= self.radius:
            self.angleOfDirection = STRAIGHT_ANGLE - self.angleOfDirection
        elif self.position[1] >= SCREEN_HEIGHT - self.radius:
            self.angleOfDirection = -self.angleOfDirection
        elif self.position[1] <= self.radius:
            self.angleOfDirection = -self.angleOfDirection

    def __handleDirection(self,obstacles):
        if SCREEN_WIDTH - self.radius > self.position[0] > self.radius and \
                SCREEN_HEIGHT - self.radius > self.position[1] > self.radius:
            self.__setPosition()
        else:
            self.__borders()
            self.__setPosition()

    def update(self,obstacles):
        self.__handleDirection(obstacles)
        draw.circle(display.get_surface(), (0, 0, 0), self.position, self.radius)
