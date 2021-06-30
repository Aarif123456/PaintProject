from pygame import *
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
from Palette import Palette
from CloneStamp import CloneStamp
from BasicToolHandler import BasicToolHandler
from BrushHandler import BrushHandler
from HighlighterHandler import HighlighterHandler
from Stamp import Stamp
from Background import Background

#-------------------------------------------------------------------------
backgroundCol = Color(255,255,255)
# Current color - start off with random color
col = Color(createRandomColor())
paintLayout = PaintLayout()
screen,cover = paintLayout.screen,paintLayout.cover

#-------------------------------------------------------------------------
# Set up logo 
paintLayout.createLogo("Resources/design/others/logo.png")
# set up canvas has to be of the ratio 680:480 -> 17:12 
# for background image to scale properly
canvasRect = Rect(230,120,510,360) 
canvas = Canvas(screen, canvasRect)
canvas.createClearBox(backgroundCol)

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
PaintLayout.createNextBox(screen, toolBoxClassNextRect)
PaintLayout.createBackBox(screen, toolBoxClassBackRect)

#--------------set up toolbox------------

toolBoxPath = "Resources/tools/" # path for all types of tools
# types of tools for display
toolsClassName = ["tools","shape","brush","spray","edit", "other"] 
toolsName=  [["Pencil","Eraser","Fill_Bucket","Text","Eyedrop","Smudge"],
             ["Circle_Shape","Square_Shape","Line_Shape","Explosion_Brush","Polygon_Shape","Polygon_Shape_Filled"],
             ["Circle_Brush","Square_Brush","Color_Masher","Line_Brush","Sticky_Surface","alpha"],
             ["Circle","Square","Rain","Stamp_Brush","Spray_design","Spray_speed"],
             ["Move","Copy","Crop","Rotate","Flip_Vertical","Flip_Horizontal"],
             ["Stamp"]
            ]

toolBoxRect =[]
for i in range (len(toolsName[0])):
    # For two columns
    x = 10 if i%2 == 0 else 98
    y=(i//2)*80+215   
    toolBoxRect.append(((Rect(x,y,80,70))))

def renderToolbox(toolClassNum):
    for i in range (len(toolsName[toolClassNum])):
        draw.rect(screen,backgroundCol,toolBoxRect[i])
        draw.rect(screen,(0,0,0),toolBoxRect[i],2)
        addImageNonSmooth(screen, (80, 70), toolBoxRect[i], f"{toolBoxPath}{toolsClassName[toolClassNum]}/{i+1}_{toolsName[toolClassNum][i]}.png" )

toolBoxTextRect = Rect(10,470,175,34)
toolboxTextInfoRect = Rect(10,505,180,140)

def renderToolInfoText(x,y,toolClassNum,toolName):
    # for the selected tool box box
    toolBoxTextOutlineRect = Rect(5,470,185,34)
    draw.rect(screen,backgroundCol,toolBoxTextOutlineRect) # fill up box
    draw.rect(screen,(0,0,0),toolBoxTextOutlineRect,1) # add outline
    hover = False
    # clear text info box
    toolboxTextInfoOutlineRect = Rect(5,505,185,140)
    draw.rect(screen,backgroundCol,toolboxTextInfoOutlineRect) 
    draw.rect(screen,(0,0,0),toolboxTextInfoOutlineRect,1)
    if toolName == "Stamp":
        toolClassNum = 5
    curTool = toolsName[toolClassNum].index(toolName)

    for i in range(len(toolsName[toolClassNum])):
        if toolBoxRect[i].collidepoint(x,y):
            curTool = i
            break

    PaintLayout.drawText(screen, open(toolBoxPath+toolsClassName[toolClassNum]+ "/"+str(curTool+1)+"_"+ toolsName[toolClassNum][curTool]+".txt").read().splitlines()[0], (0,0,0), toolboxTextInfoRect,  17)
    toolName = toolsName[toolClassNum][curTool]
    toolText = toolName.replace("_", " ")
    PaintLayout.drawText(screen,toolText, (0,255,0), toolBoxTextRect, 25)

# palette box
palette = Palette(screen, backgroundCol)

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


# stamp box
stamp = Stamp(screen, canvasRect, backgroundCol)
stamp.setup()

#background box
# the actual background has to be in rect with ratio 17:12
background = Background(screen, canvasRect, backgroundCol)
background.setup()

#music box
musicNameRect = Rect(810,10,180,25)
draw.rect(screen,(0,0,0),musicNameRect ,1)
#play stop box 
musicPlayRect = Rect(815,36,84,43)
musicStopRect = Rect(900,36,84,43)
Hover.addHover(musicPlayRect)
Hover.addHover(musicStopRect)

#next back 
musicNextRect = Rect(900,80,84,25)
musicBackRect = Rect(815,80,84,25)
PaintLayout.createNextBox(screen, musicNextRect)
PaintLayout.createBackBox(screen, musicBackRect)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------
basicTool = BasicTool(screen)
brush = Brush(screen)
highlighter = Brush(cover) 
shapes = Shapes(screen)
spray = Spray(screen)
hover = Hover(screen)

spraySpeed = 10
spraydesign = 1 # by default paint will spray in shape of a circle

cloneStamp = CloneStamp(screen)  

#Initialize text
textTool = TextTool(screen)
# TODO: REMOVE
# textTool.text((255,0,0),"Back",22,160, 25)
# textTool.text((0,255,0),"Next",107,160, 25) 

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

perfect = False
startx,starty = 0,0
polylist = []
msg=""        
basicToolHandler = BasicToolHandler(backgroundCol, canvasRect, basicTool)
brushHandler = BrushHandler(backgroundCol, canvasRect, brush)
highlighterHandler = HighlighterHandler(cover, canvasRect, highlighter)
while running:
    mx,my = mouse.get_pos()
    mb = mouse.get_pressed()
    keys = key.get_pressed()
    screen.set_clip()
    # set text to current color
    PaintLayout.drawText(screen, "Current Color", col, currentColorRect, 20)
    renderSizeRect(size) # fill rectangle depending on size
    renderToolInfoText(mx,my,toolClass,tool)
    palette.renderPalette()
    stamp.render()
    background.render()
    # the hover effect ######
    hover.createHover()
    screen.set_clip(canvasRect)

    perfect = keys[K_LSHIFT] == 1 or keys[K_RSHIFT] == 1
    events = event.get()
    basicToolHandler.handle(tool, col, size, copy, events)
    brushHandler.handle(tool, col, size, copy, events)
    highlighterHandler.handle(tool, col, size, copy, events)
    if toolClass == 2 or toolClass == 1 : # for shape or brush class
        size = min(size, 10)

    for e in events:
        if e.type == QUIT:
            running = False
        elif e.type == KEYDOWN:
            if tool == "Text":# only text gets impacted by
                msg=textTool.handleKeystrokes(e,msg)      

        elif e.type == MOUSEBUTTONUP:
            if toolsClassName[toolClass] == "edit" and e.button == 3:
                copy = canvasSurface.copy()     
            # for shape or brush class 
            if(toolClass == 2 or toolClass == 1) and (e.button == 1 or e.button == 3): 
                cover.fill(backgroundCol)
                copy = canvasSurface.copy()

        elif e.type == MOUSEBUTTONDOWN: 
            if canvasRect.collidepoint(mx,my):
                canvas.canvasChanged()
        # for something you want the event to be triggered as soon as mouse is clicked
            if e.button == 1: # tool selection
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
                    toolClass = max (0,toolClass-1)
                    tool = toolsName[toolClass][0]
                    #with the rest of the rendering make it green if selected or hover
                    screen.set_clip()  #unlock screen
                    renderToolbox(toolClass) #redraw selection
                    draw.rect(screen,(0,255,0),toolBoxRect[0],2)
                    tool = toolsName[toolClass][0]
                    screen.set_clip(canvasRect)
                    if tool == "Stamp_Brush":
                        cloneStamp.reset()
                        
                    
                elif toolBoxClassNextRect.collidepoint(mx,my): #for next tool class
                    if toolsClassName[toolClass] == "edit":
                        screen.blit(copy,(canvasRect))
                    toolClass = min(len(toolsName)-1,toolClass+1)
                    tool = toolsName[toolClass][0]
                    screen.set_clip()  # unlock screen
                    renderToolbox(toolClass) # redraw selection
                    draw.rect(screen,(0,255,0),toolBoxRect[0],2)
                    tool = toolsName[toolClass][0]
                    screen.set_clip(canvasRect)
                    if tool == "Stamp_Brush":
                        cloneStamp.reset()

                toolbar.checkToolbar()
                canvas.checkClear()
                palette.checkPalette(col)
                tool = stamp.handle(tool)
                background.handle()
                # text tool
                if tool == "Text":
                    textTool.text(col,msg,mx,my,size)
                    msg = ""

                # TODO: Create filler and add tool and classes that cause fill
                if tool == "Text" or toolClass == 1 or toolsClassName[toolClass] == "edit": 
                    cover.fill(backgroundCol)
                    copy = canvasSurface.copy() 
                           
            if canvasRect.collidepoint(mx,my):
                if e.button == 1: 
                    startx,starty = e.pos
                    #polygon tool
                    if tool == "Polygon_Shape" or tool == "Polygon_Shape_Filled":
                        draw.circle(screen,(0,0,0),(mx,my),1)
                        polylist.append((mx,my))
                    elif tool != "Polygon_Shape" and tool != "Polygon_Shape_Filled":
                        polylist=[]
                    #toggle setting
                    if tool == "Spray_design":
                        spraydesign = 2 if spraydesign == 1 else 1
                        time.wait(10)
                    
            if e.button == 4:
                size = min(20, size +1)
            elif e.button == 5:
               size = max(1, size -1)              
            elif e.button == 3:
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
                                    
                if tool == "Stamp_Brush":
                    cloneStamp.save()

                elif tool=="Move":
                    screen.blit(copy,(canvasRect))  
                    draw.rect(screen,backgroundCol,(croprect))                          
                    screen.blit(cropselected,(mx-cx/2,my-cy/2))
                    croprect=Rect(mx-cx/2,my-cy/2,cx,cy)                                           
                    
                elif tool=="Copy":
                    screen.blit(copy,(canvasRect))
                    screen.blit(cropselected,(mx-cx/2,my-cy/2))
                    
                elif tool=="Crop":
                    screen.blit(copy,(canvasRect))
                    draw.rect(screen,backgroundCol,canvasRect)
                    screen.blit(cropselected,(croprect))
                    copy = canvasSurface.copy()
                               
                elif tool=="Rotate":
                    screen.blit(copy,(canvasRect))  
                    draw.rect(screen,backgroundCol,(croprect))
                    cropselected=transform.rotate(cropselected,90)
                    screen.blit(cropselected,(croprect))   
                   
                elif tool =="Flip_Vertical":
                    screen.blit(copy,(canvasRect))  
                    draw.rect(screen,backgroundCol,(croprect))
                    cropselected=transform.flip(cropselected, False, True)
                    screen.blit(cropselected,(croprect))   
                    
                elif tool =="Flip_Horizontal":
                    screen.blit(copy,(canvasRect))  
                    draw.rect(screen,backgroundCol,(croprect))
                    cropselected=transform.flip(cropselected, True, False)
                    screen.blit(cropselected,(croprect))   
    if tool == "Text"  : # Text reblit old screen + text
        screen.blit(copy,canvasRect)            
    x,y = mx,my
    # when cursor hovers over selected tools highlight  by blitting on tool cover and then redraw tools
    if canvasRect.collidepoint(mx,my):
        # for some things it is better to track when the mouse is down
        if mb[0] == 1: 

            # shapes
            if tool == "Circle_Shape":
                shapes.ellipse(copy, col, 1, canvasRect,(mx,my,startx,starty), perfect, size)
            elif tool == "Square_Shape":
                shapes.rect(copy, col, 1, canvasRect, (mx,my,startx,starty), perfect, size)
            elif tool == "Line_Shape":
                shapes.line(copy, col, canvasRect, (mx,my,startx,starty), size)
            
            # brushes
            if tool == "Color_Masher":
                brush.colormasher(size*5,canvasRect)
                copy = canvasSurface.copy()
            # for highlighter blit copy
            if toolClass == 2 : 
                screen.blit(copy,canvasRect)
                screen.blit(cover,(0,0))      
           
                
            # sprays
            if tool == "Stamp_Brush":
                cloneStamp.clone(size)
            elif tool == "Circle":
                spray.sprayCircle(1,spraySpeed,size,spraydesign,col)
            elif tool == "Square":
                spray.spraySquare (1,spraySpeed,size,spraydesign,col)
            elif tool == "Rain":
                spray.rainSquare(1,spraySpeed,size,spraydesign,col)
            #elif tool == "Populater":
            elif tool == "Spray_speed":
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
                
        # right click held down
        if mb[2] == 1:
            # shapes right click
            if tool == "Circle_Shape":
                shapes.ellipse(copy, col,0, canvasRect, (mx,my,startx,starty), perfect, size)
            elif tool == "Square_Shape":
                shapes.rect(copy, col, 0, canvasRect, (mx,my,startx,starty), perfect, size)
            elif tool == "Line_Shape":
                shapes.aaline(copy,col,canvasRect, (mx,my,startx,starty))
            if toolClass == 2  : # for brushes blit copy
                screen.blit(copy,canvasRect)
                screen.blit(cover,(0,0))
            # spray class
            if tool == "Circle":
                spray.sprayCircle(1,spraySpeed,size,spraydesign,createRandomColor())
            elif tool == "Square":
                spray.spraySquare (1,spraySpeed,size,spraydesign,createRandomColor())
            elif tool == "Rain":
                spray.rainSquare(1,spraySpeed,size,spraydesign,createRandomColor())
            elif tool == "Spray_speed":
               spraySpeed=max(speed-1,1)            
                       
    oldmx,oldmy = mx,my 
    if tool == "Text" and canvasRect.collidepoint(mx,my):
        copy = canvasSurface.copy() 
        textTool.text(col,msg,mx,my,size)          
      
    display.update()
quit()
