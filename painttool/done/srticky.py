'''
graphicsT.py
Mr. McKenzie
This is a template that you can use for your simple graphics programs.
'''
from pygame import *
from random import *
    
screen = display.set_mode((1200,900))  # change 800,600 to any size you like
c=0
cols = [(randint(0,255),randint(0,255),randint(0,255)) for i in range(100)]
for i in range(100):
    draw.rect(screen,cols[i],(i*12,2,11,11))
    draw.rect(screen,(255,0,0),(c*12,13,11,11))
running =True
while running:                   
    for e in event.get():       # This is called the event loop. It allows you to respond to
        if e.type == QUIT:      
            running = False     
        if e.type == KEYDOWN and e.key == K_SPACE:
            cols = [(randint(0,255),randint(0,255),randint(0,255)) for i in range(100)]
        if e.type == MOUSEBUTTONDOWN:
            if e.button == 4:
                c = (c+1)%100
            if e.button == 5:
                c = (c+99)%100
    draw.rect(screen,(0,0,0),(0,0,1200,24))
    for i in range(100):
        draw.rect(screen,cols[i],(i*12,2,11,11))
        draw.rect(screen,(255,0,0),(c*12,13,11,11))


    mx,my = mouse.get_pos()
    mb = mouse.get_pressed()
    mx-=mx%100
    my-=my%100
    if mb[0]==1:
        draw.circle(screen, cols[c], (mx,my), 20)
    if mb[1]==1:
        image.save(screen,"awesomePic.jpg")
    if mb[2]==1:
        for x in range(mx-20,mx+21,10):
            for y in range(my-20,my+21,10):
                draw.circle(screen, (0,0,0), (x,y), 4)


    display.flip()  


quit()
