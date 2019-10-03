from pygame import *
from random import*
screen = display.set_mode((1024,720 ))
screen.fill((255,255,255))
col=randint(0,255),randint(0,255),randint(0,255)
size = 10
def pencil(col):
    mx,my=mouse.get_pos()
    draw.line(screen,(col),(oldmx,oldmy),(mx,my),3)
#eraser use brush class or 
def eyedrop():
    drawcol=screen.get_at((mx,my))
def tonechanger():
    tcol=screen.get_at((mx,my))
    if min(tcol)>10:
        ncol=(tcol[0]-5,tcol[1]-5,tcol[2]-5)    
        time.wait(15)        
        draw.circle(screen,ncol,(mx-size//2,my-size//2),size)
def fill(col):
    fillpos=[(mx,my)]
    oldcol=screen.get_at((mx,my))
    if oldcol!=col:
        while len(fillpos)>0:
            while len(fillpos)>0:
                x,y = fillpos.pop()
                if screen.get_at((x,y))==oldcol:
                    screen.set_at((x,y),col)
                    fillpos+=[(x+1,y), (x-1,y),(x,y+1),(x,y-1)]
def text(col):
    comicFont = font.SysFont("Comic Sans MS", size)
    txtpic=comicFont.render (msg, False, (col))#getting mx,my seperatly to avoid bracket
    draw.rect(screen,(255,255,255),(mx,my,txtpic.get_width(),txtpic.get_height()))#create rect and text on new surfaxc until enter pressed
    screen.blit(txtpic,(300,300))#300,300 replaced by mx,my corralation to middle
numshiftlist=[')','!','@','#','$','%','^','&','*','(']
msg=''
#------------------------------------------------------------------------------------------------------------------------------------------------------------------
class brush:#higlighter blit on cover    
    def circlebrush(surface,col,width):
        draw.circle(surface,(col),(mx,my),size)
    def rectbrush(surface,col,width):
        draw.rect(surface, (col),(mx,my,size,size),width)
    def linebrush(surface,col,width):
        draw.line(surface,(col),(mx,my),(oldmx,oldmy))
    def explosionbrush(surface,col,width):
        draw.line(surface,(col),(mx,my),(mx+randint(-size,size),my+randint(-size,size)))
    #def stampbrush(surface,category,stamp,width):
    #def color masher 
    #if sticky mode on dx,dy=dx//10,dy//10
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
def ellipse(surface, col):
    screen.blit(surface,(0,0))
    if abs(mx-startx)>size*2 and abs(my-starty)> size*2:
        draw.ellipse(screen,col,(min(mx,startx),min(my,starty),abs(mx-startx),abs(my-starty)),size)
    else:
        draw.ellipse(screen,col,(min(mx,startx),min(my,starty),abs(mx-startx),abs(my-starty)),0)
    #perfect use circle
perfect=False
def rect(surface, col):
    screen.blit(surface,(0,0))
    if perfect:        
        draw.rect(screen,col,((startx),(starty),(mx-startx),(my-starty)))
    else:
        draw.rect(screen,col,((startx),(starty),((mx-startx+my-starty)//2),((mx-startx+my-starty)//2)))
def polygon(polylist):    
    draw.polygon(screen,(0,0,0),polylist)
def line(surface,col):
    screen.blit(surface,(0,0))
    draw.line(screen,(col),start,(mx,my), size)
def aaline(surface,col):
    screen.blit(surface,(0,0))
    draw.aaline(screen,(col),start,(mx,my))
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#category spray
class spray:
    def circle(size,speed,radius,sprayshapecircle,col):#if sprayshapecircle: True or False
        for i in range (speed):
            x=mx+randint(-radius,radius)
            y=my+randint(-radius,radius)
            if spraydesign ==1:
                if ((x-mx)**2+(y-my)**2)<radius**2:#equation of circle
                    if sprayshapecircle:
                        draw.circle(screen,col,(x,y),size)
                    else:
                        draw.rect(screen,col,(x,y,size,size))                    
    def square(size,speed,radius,sprayshapecircle,col):
        for i in range (speed):
            x=mx+randint(-radius,radius)
            y=my+randint(-radius,radius)
            if sprayshapecircle:
                draw.circle(screen,col,(x,y),size)
            else:
                draw.rect(screen,col,(x,y,size,size))

def sprayshapecirclerect():
    if sprayshapecircle:
        sprayshapecircle==False
        time.wait(100)
    else:
        sprayshapecircle==True
        time.wait(100)
def sprayspeed():
    if mb[0]==1:
        speed+=1
    if mb[2]==1:
        speed=max(speed+1,1)

                    
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
running =True
tool = 'pencil'
while running:                   
    for e in event.get():       
        if e.type == QUIT:
            running = False
        if e.type==KEYDOWN:
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
        if e.type == MOUSEBUTTONDOWN:
            if e.button==1: 
                copy = screen.copy()
                startx,starty = e.pos
            if e.button==3:#right click
                copy=screen.copy()
                startx,starty = e.pos
                polygon(polylist)            
                polylist=[]
            if e.button == 4:
               size += 1 
            if e.button == 5:
               if size!=1:               
                   size -= 1  
    mx,my=mouse.get_pos()
    mb= mouse.get_pressed()
    if mb[0]==1:
        if tool!='polygon':
            polylist=[]
        if tool=='polygon':
            polylist.append((mx,my))
        if tool=='pencil':
            pencil(col)
    #if mb[2]==1:
                   
    oldmx,oldmy,=mx,my
    display.flip()
quit()
