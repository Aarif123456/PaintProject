from pygame import *
from random import*   
screen = display.set_mode((1200,675))
screen.fill((255,255,255))
tool="crophorizontal"
toolcategory="crop"
canvasRect=Rect(300,100,700,500)
draw.rect(screen,(0,0,0),canvasRect,5)
pencilRect=Rect(100,100,100,100)
draw.rect(screen,(255,0,0),pencilRect)
canvasSurface=screen.subsurface(canvasRect)
running =True
while running:                       
    for e in event.get():       
        if e.type == QUIT:
            running = False
        #if key pressed down arrow
        if e.type == MOUSEBUTTONDOWN:
            copy=canvasSurface.copy()
            startx,starty = e.pos
            if toolcategory=='crop' and e.button==1:
                copy = canvasSurface.copy()                
            if e.button == 4:
               size += 1
            if e.button == 5:
               if size!=1:               
                   size -= 1 
    mb = mouse.get_pressed()    
    mx,my = mouse.get_pos()
    if mb[0]==1 or mb[2]==1 and canvasRect.collidepoint(mx,my):
        screen.set_clip(canvasRect)
        if toolcategory=="crop":#making it a function gives some errors plus there is no point since it is only being used once
            if mb[0]==1:#select if category crop
                angle=0
                screen.blit(copy,(canvasRect))    
                croprect=Rect(startx,starty,mx-startx,my-starty)                
                croprect.normalize()
                cropselected=screen.subsurface(croprect).copy()
                draw.rect(screen,(0,0,0),croprect,1)
                cx,cy=cropselected.get_size()
            if mb[2]==1:
                if tool=='cropmove':
                    screen.blit(copy,(canvasRect))  
                    draw.rect(screen,(255,255,255),(croprect))                          
                    screen.blit(cropselected,(mx-cx/2,my-cy/2))
                    croprect=Rect(mx-cx/2,my-cy/2,cx,cy)                    
                    copy = canvasSurface.copy()                        
                    time.wait(200)
                if tool=='copy':
                    screen.blit(copy,(canvasRect))
                    screen.blit(cropselected,(mx-cx/2,my-cy/2))
                    time.wait(200)
                if tool=='crop':
                    draw.rect(screen,(255,255,255),canvasRect)
                    screen.blit(cropselected,(croprect))
                    copy = canvasSurface.copy()                    
                if tool=='croprotate':
                    screen.blit(copy,(canvasRect))  
                    draw.rect(screen,(255,255,255),(croprect))
                    cropselected=transform.rotate(cropselected,90)
                    screen.blit(cropselected,(croprect))   
                    time.wait(200)
                if tool =='cropvertical':
                    screen.blit(copy,(canvasRect))  
                    draw.rect(screen,(255,255,255),(croprect))
                    cropselected=transform.flip(cropselected, False, True)
                    screen.blit(cropselected,(croprect))   
                    time.wait(200)
                if tool =='crophorizontal':
                    screen.blit(copy,(canvasRect))  
                    draw.rect(screen,(255,255,255),(croprect))
                    cropselected=transform.flip(cropselected, True, False)
                    screen.blit(cropselected,(croprect))   
                    time.wait(200)              
    oldmx,oldmy,=mx,my
    display.flip()

quit()
