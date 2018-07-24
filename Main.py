import pygame
from pygame import key as Keyboard
from pygame import event as Event
from pygame.time import Clock

from Ball import Ball
from Desk import Desk
from Consts import *

pygame.init()
screen = pygame.display.set_mode((SIZEX, SIZEY))
pygame.display.set_caption("Moja gra", "Gra")
Done: bool = False
paranoid = Desk()
ball = Ball()
while not Done:
    for event in Event.get():
        if event.type == pygame.QUIT:
            Done = True
    keys = Keyboard.get_pressed()
    if keys[pygame.K_ESCAPE]:
        Done = True

    screen.fill((255, 255, 255))
    paranoid.update(keys)
    ball.update()
    pygame.display.flip()
    Clock().tick(40)

pygame.quit()
