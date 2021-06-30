from pygame import *
from random import randint

def addImage(screen, imageSize, rect, location):
    try:
        screen.blit(transform.smoothscale(image.load(location), imageSize),rect)
    except Exception as e:
        print("test")
    

def addImageNonSmooth(screen, imageSize, rect, location):
    screen.blit(transform.scale(image.load(location), imageSize),rect)

def createRandomColor():
    return (randint(0,255),randint(0,255),randint(0,255))

