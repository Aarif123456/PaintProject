# Abdullah ARif
# Brush that trails the mouse
from pygame import *
from random import*
from math import*

trials=[(0,0)]
cols=[Color(0,0,0)]
screen = display.set_mode((800,600)) 
drawcol=Color(0,0,0)
running =True
while running:                   
    for e in event.get():       
        if e.type == QUIT:      
            running = False        
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
    trials.append((mx,my))
    cols.append(Color(randint(0,255),randint(0,255),randint(0,255)))
    print(cols)
    """col.r=randint(0,255)
    col.g=randint(0,255)
    col.b=randint(0,255)"""

    for col in cols:
        if col.r!=drawcol.r:
            if col.r>drawcol.r:
                col.r-=1
            elif col.r<drawcol.r:
                col.r+=1                
        if col.g!=drawcol.g:
            if col.g>drawcol.g:
                col.g-=1
            elif col.g<drawcol.g:
                col.g+=1               
        if col.b!=drawcol.b:
            if col.b>drawcol.b:
                col.b-=1
            elif col.g<drawcol.g:
                col.b+=1  

        draw.circle(screen,col,trials[-1],10)
        
        
     


    display.flip() 


quit()
""" if mb[2]==1:
        trials[2]=randint(0,255)
        trials[3]=randint(0,255)
        trials[4]=randint(0,255)"""
""" if I wanna to get clear screen
            screen.fill((0,0,0))
            trials=[]"""
       
