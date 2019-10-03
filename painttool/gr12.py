
#Abdullah
from pygame import *
from random import*
from math import*

trials=[]
cols=[0,0,0]
screen = display.set_mode((800,600)) 
drawcol=[0,0,0]
running =True
while running:                   
    for e in event.get():       
        if e.type == QUIT:      
            running = False        
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
    if mb[0]==1:
        trials.append(mx,my)
        cols.append([randint(0,255),randint(0,255),randint(0,255)])
        print(cols)
        '''col[0]=randint(0,255)
        col[1]=randint(0,255)
        col[2]=randint(0,255)'''

    for col in cols:
        if col[0]!=drawcol[0]:
            if col[0]>drawcol[0]:
                col[0]-=1
            elif col[0]<drawcol[0]:
                col[0]+=1                
        if col[1]!=drawcol[1]:
            if col[1]>drawcol[1]:
                col[1]-=1
            elif col[1]<drawcol[1]:
                col[1]+=1               
        if col[2]!=drawcol[2]:
            if col[2]>drawcol[2]:
                col[2]-=1
            elif col[1]<drawcol[1]:
                col[2]+=1  

        draw.circle(screen,(col[0],col[1],col[2]),trials,10)
        
   
     


    display.flip() 


quit()
''' if mb[2]==1:
        trials[2]=randint(0,255)
        trials[3]=randint(0,255)
        trials[4]=randint(0,255)'''
""" if I wanna to get clear screen
            screen.fill((0,0,0))
            trials=[]"""
       
