from pygame import *
from random import*
#use for color highlighter and eraser    
screen = display.set_mode((1200,675))
screen.fill((255,255,255))
tool="brush"
size=200
canvasRect=Rect(300,100,700,500)
draw.rect(screen,(0,0,0),canvasRect,5)

brushRect=Rect(100,100,100,100)
draw.rect(screen,(255,0,0),brushRect)
def brush(surface, width):
    colorrect=Rect(mx-width//2,my-width//2,width,width)
    col=transform.average_color(screen,colorrect)
    draw.rect(surface,col,colorrect)
running =True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False        
    mb = mouse.get_pressed()    
    mx,my = mouse.get_pos()    

    if mb[0]==1 or mb[2]==1 :
        
        if tool=="brush":
            if mb[0]==1:
                brush(screen,200)
            if mb[2]==1:
                brush(screen,200)
    oldmx,oldmy=mx,my
    display.flip()

quit()

