from pygame import *
from random import*   
screen = display.set_mode((1200,675))
screen.fill((255,255,255))
tool="pencil"
canvasRect=Rect(300,100,700,500)
draw.rect(screen,(0,0,0),canvasRect,5)
pencilRect=Rect(100,100,100,100)
draw.rect(screen,(255,0,0),pencilRect)
def fill(col):
    fillpos=[(mx,my)]
    oldcol=screen.get_at((mx,my))
    if oldcol!=col:
        while len(fillpos)>0:
            while len(fillpos)>0:
                x,y = fillpos.pop()
                if screen.get_at((x,y))==oldcol:
                    screen.set_at((x,y),col)
                    fillpos+=[(x+1,y), (x-1,y),(x,y+1),(x,y-1)]
                    
                 
            
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
                fill((255,0,0))
            if mb[2]==1:
                fill((255,255,255))             
    oldmx,oldmy,=mx,my
    display.flip()

quit()
