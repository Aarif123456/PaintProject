# Abdullah Arif
# Trail brush that fades

from pygame import *
from random import*
from math import*

trials=[]
col=[0,0,0,0,0]
drawcol=[200,230,30]
screen = display.set_mode((800,600)) 

running =True
while running:                   
    for e in event.get():       
        if e.type == QUIT:      
            running = False        
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
    if mb[0]==1:
        trials.append([mx,my,randint(0,255),randint(0,255),randint(0,255)]) 
    for col in trials:
        if  col[2]!=drawcol[0]:
            if col[2]>drawcol[0]:
                col[2]-=1
            if col[2]<drawcol[0]:
                col[2]+=1            
        if col[3]!=drawcol[1]:
            if  col[3]!=drawcol[1]:
                if col[3]>drawcol[1]:
                    col[3]-=1
                if col[3]<drawcol[1]:
                    col[3]+=1
        if col[4]!=drawcol[2]:
            if  col[4]!=drawcol[2]:
                if col[4]>drawcol[2]:
                    col[4]-=1
                if col[4]<drawcol[2]:
                    col[4]+=1

        draw.circle(screen,(col[2],col[3],col[4]),col[:2],10)
    if mb[2]==1:
        drawcol=[randint(0,255),randint(0,255),randint(0,255)]        
        trials=[]
     


    display.flip() 


quit()

