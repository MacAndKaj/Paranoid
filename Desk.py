from pygame import Rect, display, draw
from pygame.constants import *
from Consts import *

class Desk(object):
    direction = dict(RIGHT=False, LEFT=False)
    position = [int(0.5*SIZEX-50), int(0.8*SIZEY)]
    size = (100, 20)

    def __init__(self) -> None:
        self.Rectangle = Rect(self.position, self.size)

    def __resetDir(self):

        self.direction['LEFT'] = False
        self.direction['RIGHT'] = False

    def __handleDirection(self):
        if self.direction['LEFT'] and not self.direction['RIGHT']:
            if not self.position[0] < 0:
                self.position[0] -= 10
        if self.direction['RIGHT'] and not self.direction['LEFT']:
            if not self.position[0] > SIZEX-self.size[0]:
                self.position[0] += 10

    def __setDir(self, keys: dict):
        if keys[K_LEFT] or keys[K_a]:
            self.direction['LEFT'] = True
        if keys[K_RIGHT] or keys[K_d]:
            self.direction['RIGHT'] = True

    def update(self, keys):
        self.__setDir(keys)
        self.__handleDirection()
        self.__resetDir()
        self.Rectangle.x = self.position[0]
        self.Rectangle.y = self.position[1]
        draw.rect(display.get_surface(), (255, 0, 0), self.Rectangle)
        draw.circle(display.get_surface(), (255, 0, 0),
                    (self.position[0],self.position[1]+int(self.size[1]/2)),int(self.size[1]/2))
        draw.circle(display.get_surface(), (255, 0, 0),
                    (self.position[0]+self.size[0], self.position[1] + int(self.size[1] / 2)), int(self.size[1] / 2))
