from pygame import *
from random import*
#use for color highlighter and eraser    
screen = display.set_mode((1200,675))
screen.fill((255,255,255))
tool="clearpage"
size=50

canvasRect=Rect(300,100,700,500)
draw.rect(screen,(0,0,0),canvasRect,5)

brushRect=Rect(100,100,100,100)
draw.rect(screen,(255,0,0),brushRect)
def clearpage(col):
    draw.rect(screen,(col),canvasRect,0)
    
    
running =True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False        
    mb = mouse.get_pressed()    
    mx,my = mouse.get_pos()    
    if mb[0]==1 or mb[2]==1:
        screen.set_clip(canvasRect)
        if tool=="clearpage":
            if mb[0]==1:
                clearpage((255,255,255))
            if mb[2]==1:
                clearpage((randint(0,255),randint(0,255),randint(0,255)))
    
    display.flip()

quit()
