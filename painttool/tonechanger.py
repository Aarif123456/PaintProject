from pygame import *
#use for color highlighter and eraser

screen = display.set_mode((1200,675))
screen.fill((255,90,90))
tool="text"
canvasRect=Rect(300,100,700,500)
draw.rect(screen,(0,0,0),canvasRect,5)
size=50
def tonechanger():
    tcol=screen.get_at((mx,my))
    if min(tcol)>10:
        ncol=(tcol[0]-1,tcol[1]-1,tcol[2]-1)    
        time.wait(15)        
        draw.circle(screen,ncol,(mx-size//2,my-size//2),size)
screencopy = screen.copy()
running =True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
      
    mb = mouse.get_pressed()    
    mx,my = mouse.get_pos()  
    if mb[0]==1:          
        tonechanger()            
        
    display.flip()

quit()
