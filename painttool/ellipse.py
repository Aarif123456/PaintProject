from pygame import *
from random import*
from math import*
#use for color highlighter and eraser    
screen = display.set_mode((1200,675))
screen.fill((255,255,255))
tool="ellipse"
width=0
canvasRect=Rect(300,100,700,500)
draw.rect(screen,(0,0,0),canvasRect,5)
size=1
brushRect=Rect(100,100,100,100)
draw.rect(screen,(255,0,0),brushRect)
def ellipse(surface, col):
    screen.blit(surface,(0,0))
    if abs(mx-startx)>size*2 and abs(my-starty)> size*2:
        draw.ellipse(screen,col,(min(mx,startx),min(my,starty),abs(mx-startx),abs(my-starty)),size)
    else:
        draw.ellipse(screen,col,(min(mx,startx),min(my,starty),abs(mx-startx),abs(my-starty)),0)
copy=screen.copy()
running =True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN:
            if e.button==1: 
                copy = screen.copy()
                startx,starty = e.pos
            if e.button==3:#right click
                copy=screen.copy()
                startx,starty = e.pos
            if e.button == 4:
                size += 1
            if e.button == 5:
                if size != 1:
                    size -= 1
    mb = mouse.get_pressed()    
    mx,my = mouse.get_pos()
    
    if mb[0]==1 or mb[2]==1 and canvasRect.collidepoint(mx,my):
        screen.set_clip(canvasRect)
        if tool=="ellipse":
            if mb[0]==1:
                ellipse(copy,(0,0,0))
            if mb[2]==1:#or col=randint(0,255),randint(0,255),randint(0,255)
                ellipse(copy,(randint(0,255),randint(0,255),randint(0,255)))
                
    oldmx,oldmy=mx,my
    display.flip()

quit()
