from pygame import *
from random import*
from tkinter import Tk
from tkinter import filedialog
from Canvas import Canvas
from PaintLayout import PaintLayout
from BasicTool import BasicTool
from TextTool import TextTool

backgroundCol= Color(255,255,255)

# Current color
col=randint(0,255),randint(0,255),randint(0,255)
# Current size
size = 10
paintLayout = PaintLayout()
screen=paintLayout.screen
cover=paintLayout.cover

#---------------------------------------------------------------------------
################screen set up###############
#--------------set up logo------------------
paintLayout.createLogo("Resources/design/others/logo.png")

# set up canvas has to be of the ratio 680:480 -> 17:12 for background image to scale properly
canvasRect=Rect(230,120,510,360) 
canvas=Canvas(screen, canvasRect)

# React to handle clear
clearRect = Rect(700,485,40,40)
screen.blit(transform.scale(image.load("Resources/design/menubar/clear.png"), (40, 40)),clearRect)

# TODO: get picture for delete canvas - as trash can and then also add add canvas
deleteRect = Rect(230,485,40,40)

canvasNumRect = Rect(465,485,40,40)
draw.rect(screen,(0,0,0),canvasNumRect,1) # TODO make hover
canvasBackRect = Rect(384,485,80,40)
canvasNextRect = Rect(506,485,80,40)
draw.rect(screen,(0,0,0),canvasBackRect,1) # TODO make hover
draw.rect(screen,(0,0,0),canvasNextRect,1) # TODO make hover

#--------------set up menu options----------
menuPics=["open","save","undo","redo","full_screen"] # TODO full screen not implemented
menuPath = "Resources/design/menubar/"
menuRect =[]
for i in range (4):
    menuRect.append(((Rect(i*30+15,0,25,25))))
    screen.blit(transform.scale(image.load(menuPath  + menuPics[i] +".png"), (25, 25)),menuRect[i])

#--------------tool box classes-----------
toolBoxClassTextRect = Rect(10,120,168,40) # hold text that says tool box class
toolBoxClassBackRect = Rect(10,160,84,40)  # hold next arrow
toolBoxClassNextRect = Rect(95,160,84,40)  # hold next arrow
draw.rect(screen,(0,0,0),toolBoxClassTextRect,2)


#--------------set up toolbox------------
# turn to function to draw
toolBoxRect =[]
toolBoxPath = "Resources/tools/" # path for all types of tools
# types of tools for display
toolsClassName = ["tools","shape","brush","spraypaint","edit"] 
toolsName=  [["Pencil","Eraser","Fill_Bucket","Text","Eyedrop","Smudge"],
             ["Circle_Shape","Square_Shape","Line_Shape","Explosion_Brush","Polygon_Shape","Polygon_Shape_Filled"],
             ["Circle_Brush","Square_Brush","Color_Masher","Line_Brush","Sticky_Surface","alpha"],
             ["Circle","Square","Rain","Stamp_Brush","Spray_design","Spray_speed"],
             ["Move","Copy","Crop","Rotate","Flip_Vertical","Flip_Horizontal"]
            ]
            # TODO for shape add custom made text box which says toggle fill which you highlight when toggled on
            # for spray paint need picture for square and circle spray and for spray speed just have text box that says speed


def openFile(surface, canvasRect):
    Tk().withdraw()
    fileFormats = [ ('Portable Network Graphics','*.png'),
               ('Windows Bitmap','*.bmp'),
               ('JPEG / JFIF','*.jpg'),
               ('CompuServer GIF','*.gif')]
    file = filedialog.askopenfile(mode="r",title="Load",filetypes = fileFormats)
    if file != None:
        renderImage(surface, canvasRect, file)

def renderImage(surface, canvasRect, file):
    canvasSurface = surface.subsurface(canvasRect)
    loader = image.load(file.name)

    canvasSurface.blit(transform.smoothscale(loader, (canvasRect.width, canvasRect.height)), (0,0))

def saveFile(surface, canvasRect):
    Tk().withdraw()
    file = filedialog.asksaveasfile(mode='w', title = "Save As",defaultextension = ".png")
    if file != None:
        image.save(screen.subsurface(canvasRect), file.name)

def renderToolbox(toolClassNum):
    for i in range (len(toolsName[toolClassNum])):
        if i%2==0:
            x=10
        else:
            x=98
        y=(i//2)*80+215   
        toolBoxRect.append(((Rect(x,y,80,70))))
        draw.rect(screen,backgroundCol,toolBoxRect[i])
        draw.rect(screen,(0,0,0),toolBoxRect[i],2)
        screen.blit(transform.scale(image.load(toolBoxPath + toolsClassName[toolClassNum]+"/"  +str(i+1)+"_"+ toolsName[toolClassNum][i] +".png"), (80, 70)),toolBoxRect[i])
toolBoxTextRect = Rect(10,470,175,34)
toolboxTextInfoRect = Rect(10,505,180,140)

def renderToolInfoText(x,y,toolClassNum,toolName):
    # for the selected tool box box
    draw.rect(screen,(255,255,255),Rect(5,470,185,34)) # fill up box
    draw.rect(screen,(0,0,0),Rect(5,470,185,34),1) # add outline
    hover = False
    # clear text info box
    draw.rect(screen,(255,255,255),Rect(5,505,185,140)) 
    draw.rect(screen,(0,0,0),Rect(5,505,185,140),1)

    for i in range(6):
        if toolBoxRect[i].collidepoint(x,y):
            PaintLayout.drawText(screen, open(toolBoxPath+toolsClassName[toolClass]+ "/"+str(i+1)+"_"+ toolsName[toolClassNum][i]+".txt").read().splitlines()[0], (0,0,0), toolboxTextInfoRect,  17)
            toolName = toolsName[toolClassNum][i]
            hover =True
    if not hover:
        for i in range(6):
            if toolsName[toolClassNum][i]==toolName:
                PaintLayout.drawText(screen, open(toolBoxPath+toolsClassName[toolClass]+ "/"+str(i+1)+"_"+ toolName+".txt").read().splitlines()[0], (0,0,0), toolboxTextInfoRect,  17)
                break    

    toolText = toolName.replace("_", " ")
    PaintLayout.drawText(screen,toolText, (0,255,0), toolBoxTextRect,  17)

# pallete box
palleteRect = Rect(412,540,145,145)
palleteBackRect = Rect(412,686,72,30)
palleteNextRect = Rect(412+73,686,72,30)
draw.rect(screen,(0,0,0),palleteBackRect,1)
draw.rect(screen,(0,0,0),palleteNextRect,1)
draw.rect(screen,(0,0,0),palleteRect,1)

# color value
currentColorRect = Rect(30,646,160,30)  # Text says current color written in current color
draw.rect(screen,(255,255,255),Rect(5,646,185,30),0)
draw.rect(screen,(0,0,0),Rect(5,646,185,30),1) # outline in black

def renderSizeRect(size):
    fullSizeRect = Rect(5,677,185,30) # the entire size rect
    currenSizeRect = Rect(5,677,(int)(9.25*size),30)
    draw.rect(screen,(255,255,255),fullSizeRect) # white background
    draw.rect(screen,(0,0,0),currenSizeRect ) # fill in depending on the size
    draw.rect(screen,(0,0,0),fullSizeRect ,1)



#draw.rect(screen,(0,0,0),greenValRect ,1)

#wheel visually displaying current color and size 
#draw.circle(screen,col,(440,605),(75),0)
#colorwheelTextRect = Rect(370,685,140,34)
#draw.rect(screen,(0,0,0),colorwheelTextRect ,1)

#mouse coordinate
#on screen
#mouseRect = Rect(600,560,185,45)
#draw.rect(screen,(0,0,0),mouseRect ,1)
#on canvas

#stamp box
#770 end of canvas x
stampCategoryTextRect = Rect(816,349,163,30)
stampCategoryBackRect = Rect(780,349,35,30)
stampCategoryNextRect = Rect(980,349,35,30)
stampTextRect = Rect(816,380,163,30)
stampBackRect = Rect(780,380,35,30)
stampNextRect = Rect(980,380,35,30)
stampRect = Rect(797,411,200,300) #rect has to be i box 200:300
draw.rect(screen,(0,0,0),stampRect ,1)
draw.rect(screen,(0,0,0),stampCategoryTextRect ,1)
draw.rect(screen,(0,0,0),stampCategoryBackRect ,1)
draw.rect(screen,(0,0,0),stampCategoryNextRect ,1)
draw.rect(screen,(0,0,0),stampTextRect ,1)
draw.rect(screen,(0,0,0),stampBackRect ,1)
draw.rect(screen,(0,0,0),stampNextRect ,1)
#120-480 -canvas y range

#background box
backgroundRect = Rect(795,183,204,144) #the actual background has to be in rect with ratio 17:12
backgroundTextRect = Rect(816,152,163,30)
backgroundBackRect = Rect(780,152,35,30)
backgroundNextRect = Rect(980,152,35,30)
backgroundShipRect = Rect(780,121,117,30)
backgroundIslandRect = Rect(898,121,117,30)
draw.rect(screen,(0,0,0),backgroundRect ,1)
draw.rect(screen,(0,0,0),backgroundTextRect ,1)
draw.rect(screen,(0,0,0),backgroundBackRect ,1)
draw.rect(screen,(0,0,0),backgroundNextRect ,1)
draw.rect(screen,(0,0,0),backgroundShipRect ,1)
draw.rect(screen,(0,0,0),backgroundIslandRect ,1)

#music box
#musicRect = Rect(810,10,180,90)
#draw.rect(screen,(0,0,0),musicRect ,1)
#name
musicNameRect = Rect(810,10,180,25)
draw.rect(screen,(0,0,0),musicNameRect ,1)
#play stop box 
musicPlayRect = Rect(815,36,84,43)
musicStopRect = Rect(900,36,84,43)
draw.rect(screen,(0,0,0),musicPlayRect ,1)
draw.rect(screen,(0,0,0),musicStopRect ,1)
#next back 
musicBackRect = Rect(815,80,84,25)
musicNextRect = Rect(900,80,84,25)
draw.rect(screen,(0,0,0),musicBackRect ,1)
draw.rect(screen,(0,0,0),musicNextRect ,1)

maxPallate = 5
curPallate = 1
    
msg=''

        

#------------------------------------------------------------------------------------------------------------------------------------------------------------------
basicTool = BasicTool(screen)
#highlighter blit on cover    
def circlebrush(surface,x,y,col,width):
    draw.circle(surface,(col),(x,y),width)
def rectbrush(surface,x,y,col,width):
    draw.rect(surface, (col),(x,y,width,width),width)
def linebrush(surface,x,y,col,width):
    draw.line(surface,(col),(mx,my),(oldmx,oldmy),width)
def explosionbrush(surface,col,width):
    draw.line(surface,(col),(mx,my),(mx+randint(-width,width),my+randint(-width,width)))
def colormasher(surface, s, canvasRect):
    tries =0 #count number of time rectangle resized
    width =s
    while tries <10:
        colorrect=Rect(mx-width//2,my-width//2,width,width)
        if canvasRect.contains(colorrect):
            break
        tries+=1
        width = width//2
        
    col=transform.average_color(screen,colorrect)
    draw.rect(screen,col,colorrect)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#shapes

def ellipse(surface, col,fill, canvasRect):
    screen.blit(surface,canvasRect)
    if perfect:  #perfect use circle
        if (abs(mx-startx)+abs(my-starty))//2> size:
            draw.circle(screen,col,(startx,starty),((abs(mx-startx)+abs(my-starty))//2),size*fill)
        else:
            draw.circle(screen,col,(startx,starty),((abs(mx-startx)+abs(my-starty))//2),0)
    else:
        if abs(mx-startx)>size*2 and abs(my-starty)> size*2:
            draw.ellipse(screen,col,(min(mx,startx),min(my,starty),abs(mx-startx),abs(my-starty)),size*fill)
        else:
            draw.ellipse(screen,col,(min(mx,startx),min(my,starty),abs(mx-startx),abs(my-starty)),0)
   

def rect(surface, col,fill, canvasRect):
    screen.blit(surface,canvasRect)
    if perfect:        
        draw.rect(screen,col,((startx),(starty),((mx-startx+my-starty)//2),((mx-startx+my-starty)//2)),size*fill)
    else:
        draw.rect(screen,col,((startx),(starty),(mx-startx),(my-starty)),size*fill)
        
def polygon(polylist,fill):    
    draw.polygon(screen,col,polylist,size*fill)
def line(surface,col,canvasRect):
    screen.blit(surface,canvasRect)
    draw.line(screen,(col),((startx),(starty)),(mx,my), size)
def aaline(surface,col,canvasRect):
    screen.blit(surface,canvasRect)
    draw.aaline(screen,(col),(startx,starty),(mx,my))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#category spray

def sprayCircle(size,speed,radius,spraydesign,col):#spray out circles
    for i in range (speed):
        x=mx+randint(-radius,radius)
        y=my+randint(-radius,radius)
        if spraydesign ==1:
            if ((x-mx)**2+(y-my)**2)<radius**2:#equation of circle
                draw.circle(screen,col,(x,y),size)
        else:
            draw.circle(screen,col,(x,y),size)
            
spraySpeed =10
spraydesign =1 #by default paint will spray in shape of a circle

def spraySquare(size,speed,radius,spraydesign,col):
    for i in range (speed):
        x=mx+randint(-radius,radius)
        y=my+randint(-radius,radius)
        if spraydesign ==1:
            if ((x-mx)**2+(y-my)**2)<radius**2:#equation of circle
                draw.rect(screen,col,(x,y,size,size))
        else:
            draw.rect(screen,col,(x,y,size,size))
            
def rainSquare(size,speed,radius,spraydesign,col):
    for i in range (speed):
        x=mx+randint(-radius,radius)
        y=my+randint(-radius,radius)
        if spraydesign ==1:
            if ((x-mx)**2+(y-my)**2)<radius**2:#equation of circle
                draw.line(screen,(col),(x,y),(x+randint(-3,3),y+randint(-3,3)), size) 
        else:
            draw.line(screen,(col),(x,y),(x+randint(-3,3),y+randint(-3,3)), size)
            
def clonestamp (cdx,cdy,sx,sy,size):    
    difx,dify=mx-sx,my-sy
    if min(cdx+difx,cdy+dify)>0:
        clonedrect=Rect(cdx+difx,cdy+dify,size,size)
        cloned=screen.subsurface(clonedrect).copy()
        cloned.convert()
        screen.blit(cloned,(mx,my))   

#Initialize text
textTool = TextTool(screen)
textTool.text((255,0,0),"Back",22,160, 25)
textTool.text((0,255,0),"Next",107,160, 25) 
size = 17

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
running =True
size =10
tool = 'Pencil'
toolClass = 0 #Set starting class to tools
renderToolbox(toolClass) #do it every time tool changes or class changes
draw.rect(screen,(0,255,0),toolBoxRect[0],2)
canvasSurface=screen.subsurface(canvasRect)
copy = canvasSurface.copy() #store copy of canvas need for some tools
cropselected = canvasSurface
first = False #save original position of mouse to track clone
saved = False # track if clone has been initiated
sticky = False
alpha = False
perfect=False
startx,starty = 0,0
polylist =[]

while running:
    mx,my=mouse.get_pos()
    mb= mouse.get_pressed()
    keys = key.get_pressed()
    screen.set_clip()
    #set text to current color
    PaintLayout.drawText(screen, "Current Color", col, currentColorRect, 20)
    renderSizeRect(size) # fill rectangle depending on size
    renderToolInfoText(mx,my,toolClass,tool)
    draw.rect(screen,(255,255,255),palleteRect,0)
    screen.blit(transform.scale(image.load(f"Resources/palette/Palette{curPallate}.png"), (145, 145)),palleteRect)

    #the hover effect ######
    if clearRect.collidepoint(mx,my): #clear box
        draw.rect(screen,(0,255,0),clearRect,1)
    else:
        draw.rect(screen,(0,0,0),clearRect,1)

    if deleteRect.collidepoint(mx,my): # for delete box
        draw.rect(screen,(0,255,0),deleteRect,1) 
    else:
        draw.rect(screen,(0,0,0),deleteRect,1)

    if toolBoxClassBackRect.collidepoint(mx,my): #Back box
        draw.rect(screen,(0,255,0),toolBoxClassBackRect,1)
    else:
        draw.rect(screen,(0,0,0),toolBoxClassBackRect,1) 

    if toolBoxClassNextRect.collidepoint(mx,my): #Next box
        draw.rect(screen,(0,255,0),toolBoxClassNextRect,1)
    else:
        draw.rect(screen,(0,0,0),toolBoxClassNextRect,1)    
       
    screen.set_clip(canvasRect)

    if toolsClassName[toolClass] == 'shape':
        if keys[K_LSHIFT] or keys[K_RSHIFT] :
            perfect = True
        else :
            perfect = False
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type==KEYDOWN:
            if tool == 'Text':# only text gets impacted by
                msg=textTool.handleKeystrokes(e,msg)
              
        if toolClass == 2 or toolClass ==1 : #for shape or brush class
            if(size>10):
                size = size %10+1

        if e.type == MOUSEBUTTONUP:
            if toolsClassName[toolClass] == 'edit' and e.button == 3:
                copy = canvasSurface.copy()      
            if(toolClass == 2 or toolClass ==1) and (e.button==1 or e.button == 3): # for brush class
                cover.fill((255,255,255))
                copy = canvasSurface.copy()
                
        if e.type == MOUSEBUTTONDOWN: 
        #for something you want the event to be triggered as soon as mouse is clicked
            if e.button==1: #tool selection
                    print(str(mx) + "," + str(my))
                    for i in range(6):
                        if toolBoxRect[i].collidepoint(mx,my):
                            tool = toolsName[toolClass][i]
                            screen.set_clip()  #unlock screen
                            renderToolbox(toolClass) #redraw selection
                            draw.rect(screen,(0,255,0),toolBoxRect[i],2)
                            screen.set_clip(canvasRect)
                            
                    if toolBoxClassBackRect.collidepoint(mx,my): #for next tool class
                        if toolsClassName[toolClass] == 'edit':
                            screen.blit(copy,(canvasRect))
                        toolClass -=1 
                        toolClass =max (0,toolClass)
                        tool = toolsName[toolClass][0]
                        #with the rest of the rendering make it green if selected or hover

                        screen.set_clip()  #unlock screen
                        renderToolbox(toolClass) #redraw selection
                        draw.rect(screen,(0,255,0),toolBoxRect[0],2)
                        tool = toolsName[toolClass][0]
                        screen.set_clip(canvasRect)
                        if  tool == "Stamp_Brush":
                            first = False #save original position of mouse to track clone
                            saved = False # track if clone has been initiated
                        
                    if toolBoxClassNextRect.collidepoint(mx,my): #for next tool class
                        if toolsClassName[toolClass] == 'edit':
                            screen.blit(copy,(canvasRect))
                        toolClass +=1 
                        toolClass =min (len(toolsName)-1,toolClass)
                        tool = toolsName[toolClass][0]

                        screen.set_clip()  #unlock screen
                        renderToolbox(toolClass) #redraw selection
                        draw.rect(screen,(0,255,0),toolBoxRect[0],2)
                        tool = toolsName[toolClass][0]
                        screen.set_clip(canvasRect)
                        if  tool == "Stamp_Brush":
                            first = False #save original position of mouse to track clone
                            saved = False # track if clone has been initiated

                    if menuRect[0].collidepoint(mx,my):
                        openFile(screen, canvasRect)
                    if menuRect[1].collidepoint(mx,my):
                        saveFile(screen, canvasRect)
                    if clearRect.collidepoint(mx,my):
                        canvas.clear()
                    if palleteRect.collidepoint(mx,my):
                        col = basicTool.eyedrop()
                    if palleteNextRect.collidepoint(mx,my):
                        curPallate+=1
                        curPallate=min(curPallate, maxPallate)
                    if palleteBackRect.collidepoint(mx,my):
                        curPallate-=1
                        curPallate = max(curPallate, 1)    
                    if tool == 'Text' or toolsClassName[toolClass] == 'shape' or toolsClassName[toolClass] == 'edit': 
                        cover.fill((255,255,255))
                        copy = canvasSurface.copy() 
                           
            if canvasRect.collidepoint(mx,my):
                if e.button==1: 
                    startx,starty = e.pos
                    #polygon tool
                    if tool == "Polygon_Shape" or tool == "Polygon_Shape_Filled":
                        draw.circle(screen,(0,0,0),(mx,my),1)
                        polylist.append((mx,my))
                        #polygon(polylist,1)
                    if tool!='Polygon_Shape' and tool != "Polygon_Shape_Filled":
                        polylist=[]
                    #text tool
                    if tool=='Text' and canvasRect.collidepoint(mx,my):
                        textTool.text(col,msg,mx,my,size)
                        msg = ''
                    #toggle setting
                    if tool == "Sticky_Surface":
                        if sticky:
                            sticky =False
                        else:
                            sticky = True
                        print (sticky)
                    if tool == "alpha":
                         if alpha:
                            alpha =False
                            cover.set_alpha(255)
                         else:
                            alpha = True
                            cover.set_alpha(55)
                         print(alpha)
                    if tool == "Spray_design":
                        if spraydesign==1:
                            spraydesign=2
                            time.wait(10)
                        else:
                            spraydesign=1
                            time.wait(10)
                    
                    
            if e.button == 4:
                size = min(20, size +1)
            if e.button == 5:
               size = max(1, size -1)              
            if  e.button==3 and e.button!= 4 and e.button!= 5:
                startx,starty = e.pos
                if len(polylist)>2:
                    if tool=='Polygon_Shape':
                        polygon(polylist,1)            
                        polylist=[]
                    if tool=='Polygon_Shape_Filled' :
                        polygon(polylist,0)            
                        polylist=[]
                    
                if toolsClassName[toolClass] == 'edit':
                    copy = canvasSurface.copy() 
                    time.wait(100)

                if tool =='Fill_Bucket':
                    basicTool.fill((randint(0,255),randint(0,255),randint(0,255)))
                if tool == 'Eraser':
                    basicTool.fill((255,255,255))
                    
                if tool == "Stamp_Brush":
                    cspdx,cspdy=mx,my
                    first = True
                    saved = True

                if tool=="Move":
                    screen.blit(copy,(canvasRect))  
                    draw.rect(screen,(255,255,255),(croprect))                          
                    screen.blit(cropselected,(mx-cx/2,my-cy/2))
                    croprect=Rect(mx-cx/2,my-cy/2,cx,cy)                                           
                    
                if tool=="Copy":
                    screen.blit(copy,(canvasRect))
                    screen.blit(cropselected,(mx-cx/2,my-cy/2))
                    
                if tool=="Crop":
                    screen.blit(copy,(canvasRect))
                    draw.rect(screen,(255,255,255),canvasRect)
                    screen.blit(cropselected,(croprect))
                    copy = canvasSurface.copy()
                               
                if tool=="Rotate":
                    screen.blit(copy,(canvasRect))  
                    draw.rect(screen,(255,255,255),(croprect))
                    cropselected=transform.rotate(cropselected,90)
                    screen.blit(cropselected,(croprect))   
                   
                if tool =="Flip_Vertical":
                    screen.blit(copy,(canvasRect))  
                    draw.rect(screen,(255,255,255),(croprect))
                    cropselected=transform.flip(cropselected, False, True)
                    screen.blit(cropselected,(croprect))   
                    
                if tool =="Flip_Horizontal":
                    screen.blit(copy,(canvasRect))  
                    draw.rect(screen,(255,255,255),(croprect))
                    cropselected=transform.flip(cropselected, True, False)
                    screen.blit(cropselected,(croprect))   
                
    if tool == 'Text'  : # Text reblit old screen + text
        screen.blit(copy,canvasRect)
    x,y=mx,my
    if sticky and toolClass == 2:
        x -= x%((int)(size*1.5))
        y -= y%((int)(size*1.5))
    #when cursor hovers over selected tools highlight  by blitting on tool cover and then redraw tools
    if canvasRect.collidepoint(mx,my):
        if mb[0]==1: #for some things it is better to track when the mouse is down
            #tools class
            if tool=='Pencil':
                basicTool.pencil(col, (oldmx, oldmy))
            if tool == 'Eraser':
                circlebrush(screen,x,y,(255,255,255),size)
            if tool =='Fill_Bucket':
                basicTool.fill(col)
                
            if tool == 'Eyedrop':
                col = basicTool.eyedrop()
            if tool == 'Smudge':
                basicTool.tonechanger(1, canvasRect, size)
            #shape class
            if tool == "Circle_Shape":
                ellipse(copy, col,1, canvasRect)
            if tool == "Square_Shape":
                rect(copy, col,1, canvasRect)
            

            if tool == "Line_Shape":
                line(copy,col, canvasRect)
            if tool == "Explosion_Brush":
                explosionbrush(screen,col,size)
            
            #brush class
            if tool == 'Circle_Brush':
                circlebrush(cover,x,y,col,size)
            if tool == "Square_Brush":
                rectbrush(cover,x,y,col,size)
            if tool == "Color_Masher":
                colormasher(copy, size*5)
                copy = canvasSurface.copy()
            if tool == "Line_Brush":
                linebrush(cover,x,y,col,size)           
            if toolClass == 2 : # for highlighter blit copy
                screen.blit(copy,canvasRect)
                screen.blit(cover,(0,0))      
                
            
            #spray
            if tool == "Stamp_Brush":
                if first:
                    sx,sy=mx,my
                    first=False
                if saved:
                    clonestamp(cspdx,cspdy,sx,sy,size)

            if tool == "Circle":
                sprayCircle(1,spraySpeed,size,spraydesign,col)
            if tool == "Square":
                spraySquare (1,spraySpeed,size,spraydesign,col)
            if tool == "Rain":
                rainSquare(1,spraySpeed,size,spraydesign,col)
            #if tool == "Populater":
            if tool == "Spray_speed":
               spraySpeed+=1
            
            

            #edit class
            if toolsClassName[toolClass] == 'edit':
                angle=0
                screen.blit(copy,(canvasRect))    
                croprect=Rect(startx,starty,mx-startx,my-starty)                
                croprect.normalize()
                cropselected=screen.subsurface(croprect).copy()
                draw.rect(screen,(0,0,0),croprect,1)
                cx,cy=cropselected.get_size()
                
        if mb[2]==1:
            #tool right click
            if tool=='Pencil':
                basicTool.pencil((randint(0,255),randint(0,255),randint(0,255)), (oldmx,oldmy))
            if(tool == 'Eyedrop'):
                col = (randint(0,255),randint(0,255),randint(0,255))
            if tool == 'Smudge':
                basicTool.tonechanger(-1, canvasRect, size)
            #shapes right click
            if tool == "Circle_Shape":
                 ellipse(copy, col,0)
            if tool == "Square_Shape":
                 rect(copy, col,0)
            if tool == "Line_Shape":
                 aaline(copy,col)
                           
            #brush right click
            if tool == 'Circle_Brush':
                circlebrush(cover,x,y,(randint(0,255),randint(0,255),randint(0,255)),size)
            if tool == "Square_Brush":
                rectbrush(cover,x,y,(randint(0,255),randint(0,255),randint(0,255)),size)
            if tool == "Explosion_Brush":
                explosionbrush(screen,(randint(0,255),randint(0,255),randint(0,255)),size)
            if tool == "Line_Brush":
                linebrush(cover,x,y,(randint(0,255),randint(0,255),randint(0,255)),size) 
            if toolClass == 2  : # for brushes blit copy
                screen.blit(copy,canvasRect)
                screen.blit(cover,(0,0))
            
            #spray class
            if tool == "Circle":
                sprayCircle(1,spraySpeed,size,spraydesign,(randint(0,255),randint(0,255),randint(0,255)))
            if tool == "Square":
                spraySquare (1,spraySpeed,size,spraydesign,(randint(0,255),randint(0,255),randint(0,255)))
            if tool == "Rain":
                rainSquare(1,spraySpeed,size,spraydesign,(randint(0,255),randint(0,255),randint(0,255)))
           
            if tool == "Spray_speed":
               spraySpeed=max(speed-1,1)            
                       
    oldmx,oldmy,=mx,my 
    if tool=='Text' and canvasRect.collidepoint(mx,my):
        copy = canvasSurface.copy() 
        textTool.text(col,msg,mx,my,size)          
      
    display.flip()
quit()
