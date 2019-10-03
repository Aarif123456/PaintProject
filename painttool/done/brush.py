from pygame import *
from random import*
#use for color highlighter and eraser    
screen = display.set_mode((1200,675))
screen.fill((255,255,255))
tool="brush"
size=20
cover = Surface((1200,675)).convert()#make blank Surface
cover.set_alpha(55)
cover.set_colorkey((255,255,255))
canvasRect=Rect(300,100,700,500)
draw.rect(screen,(0,0,0),canvasRect,5)

brushRect=Rect(100,100,100,100)
draw.rect(screen,(255,0,0),brushRect)
screencopy = screen.copy()
cover.fill((255,255,255))
class brush:    
    def circlebrush(surface,col,width):
        draw.circle(surface,(col),(mx,my),size)
    def rectbrush(surface,col,width):
        draw.rect(surface, (col),(mx,my,size,size),width)
    def linebrush(surface,col,width):
        draw.line(surface,(col),(mx,my),(oldmx,oldmy))
    def explosionbrush(surface,col,width):
        draw.line(surface,(col),(mx,my),(mx+randint(-size,size),my+randint(-size,size)))
class highlighter:    
    def circlebrush(surface,col,width):#surface is cover[pagecanvasnum]        
        draw.circle(surface,(col),(mx,my),size)
    def rectbrush(surface,col,width):
        draw.rect(surface, (col),(mx,my,size,size),width)
    def linebrush(surface,col,width):
        draw.line(surface,(col),(mx,my),(oldmx,oldmy))
    def explosionbrush(surface,col,width):
        draw.line(surface,(col),(mx,my),(mx+randint(-size,size),my+randint(-size,size)))
    
    
    
running =True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
    if e.type == MOUSEBUTTONUP:
        cover.fill((255,255,255))         
        screencopy = screen.copy()
               
                
    mb = mouse.get_pressed()    
    mx,my = mouse.get_pos()    
    
    if mb[0]==1 or mb[2]==1 and canvasRect.collidepoint(mx,my):
        screen.set_clip(canvasRect)
        if tool=="brush":
            if mb[0]==1:
                highlighter.circlebrush(cover,(255,0,0),0)
                screen.blit(screencopy,(0,0))
                screen.blit(cover,(0,0,))
            if mb[2]==1:
                brush.explosionbrush(screen,(randint(0,255),randint(0,255),randint(0,255)),0)
    oldmx,oldmy=mx,my
    display.flip()

quit()
