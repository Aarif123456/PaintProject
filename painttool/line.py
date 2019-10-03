from pygame import *
from random import*
#use for color highlighter and eraser    
screen = display.set_mode((1200,675))
screen.fill((255,255,255))
tool="line"
start = 0,0
size = 1

canvasRect=Rect(300,100,700,500)
draw.rect(screen,(0,0,0),canvasRect,5)

brushRect=Rect(100,100,100,100)
draw.rect(screen,(255,0,0),brushRect)
def line(surface,col):
    screen.blit(surface,(0,0))
    draw.line(screen,(col),start,(mx,my), size)  
running =True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN:
            if e.button ==1 or e.button ==2:
                copy = screen.copy()
                start = e.pos
            if e.button == 4:
                size += 1
            if e.button == 5:
                if size != 1:
                    size -= 1
    mb = mouse.get_pressed()    
    mx,my = mouse.get_pos()    
    if mb[0]==1 or mb[2]==1 and canvasRect.collidepoint(mx,my):
        screen.set_clip(canvasRect)
        if tool=="line":
            if mb[0]==1:
                line(copy,(0,0,0))
            if mb[2]==1:#or col=randint(0,255),randint(0,255),randint(0,255)
                line(copy,(randint(0,255),randint(0,255),randint(0,255)))
                
    
    display.flip()

quit()
