from pygame import *
from random import*
#use for color highlighter and eraser    
screen = display.set_mode((1200,675))
screen.fill((255,255,255))
tool="eraser"
size=50

canvasRect=Rect(300,100,700,500)
draw.rect(screen,(0,0,0),canvasRect,1)

brushRect=Rect(100,100,100,100)
draw.rect(screen,(255,0,0),brushRect)

class brush:
    surface= screen
    col=255,255,255
    def circlebrush:
        draw.circle(surface,(col),(mx,my),size)
    def rectbrush:
        draw.rect(surface, (col),(mx,my,size,size),width)
    def linebrush:
        draw.line(surface,(col),(mx,my),(oldmx,oldmy))
    def explosionbrush:
        draw.line(surface,(col),(mx,my),(mx+randint(-size,size),my+randint(-size,size)))
    def polybrush:#fix up poly obvously
        draw.polygon(surface, (col),poly)
    screen.blit(surface,(0,0))

    pop
running =True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False        
    mb = mouse.get_pressed()    
    mx,my = mouse.get_pos()
    poly=[(mx,my), (mx+20,my+40), (mx+30,my+40)]

    if mb[0]==1 or mb[2]==1 and canvasRect.collidepoint(mx,my):
        screen.set_clip(canvasRect)
        if tool=="eraser":
            if mb[0]==1:
                brush.circlebrush(screen,(255,255,255))
            #if mb[2]==1:fill tool
                #brush(screen,5,(255,255,255))
    oldmx,oldmy=mx,my
    display.flip()

quit()
