from pygame import *
#use for color highlighter and eraser
numshiftlist=[')','!','@','#','$','%','^','&','*','(']
screen = display.set_mode((1200,675))
screen.fill((255,255,255))
tool="text"
canvasRect=Rect(300,100,700,500)
draw.rect(screen,(0,0,0),canvasRect,5)
font.init()
size=20

textRect=Rect(100,100,100,100)
draw.rect(screen,(255,0,0),textRect)
def text(col):
    comicFont = font.SysFont("Comic Sans MS", size)
    txtpic=comicFont.render (msg, False, (col))#getting mx,my seperatly to avoid bracket
    draw.rect(screen,(255,255,255),(mx,my,txtpic.get_width(),txtpic.get_height()))#create rect and text on new surface until enter ressed
    screen.blit(txtpic,(mx,my))
screencopy = screen.copy()
msg=''
running =True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type==KEYDOWN:
            print(e.key)
            if key.get_mods()& KMOD_CAPS and not key.get_mods()& KMOD_SHIFT and e.key >96 and e.key <123:                
                msg+=chr(e.key-32)
            elif key.get_mods()& KMOD_SHIFT and not key.get_mods()& KMOD_CAPS and e.key >96 and e.key <123:
                msg+=chr(e.key-32)
            elif key.get_mods()& KMOD_SHIFT and e.key >47 and e.key<60:
                msg+=numshiftlist[e.key-48]
            elif e.key==32:
                msg+=' '
            elif e.key>32 and e.key<126  :                
                msg+=chr(e.key)
            elif e.key==8:
                msg=msg[:-1]
                
            
            
    draw.rect(screen,(255,255,255),canvasRect)    
    mb = mouse.get_pressed()    
    mx,my = mouse.get_pos()  
    if tool=="text":            
        text((255,0,0))            
        #highlighter((255,255,255))   
    display.flip()

quit()
