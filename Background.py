from pygame import *
from PaintLayout import PaintLayout
from Hover import Hover
import os
import re

class Background(object):
    SHIPS = 1
    ISLANDS = 0
    NAME_FINDER = re.compile(r"(^(?:\d*_)?(?P<fileName>.*)(?:\.png)$)")
    
    def __init__(self, surface, canvasRect, backgroundCol):
        super().__init__()

        self.surface = surface
        self.canvasRect = canvasRect
        self.backgroundCol = backgroundCol

        self.backgroundRect = Rect(795,183,204,144) 
        self.backgroundTextRect = Rect(816,152,163,30)
        self.backgroundNextRect = Rect(980,152,35,30)
        self.backgroundBackRect = Rect(780,152,35,30)

        draw.rect(surface,(0,0,0),self.backgroundRect, 1)
        draw.rect(surface,(0,0,0),self.backgroundTextRect, 1)
        PaintLayout.createNextBox(surface, self.backgroundNextRect)
        PaintLayout.createBackBox(surface, self.backgroundBackRect)

        self.backgroundShipRect = Rect(780,121,117,30)
        self.backgroundIslandRect = Rect(898,121,117,30)

        PaintLayout.drawText(surface, "Ships", (0,0,0), self.backgroundShipRect, 30)
        PaintLayout.drawText(surface, "Islands", (0,0,0), self.backgroundIslandRect, 30)
        Hover.addHover(self.backgroundShipRect)
        Hover.addHover(self.backgroundIslandRect)
        self.selectedCategory = Background.SHIPS
        self.selectedImage = 0 

        self.shipImages = []
        self.islandImages = []

    def getImages(location)->list:
        images = []
        files = os.listdir(location) 
        files.sort() # because listdir does not guarantee order
        for file in files:
            if file.endswith(".png"):#g et only the picture
                name = Background.NAME_FINDER.match(file).group('fileName').replace("_", " ")
                images.append((image.load(f"{location}/{file}"), name))

        return images

    def blitImage(screen, rect, img):
        imgSize = (rect.width, rect.height)
        screen.blit(transform.smoothscale(img, imgSize), (rect.x,rect.y))

    def setup(self):
        self.shipImages = Background.getImages("Resources/background/Ships")
        self.islandImages = Background.getImages("Resources/background/Islands")
        self.curImage = self.shipImages[0]


    # Make selected box yellow
    def renderSelected(self):
        if self.selectedCategory ==  Background.SHIPS:
            draw.rect(self.surface,(0,0,0),self.backgroundIslandRect, 1)
            draw.rect(self.surface,(255,255,0),self.backgroundShipRect, 1)
        else:
            draw.rect(self.surface,(255,255,0),self.backgroundIslandRect, 1)
            draw.rect(self.surface,(0,0,0),self.backgroundShipRect, 1)


    def renderImage(self):
        draw.rect(self.surface, self.backgroundCol, self.backgroundRect) 
        Background.blitImage(self.surface, self.backgroundRect, self.curImage[0])

    def renderText(self): 
        PaintLayout.drawText(self.surface, self.curImage[1], (0,0,0), self.backgroundTextRect, 20)

    def render(self):
        self.renderImage()
        self.renderSelected()
        self.renderText()

    def curImageList(self):
        return self.shipImages if self.selectedCategory ==  Background.SHIPS else self.islandImages

    def handle(self):
        mx,my=mouse.get_pos()
        curList = self.curImageList()
        if self.backgroundShipRect.collidepoint(mx,my)==True:
            self.selectedCategory = Background.SHIPS
        elif self.backgroundIslandRect.collidepoint(mx,my)==True:
            self.selectedCategory = Background.ISLANDS
        elif self.backgroundNextRect.collidepoint(mx,my)==True:
            self.selectedImage += 1
        elif self.backgroundBackRect.collidepoint(mx,my)==True:
            self.selectedImage += len(curList)-1
        elif self.backgroundRect.collidepoint(mx,my)==True:
            Background.blitImage(self.surface, self.canvasRect, self.curImage[0])
        curList = self.curImageList()
        self.selectedImage %= len(curList)
        self.curImage = curList[self.selectedImage]




