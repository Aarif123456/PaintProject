from pygame import *
#use for color highlighter and eraser
polylist=[]
screen = display.set_mode((1200,675))
screen.fill((255,90,90))
tool='polygon'
canvasRect=Rect(300,100,700,500)
draw.rect(screen,(0,0,0),canvasRect,5)
size=50
def polygon(polylist):    
    draw.polygon(screen,(0,0,0),polylist)    
    
screencopy = screen.copy()
running =True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type==MOUSEBUTTONDOWN:
            if e.button ==3:
                polygon(polylist)            
                polylist=[]
    mb = mouse.get_pressed()    
    mx,my = mouse.get_pos()  
    if mb[0]==1:
        if tool!='polygon':
            polylist=[]
        if tool=='polygon':
            polylist.append((mx,my))
    
        
    display.flip()

quit()
