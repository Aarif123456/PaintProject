from pygame import *
from random import *
from PaintHelper import * 
from Canvas import Canvas
from PaintLayout import PaintLayout
from BasicTool import BasicTool
from TextTool import TextTool
from Brush import Brush
from Shapes import Shapes
from Spray import Spray
from Hover import Hover
from Toolbar import Toolbar

#-------------------------------------------------------------------------
backgroundCol = Color(255,255,255)
# Current color - start off with random color
col = randint(0,255),randint(0,255),randint(0,255)
size = 10 # Current size
paintLayout = PaintLayout()
screen = paintLayout.screen
cover = paintLayout.cover

#-------------------------------------------------------------------------
################screen set up###############
paintLayout.createLogo("Resources/design/others/logo.png")
# set up canvas has to be of the ratio 680:480 -> 17:12 for background image to scale properly
canvasRect = Rect(230,120,510,360) 
canvas = Canvas(screen, canvasRect)

# React to handle clear
clearRect = Rect(700,485,40,40)
draw.rect(screen,backgroundCol,clearRect,0)
Hover.addHover(clearRect)
addImage(screen, (40, 40), clearRect, "Resources/design/menubar/clear.png")


#--------------set up toolbar ----------

toolbar = Toolbar(screen)
toolbar.addFunction("open", canvas.openFile)
toolbar.addFunction("save", canvas.saveFile)
toolbar.addFunction("undo", canvas.undo)
toolbar.addFunction("redo", canvas.redo)
    

#--------------tool box classes-----------
toolBoxClassTextRect = Rect(10,120,168,40) # hold text that says tool box class
toolBoxClassBackRect = Rect(10,160,84,40)  # hold next arrow
toolBoxClassNextRect = Rect(95,160,84,40)  # hold next arrow
draw.rect(screen,backgroundCol,toolBoxClassTextRect,0)
Hover.addHover(toolBoxClassBackRect)
Hover.addHover(toolBoxClassNextRect)


#--------------set up toolbox------------
# turn to function to draw
toolBoxRect =[]
toolBoxPath = "Resources/tools/" # path for all types of tools
# types of tools for display
toolsClassName = ["tools","shape","brush","spray","edit"] 
toolsName=  [["Pencil","Eraser","Fill_Bucket","Text","Eyedrop","Smudge"],
             ["Circle_Shape","Square_Shape","Line_Shape","Explosion_Brush","Polygon_Shape","Polygon_Shape_Filled"],
             ["Circle_Brush","Square_Brush","Color_Masher","Line_Brush","Sticky_Surface","alpha"],
             ["Circle","Square","Rain","Stamp_Brush","Spray_design","Spray_speed"],
             ["Move","Copy","Crop","Rotate","Flip_Vertical","Flip_Horizontal"]
            ]

def renderToolbox(toolClassNum):
    for i in range (len(toolsName[toolClassNum])):
        # For two columns
        x = 10 if i%2 == 0 else 98
        y=(i//2)*80+215   
        toolBoxRect.append(((Rect(x,y,80,70))))
        draw.rect(screen,backgroundCol,toolBoxRect[i])
        draw.rect(screen,(0,0,0),toolBoxRect[i],2)
        addImageNonSmooth(screen, (80, 70), toolBoxRect[i], f"{toolBoxPath}{toolsClassName[toolClassNum]}/{i+1}_{toolsName[toolClassNum][i]}.png" )

toolBoxTextRect = Rect(10,470,175,34)
toolboxTextInfoRect = Rect(10,505,180,140)

def renderToolInfoText(x,y,toolClassNum,toolName):
    # for the selected tool box box
    draw.rect(screen,backgroundCol,Rect(5,470,185,34)) # fill up box
    draw.rect(screen,(0,0,0),Rect(5,470,185,34),1) # add outline
    hover = False
    # clear text info box
    draw.rect(screen,backgroundCol,Rect(5,505,185,140)) 
    draw.rect(screen,(0,0,0),Rect(5,505,185,140),1)
    curTool = toolsName[toolClassNum].index(toolName)

    for i in range(6):
        if toolBoxRect[i].collidepoint(x,y):
            curTool = i
            break

    PaintLayout.drawText(screen, open(toolBoxPath+toolsClassName[toolClass]+ "/"+str(curTool+1)+"_"+ toolsName[toolClassNum][curTool]+".txt").read().splitlines()[0], (0,0,0), toolboxTextInfoRect,  17)
    toolName = toolsName[toolClassNum][curTool]
    toolText = toolName.replace("_", " ")
    PaintLayout.drawText(screen,toolText, (0,255,0), toolBoxTextRect, 25)

# pallete box
palleteRect = Rect(412,540,145,145)
palleteBackRect = Rect(412,686,72,30)
palleteNextRect = Rect(412+73,686,72,30)
Hover.addHover(palleteBackRect)
Hover.addHover(palleteNextRect)
draw.rect(screen,(0,0,0),palleteRect,1)

# color value
currentColorRect = Rect(30,646,160,30)  # Text says current color written in current color
draw.rect(screen,backgroundCol,Rect(5,646,185,30),0)
draw.rect(screen,(0,0,0),Rect(5,646,185,30),1) # outline in black

def renderSizeRect(size):
    fullSizeRect = Rect(5,677,185,30) # the entire size rect
    currenSizeRect = Rect(5,677,(int)(9.25*size),30)
    draw.rect(screen,backgroundCol,fullSizeRect) # white background
    draw.rect(screen,(0,0,0),currenSizeRect ) # fill in depending on the size
    draw.rect(screen,(0,0,0),fullSizeRect ,1)


#stamp box
#770 end of canvas x
stampCategoryTextRect = Rect(816,349,163,30)
stampCategoryBackRect = Rect(780,349,35,30)
stampCategoryNextRect = Rect(980,349,35,30)
Hover.addHover(stampCategoryBackRect)
Hover.addHover(stampCategoryNextRect)
draw.rect(screen,(0,0,0),stampCategoryTextRect ,1)

stampTextRect = Rect(816,380,163,30)
stampBackRect = Rect(780,380,35,30)
stampNextRect = Rect(980,380,35,30)
Hover.addHover(stampBackRect)
Hover.addHover(stampNextRect)
draw.rect(screen,(0,0,0),stampTextRect ,1)

# rect has to be i box 200:300
# 120-480 -canvas y range
stampRect = Rect(797,411,200,300) 
draw.rect(screen,(0,0,0),stampRect ,1)

#background box
# the actual background has to be in rect with ratio 17:12
backgroundRect = Rect(795,183,204,144) 
backgroundTextRect = Rect(816,152,163,30)
backgroundBackRect = Rect(780,152,35,30)
backgroundNextRect = Rect(980,152,35,30)

draw.rect(screen,(0,0,0),backgroundRect ,1)
draw.rect(screen,(0,0,0),backgroundTextRect ,1)
Hover.addHover(backgroundBackRect)
Hover.addHover(backgroundNextRect)


backgroundShipRect = Rect(780,121,117,30)
backgroundIslandRect = Rect(898,121,117,30)
Hover.addHover(backgroundShipRect)
Hover.addHover(backgroundIslandRect)

#music box
musicNameRect = Rect(810,10,180,25)
draw.rect(screen,(0,0,0),musicNameRect ,1)
#play stop box 
musicPlayRect = Rect(815,36,84,43)
musicStopRect = Rect(900,36,84,43)
Hover.addHover(musicPlayRect)
Hover.addHover(musicStopRect)

#next back 
musicBackRect = Rect(815,80,84,25)
musicNextRect = Rect(900,80,84,25)
Hover.addHover(musicBackRect)
Hover.addHover(musicNextRect)

maxPallate = 5
curPallate = 1
    
msg=""        

#------------------------------------------------------------------------------------------------------------------------------------------------------------------
basicTool = BasicTool(screen)
brush = Brush(screen)
highlighter = Brush(cover) 
shapes = Shapes(screen)
spray = Spray(screen)
hover = Hover(screen)

spraySpeed = 10
spraydesign = 1 # by default paint will spray in shape of a circle

def clonestamp(cd,dif,size):    
    difx,dify = dif
    cdx,cdy = cd
    if min(cdx+difx,cdy+dify)>0:
        clonedrect = Rect(cdx+difx,cdy+dify,size,size)
        cloned = screen.subsurface(clonedrect).copy()
        cloned.convert()
        screen.blit(cloned,(mx,my))   

#Initialize text
textTool = TextTool(screen)
textTool.text((255,0,0),"Back",22,160, 25)
textTool.text((0,255,0),"Next",107,160, 25) 
size = 17

#-------------------------------------------------------------------------------------
running = True
size = 10
tool = "Pencil"
toolClass = 0 # Set starting class to tools
renderToolbox(toolClass) # do it every time tool changes or class changes
draw.rect(screen,(0,255,0),toolBoxRect[0],2)
canvasSurface=screen.subsurface(canvasRect)
copy = canvasSurface.copy() # store copy of canvas need for some tools
cropselected = canvasSurface
first = False # save original position of mouse to track clone
saved = False # track if clone has been initiated
alpha = False
perfect = False
startx,starty = 0,0
polylist = []
while running:
    mx,my = mouse.get_pos()
    mb = mouse.get_pressed()
    keys = key.get_pressed()
    screen.set_clip()
    # set text to current color
    PaintLayout.drawText(screen, "Current Color", col, currentColorRect, 20)
    renderSizeRect(size) # fill rectangle depending on size
    renderToolInfoText(mx,my,toolClass,tool)
    draw.rect(screen,backgroundCol,palleteRect,0)
    screen.blit(transform.scale(image.load(f"Resources/palette/Palette{curPallate}.png"), (145, 145)),palleteRect)
    # the hover effect ######
    hover.createHover()

       
    screen.set_clip(canvasRect)

    perfect = keys[K_LSHIFT] == 1 or keys[K_RSHIFT] == 1
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type==KEYDOWN:
            if tool == "Text":# only text gets impacted by
                msg=textTool.handleKeystrokes(e,msg)
              
        if toolClass == 2 or toolClass == 1 : # for shape or brush class
            size = min(size, 10)

        if e.type == MOUSEBUTTONUP:
            if toolsClassName[toolClass] == "edit" and e.button == 3:
                copy = canvasSurface.copy()      
            if(toolClass == 2 or toolClass == 1) and (e.button == 1 or e.button == 3): # for brush class
                cover.fill(backgroundCol)
                copy = canvasSurface.copy()

        if e.type == MOUSEBUTTONDOWN: 
            if canvasRect.collidepoint(mx,my):
                canvas.canvasChanged()
        # for something you want the event to be triggered as soon as mouse is clicked
            if e.button==1: # tool selection
                    print(str(mx) + "," + str(my))
                    for i in range(6):
                        if toolBoxRect[i].collidepoint(mx,my):
                            tool = toolsName[toolClass][i]
                            screen.set_clip()  #unlock screen
                            renderToolbox(toolClass) #redraw selection
                            draw.rect(screen,(0,255,0),toolBoxRect[i],2)
                            screen.set_clip(canvasRect)
                            
                    if toolBoxClassBackRect.collidepoint(mx,my): #for next tool class
                        if toolsClassName[toolClass] == "edit":
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
                        if toolsClassName[toolClass] == "edit":
                            screen.blit(copy,(canvasRect))
                        toolClass += 1 
                        toolClass = min(len(toolsName)-1,toolClass)
                        tool = toolsName[toolClass][0]

                        screen.set_clip()  #unlock screen
                        renderToolbox(toolClass) #redraw selection
                        draw.rect(screen,(0,255,0),toolBoxRect[0],2)
                        tool = toolsName[toolClass][0]
                        screen.set_clip(canvasRect)
                        if  tool == "Stamp_Brush":
                            first = False #save original position of mouse to track clone
                            saved = False # track if clone has been initiated

                    toolbar.checkToolbar()
                    if clearRect.collidepoint(mx,my):
                        canvas.clear()
                    if palleteRect.collidepoint(mx,my):
                        col = basicTool.eyedrop()
                    if palleteNextRect.collidepoint(mx,my):
                        curPallate += 1
                        curPallate = min(curPallate, maxPallate)
                    if palleteBackRect.collidepoint(mx,my):
                        curPallate-=1
                        curPallate = max(curPallate, 1)    
                    if tool == "Text" or toolsClassName[toolClass] == "shape" or toolsClassName[toolClass] == "edit": 
                        cover.fill(backgroundCol)
                        copy = canvasSurface.copy() 
                           
            if canvasRect.collidepoint(mx,my):
                if e.button==1: 
                    startx,starty = e.pos
                    #polygon tool
                    if tool == "Polygon_Shape" or tool == "Polygon_Shape_Filled":
                        draw.circle(screen,(0,0,0),(mx,my),1)
                        polylist.append((mx,my))
                    if tool!="Polygon_Shape" and tool != "Polygon_Shape_Filled":
                        polylist=[]
                    #text tool
                    if tool=="Text" and canvasRect.collidepoint(mx,my):
                        textTool.text(col,msg,mx,my,size)
                        msg = ""
                    #toggle setting
                    if tool == "Sticky_Surface":
                        highlighter.toggleSticky()
                        print (highlighter.sticky)
                    if tool == "alpha":
                         if alpha:
                            alpha = False
                            cover.set_alpha(255)
                         else:
                            alpha = True
                            cover.set_alpha(55)
                         print(alpha)
                    if tool == "Spray_design":
                        if spraydesign==1:
                            spraydesign = 2
                            time.wait(10)
                        else:
                            spraydesign = 1
                            time.wait(10)
                    
                    
            if e.button == 4:
                size = min(20, size +1)
            if e.button == 5:
               size = max(1, size -1)              
            if  e.button == 3 and e.button != 4 and e.button != 5:
                startx,starty = e.pos
                if len(polylist) > 2:
                    if tool == "Polygon_Shape":
                        shapes.polygon(polylist,col, 1,size)            
                        polylist = []
                    if tool == "Polygon_Shape_Filled":
                        shapes.polygon(polylist,col, 0,size)            
                        polylist = []
                    
                if toolsClassName[toolClass] == "edit":
                    copy = canvasSurface.copy() 
                    time.wait(100)

                if tool =="Fill_Bucket":
                    basicTool.fill((randint(0,255),randint(0,255),randint(0,255)))
                if tool == "Eraser":
                    basicTool.fill(backgroundCol)
                    
                if tool == "Stamp_Brush":
                    cspdx,cspdy=mx,my
                    first = True
                    saved = True

                if tool=="Move":
                    screen.blit(copy,(canvasRect))  
                    draw.rect(screen,backgroundCol,(croprect))                          
                    screen.blit(cropselected,(mx-cx/2,my-cy/2))
                    croprect=Rect(mx-cx/2,my-cy/2,cx,cy)                                           
                    
                if tool=="Copy":
                    screen.blit(copy,(canvasRect))
                    screen.blit(cropselected,(mx-cx/2,my-cy/2))
                    
                if tool=="Crop":
                    screen.blit(copy,(canvasRect))
                    draw.rect(screen,backgroundCol,canvasRect)
                    screen.blit(cropselected,(croprect))
                    copy = canvasSurface.copy()
                               
                if tool=="Rotate":
                    screen.blit(copy,(canvasRect))  
                    draw.rect(screen,backgroundCol,(croprect))
                    cropselected=transform.rotate(cropselected,90)
                    screen.blit(cropselected,(croprect))   
                   
                if tool =="Flip_Vertical":
                    screen.blit(copy,(canvasRect))  
                    draw.rect(screen,backgroundCol,(croprect))
                    cropselected=transform.flip(cropselected, False, True)
                    screen.blit(cropselected,(croprect))   
                    
                if tool =="Flip_Horizontal":
                    screen.blit(copy,(canvasRect))  
                    draw.rect(screen,backgroundCol,(croprect))
                    cropselected=transform.flip(cropselected, True, False)
                    screen.blit(cropselected,(croprect))   
                
    if tool == "Text"  : # Text reblit old screen + text
        screen.blit(copy,canvasRect)
    x,y=mx,my
    #when cursor hovers over selected tools highlight  by blitting on tool cover and then redraw tools
    if canvasRect.collidepoint(mx,my):
        #for some things it is better to track when the mouse is down
        if mb[0]==1: 
            # tools 
            if tool=="Pencil":
                basicTool.pencil(col, (oldmx, oldmy))
            if tool == "Eraser":
                brush.circle(backgroundCol,size)
            if tool =="Fill_Bucket":
                basicTool.fill(col)
                
            if tool == "Eyedrop":
                col = basicTool.eyedrop()
            if tool == "Smudge":
                basicTool.tonechanger(1, canvasRect, size)

            # shapes
            if tool == "Circle_Shape":
                shapes.ellipse(copy, col, 1, canvasRect,(mx,my,startx,starty), perfect, size)
            if tool == "Square_Shape":
                shapes.rect(copy, col, 1, canvasRect, (mx,my,startx,starty), perfect, size)
            if tool == "Line_Shape":
                shapes.line(copy, col, canvasRect, (mx,my,startx,starty), size)
            
            # brushes
            if tool == "Explosion_Brush":
                brush.explosion(col,size)
            if tool == "Circle_Brush":
                highlighter.circle(col,size)
            if tool == "Square_Brush":
                highlighter.rect(col,size)
            if tool == "Color_Masher":
                brush.colormasher(size*5,canvasRect)
                copy = canvasSurface.copy()
            if tool == "Line_Brush":
                highlighter.line((oldmx,oldmy),col,size) 
            # for highlighter blit copy          
            if toolClass == 2 : 
                screen.blit(copy,canvasRect)
                screen.blit(cover,(0,0))      
                
            # sprays
            if tool == "Stamp_Brush":
                if first:
                    sx,sy=mx,my
                    first=False
                if saved:
                    clonestamp((cspdx,cspdy),(mx-sx,my-sy),size)
            if tool == "Circle":
                spray.sprayCircle(1,spraySpeed,size,spraydesign,col)
            if tool == "Square":
                spray.spraySquare (1,spraySpeed,size,spraydesign,col)
            if tool == "Rain":
                spray.rainSquare(1,spraySpeed,size,spraydesign,col)
            #if tool == "Populater":
            if tool == "Spray_speed":
               spraySpeed+=1

            #edit class
            if toolsClassName[toolClass] == "edit":
                angle=0
                screen.blit(copy,(canvasRect))    
                croprect=Rect(startx,starty,mx-startx,my-starty)                
                croprect.normalize()
                cropselected=screen.subsurface(croprect).copy()
                draw.rect(screen,(0,0,0),croprect,1)
                cx,cy=cropselected.get_size()
                
        #tool right click
        if mb[2]==1:
            if tool=="Pencil":
                basicTool.pencil((randint(0,255),randint(0,255),randint(0,255)), (oldmx,oldmy))
            if(tool == "Eyedrop"):
                col = (randint(0,255),randint(0,255),randint(0,255))
            if tool == "Smudge":
                basicTool.tonechanger(-1, canvasRect, size)
            # shapes right click
            if tool == "Circle_Shape":
                shapes.ellipse(copy, col,0, canvasRect, (mx,my,startx,starty), perfect, size)
            if tool == "Square_Shape":
                shapes.rect(copy, col, 0, canvasRect, (mx,my,startx,starty), perfect, size)
            if tool == "Line_Shape":
                shapes.aaline(copy,col,canvasRect, (mx,my,startx,starty))
            # brush right click
            if tool == "Circle_Brush":
                highlighter.circle((randint(0,255),randint(0,255),randint(0,255)),size)
            if tool == "Square_Brush":
                highlighter.rect((randint(0,255),randint(0,255),randint(0,255)),size)
            if tool == "Explosion_Brush":
                brush.explosion((randint(0,255),randint(0,255),randint(0,255)),size)
            if tool == "Line_Brush":
                highlighter.line((oldmx,oldmy),(randint(0,255),randint(0,255),randint(0,255)),size) 
            if toolClass == 2  : # for brushes blit copy
                screen.blit(copy,canvasRect)
                screen.blit(cover,(0,0))
            
            # spray class
            if tool == "Circle":
                spray.sprayCircle(1,spraySpeed,size,spraydesign,(randint(0,255),randint(0,255),randint(0,255)))
            if tool == "Square":
                spray.spraySquare (1,spraySpeed,size,spraydesign,(randint(0,255),randint(0,255),randint(0,255)))
            if tool == "Rain":
                spray.rainSquare(1,spraySpeed,size,spraydesign,(randint(0,255),randint(0,255),randint(0,255)))
           
            if tool == "Spray_speed":
               spraySpeed=max(speed-1,1)            
                       
    oldmx,oldmy,=mx,my 
    if tool == "Text" and canvasRect.collidepoint(mx,my):
        copy = canvasSurface.copy() 
        textTool.text(col,msg,mx,my,size)          
      
    display.flip()
quit()
