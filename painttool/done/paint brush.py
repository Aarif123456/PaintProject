#Abdullah Arif
from pygame import *
from random import*
from math import*
drawingColor=(0,0,0)
tool="pencil"
#setup
screen = display.set_mode((1024,720)) 
screen.fill((255,255,255))
running =True
while running:                   
    for e in event.get():       
        if e.type == QUIT:     
            running = False     
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
    draw.line(screen,(randint(0,255),randint(0,255),randint(0,255)),(mx,my),(randint(40,640),randint(80,580)),2)
