#summon tool
from pygame import *
from random import*
import os

#categoryNames[c].replace(" ", "_").replace(".","_")
screen = display.set_mode((1200,675))
screen.fill((255,255,255))
tool="stamp"
#predefining all variable needed
stampnum=0 #starting stamp is 0
stampCategory=0 #first category is one
size=1    #size of stamp

#making all the list I need
stampImages={} #store all of the images
stampnames=[] # list of names
listdir=[] #hold files in folder

#set up rects needed
canvasrect=Rect(300,100,700,500)
draw.rect(screen,(0,0,0),canvasrect,1)
nextrect=Rect(1200-100,120,100,100)
draw.rect(screen,(255,0,255),nextrect)
prevrect=Rect(1200-100,320,100,100)
draw.rect(screen,(255,0,255),prevrect)

#get name of each category of pirates
categoryNames=open('names.txt','r').read().splitlines()

for c in range (25):#to get all stamps
  if c<10:
    categoryFolderPath = '0'+ str(c)
  else:
    categoryFolderPath=str(c)
  #all spaces are represented as underscore on folders and files
  categoryFolderPath += "_" +categoryNames[c].replace(" ", "_")
  print(categoryFolderPath)
  listdir=os.listdir(categoryFolderPath) #search for files in stampCategory folder
  listdir.sort() #because listdir does not guarantee order

  stampimage =[] #list to hold all the stamps
  for file in listdir:
    if file.endswith('.png'):#get only the picture
      stampimage.append(image.load(categoryFolderPath+'/'+file))
  stampImages[categoryNames[c]] = stampimage #store images in dictionary

  #get name of each character and store into list
  stampname=open(categoryFolderPath + '/names.txt','r').read().splitlines()
  stampnames.append(stampname)

     
'''for i in range(len(stampimages)):#loading screen
    draw.rect(screen,(0,0,0),(0,0,200,380))
    screen.blit(stampimages[i],(0,0))
    time.wait(500)
    display.flip()'''


#stampcopy=transform.smoothscale#make all stamps = ratio maybe like a square or something or keep all stamp ratio same using python
    
running =True
mx,my = mouse.get_pos()
while running:                       
    for e in event.get():       
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN:
           if e.button ==1:
               stampname=stampnames[stampCategory][stampnum]
               print("stampCategory: " + categoryNames[stampCategory] +"\n Character Name : " + stampname +"\n")
               if nextrect.collidepoint(mx,my)==True:
                   if stampCategory <24:
                       stampCategory+=1 #make new and oldcategory variable later new catergory gets added
                       
               if prevrect.collidepoint(mx,my)==True:
                    if stampCategory >0:
                        stampCategory-=1
               if canvasrect.collidepoint(mx,my):
                    screen.blit(stampImages[categoryNames[stampCategory]][stampnum],(mx-100,my-190))
                        
           if e.button == 4:
               size += 1
           if e.button == 5:
               if size!=1:               
                   size -= 1 
    mb = mouse.get_pressed()    
    mx,my = mouse.get_pos()
    draw.rect(screen,(0,0,0),(0,0,200,300))                  
    screen.blit(stampImages[categoryNames[stampCategory]][stampnum],(0,0))
    
     
    oldmx,oldmy,=mx,my
    display.flip()

quit()
