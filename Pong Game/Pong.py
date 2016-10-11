import pygame, sys
from pygame.locals import *


pygame.init()

yDirection = 1
xDirection = -1


xPos = 400
yPos = 0
WIDTH = 800
HEIGHT = 600

window = pygame.display.set_mode((WIDTH, HEIGHT),0,32)
BLACK= (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

ball = Rect(xPos,yPos,30,30)

while True:
    ball.centerx = xPos
    ball.centery = yPos
    window.fill(BLACK)

    if yDirection == 1:
        yPos = yPos +0.2
    elif yDirection == -1:
        yPos = yPos - 0.2

    if xDirection == 1:
        xPos = xPos +0.2
    elif xDirection == -1:
        xPos = xPos - 0.2


    if yPos>=600:
        yDirection = -1
    if yPos<= 0:
        yDirection = 1
    if xPos >= 800:
        xDirection = -1
    if xPos <= 0:
        xDirection =1



    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.exit()
            sys.exit()


    pygame.draw.rect(window,WHITE,ball)
    pygame.display.update()