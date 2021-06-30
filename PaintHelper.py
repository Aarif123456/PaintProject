from random import randint

from pygame import *


def addImage(screen, imageSize, rect, location):
    screen.blit(transform.smoothscale(image.load(location), imageSize), rect)


def addImageNonSmooth(screen, imageSize, rect, location):
    screen.blit(transform.scale(image.load(location), imageSize), rect)


def createRandomColor():
    return randint(0, 255), randint(0, 255), randint(0, 255)
