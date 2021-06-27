#Abdulllah
#explosion brush
from pygame import*
from random import*
size=20    
screen = display.set_mode((800,600))  # change 800,600 to any size you like
def lines(col,x,y,steps):
        if steps>0:
            x2=randint(-20,20)+x
            y2=randint(-20,20)+y
            for i in range(randint(1,3)):
                x2=x+randint(-size,size)
                y2=y+randint(-size,size)
                draw.line(screen,col,(x,y),(x2,y2))
running =True
while running:                   
    for e in event.get():       # This is called the event loop. It allows you to respond to
        if e.type == QUIT:      # things that happen as distict events. e.g. clicking a mouse button
            running = False     # or key on the keyboard rather than holding either one down.
                                # Without this your pygame window will lag/freeze. This one also
                                # allows the user to click on the x at top right to exit.

    # -------- Your code goes between these two line -------------------------    
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
    if mb[0]==1:
        col=randint(0,255),randint(0,255),randint(0,255)
        lines(col,mx,my,50)
    elif mb[2]==1:
        screen.fill((0,0,0))
    
                                     
    # ------------------------------------------------------------------------ 
    display.flip()  # all drawing happens to memory, this copies it to the screen


quit()

