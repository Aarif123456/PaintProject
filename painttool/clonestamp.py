from pygame import *
from random import*   
screen = display.set_mode((1200,675))
screen.fill((255,255,255))
tool="pencil"
canvasRect=Rect(300,100,700,500)
draw.rect(screen,(0,0,0),canvasRect,5)
pencilRect=Rect(100,100,100,100)
draw.rect(screen,(255,0,0),pencilRect)
def clonestamp (cdx,cdy,sx,sy,size):    
    difx,dify=mx-sx,my-sy
    if min(cdx+difx,cdy+dify)>0:
        clonedrect=Rect(cdx+difx,cdy+dify,size,size)
        cloned=screen.subsurface(clonedrect).copy()
        cloned.convert()
        screen.blit(cloned,(mx,my))
size=10
running = True
first = False #save original position of mouse to track clone
saved = False # track if clone has been initiated 
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
    if tool=="pencil":
        if mb[0]==1:
            if first==True:
                sx,sy=mx,my
                first=False
            if saved:
                clonestamp(cspdx,cspdy,sx,sy,size)            
        if mb[2]==1:
            cspdx,cspdy=mx,my
            first=True
            saved = True
            
              
                
                           
    oldmx,oldmy,=mx,my
    display.flip()

quit()
