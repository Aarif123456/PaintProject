from pygame import *
#use for color highlighter and eraser    
screen = display.set_mode((1200,675))
screen.fill((255,255,255))
cover = Surface((1200,675)).convert()#make blank Surface
cover.set_alpha(55)
cover.set_colorkey((255,255,255))
tool="highlight"

canvasRect=Rect(300,100,700,500)
draw.rect(screen,(0,0,0),canvasRect,5)

highlightRect=Rect(100,100,100,100)
draw.rect(screen,(255,0,0),highlightRect)
def highlighter(col):
    draw.circle(cover,(col),(mx,my),50)
    screen.blit(screencopy,(0,0))
    screen.blit(cover,(0,0))
screencopy = screen.copy()
cover.fill((255,255,255))
running =True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False        
        if e.type == MOUSEBUTTONUP:
            if  e.button==1 and e.button!= 4 and e.button!= 5:                
                cover.fill((255,255,255))         
                screencopy = screen.copy()
    mb = mouse.get_pressed()    
    mx,my = mouse.get_pos()


    if mb[0]==1 or mb[2]==1 and canvasRect.collidepoint(mx,my):
        screen.set_clip(canvasRect)
        if tool=="highlight":
            if mb[0]==1:
                highlighter((0,255,0))
            if mb[2]==1:
                highlighter((255,255,255))   
    display.flip()

quit()
