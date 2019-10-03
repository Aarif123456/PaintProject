from pygame import *
from random import*   
screen = display.set_mode((1200,675))
screen.fill((255,255,255))
tool="pencil"
canvasRect=Rect(300,100,700,500)
draw.rect(screen,(0,0,0),canvasRect,5)
pencilRect=Rect(100,100,100,100)
draw.rect(screen,(255,0,0),pencilRect)
def pencil(col):
    mx,my=mouse.get_pos()
    draw.line(screen,(col),(oldmx,oldmy),(mx,my),3)
running =True
while running:                       
    for e in event.get():       
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN:
           if e.button == 4:
               size += 1
           if e.button == 5:
               if size!=1:               
                   size -= 1 
    mb = mouse.get_pressed()    
    mx,my = mouse.get_pos()
    if mb[0]==1 or mb[2]==1 and canvasRect.collidepoint(mx,my):
        screen.set_clip(canvasRect)
        if tool=="pencil":
            if mb[0]==1:
                pencil((255,0,0))
            if mb[2]==1:
                pencil((randint(0,255),randint(0,255),randint(0,255)))             
    oldmx,oldmy,=mx,my
    display.flip()

quit()
