from pygame import *
from random import*
from math import*
screen = display.set_mode((1200,675))
screen.fill((255,255,255))
tool="circle"
width=0
canvasRect=Rect(300,100,700,500)
draw.rect(screen,(0,0,0),canvasRect,5)
size=1
brushRect=Rect(100,100,100,100)
draw.rect(screen,(255,0,0),brushRect)
def circle(surface, col):
    screen.blit(surface,(0,0))
    if (abs(mx-startx)+abs(my-starty))//2> size:
        draw.circle(screen,col,(startx,starty),((abs(mx-startx)+abs(my-starty))//2),size)
    else:
        draw.circle(screen,col,(startx,starty),((abs(mx-startx)+abs(my-starty))//2),0)
running =True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN:
            copy = screen.copy()
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
        if tool=="circle":
            if mb[0]==1:
                circle(copy,(0,0,0))
            if mb[2]==1:#or col=randint(0,255),randint(0,255),randint(0,255)
                circle(copy,(randint(0,255),randint(0,255),randint(0,255)),)
                
    oldmx,oldmy=mx,my
    display.flip()

quit()
