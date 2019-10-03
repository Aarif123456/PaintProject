#populatio tool
from pygame import *
from random import*   
screen = display.set_mode((1200,675))
screen.fill((255,255,255))
tool="spray"
canvasRect=Rect(300,100,700,500)
draw.rect(screen,(0,0,0),canvasRect,5)
radius=50
size=10
def spray(size,speed,radius,spraydesign,sprayshape,col):#reorganize later
    for i in range (speed):
        x=mx+randint(-radius,radius)
        y=my+randint(-radius,radius)
        if spraydesign ==1:
            if ((x-mx)**2+(y-my)**2)<radius**2:#equation of circle
                if sprayshape==1:
                    draw.circle(screen,col,(x,y),size)
                elif sprayshape==2:
                    draw.rect(screen,col,(x,y,size,size))
                else:
                    draw.line(screen,(col),(x,y),(x+randint(-3,3),y+randint(-3,3)), size) 
        elif spraydesign ==2:
            if sprayshape==1:
                draw.circle(screen,col,(x,y),size)
            elif sprayshape==2:
                draw.rect(screen,col,(x,y,size,size))                    
            else:
                draw.line(screen,(col),(x,y),(x+randint(-3,3),y+randint(-3,3)), size) 
            
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
        if tool=="spray":
            if mb[0]==1:
                spray(size,10,radius,1,3,(255,0,0,))
            if mb[2]==1:
                spray(size,10,radius,1,1,(randint(0,255),randint(0,255),randint(0,255),))            
    oldmx,oldmy,=mx,my
    display.flip()

quit()
