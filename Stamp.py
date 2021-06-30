import os

from pygame import *

from PaintLayout import PaintLayout


class Stamp(object):
    MAX_STAMPS = 25

    def __init__(self, surface, canvasRect, backgroundCol):
        super().__init__()

        self.surface = surface
        self.canvasRect = canvasRect
        self.backgroundCol = backgroundCol

        # get name of each category of pirates
        self.categoryNames = open("Resources/stamps/names.txt", "r").read().splitlines()
        self.stampNum = 0  # starting stamp is 0
        self.stampCategory = 0  # first category is one

        self.stampImages = {}  # store all of the images
        self.stampNames = []  # list of names

        self.stampTextRect = Rect(816, 380, 163, 30)
        self.stampBackRect = Rect(780, 380, 35, 30)
        self.stampNextRect = Rect(980, 380, 35, 30)
        PaintLayout.createNextBox(surface, self.stampNextRect)
        PaintLayout.createBackBox(surface, self.stampBackRect)

        self.stampCategoryTextRect = Rect(816, 349, 163, 30)
        self.stampCategoryBackRect = Rect(780, 349, 35, 30)
        self.stampCategoryNextRect = Rect(980, 349, 35, 30)
        PaintLayout.createNextBox(surface, self.stampCategoryNextRect)
        PaintLayout.createBackBox(surface, self.stampCategoryBackRect)

        self.stampRect = Rect(797, 411, 200, 300)
        draw.rect(surface, (0, 0, 0), self.stampRect, 1)

    def setup(self):
        for c in range(Stamp.MAX_STAMPS):  # to get all stamps
            categoryFolderPath = "Resources/stamps/"
            if c < 10:
                categoryFolderPath += "0" + str(c)
            else:
                categoryFolderPath += str(c)
            # all spaces are represented as underscore on folders and files
            categoryFolderPath += "_" + self.categoryNames[c].replace(" ", "_")
            # search for files in stampCategory folder
            listdir = os.listdir(categoryFolderPath)
            listdir.sort()  # because listdir does not guarantee order

            stampImage = []  # list to hold all the stamps
            for file in listdir:
                if file.endswith(".png"):  # g et only the picture
                    stampImage.append(image.load(f"{categoryFolderPath}/{file}"))
            # store images in dictionary
            self.stampImages[self.categoryNames[c]] = stampImage

            # get name of each character and store into list
            stampName = open(categoryFolderPath + "/names.txt", "r").read().splitlines()
            self.stampNames.append(stampName)

    def getStampName(self):
        return self.stampNames[self.stampCategory][self.stampNum]

    def getStampCategory(self):
        return self.categoryNames[self.stampCategory]

    def getImagePath(self):
        return self.stampImages[self.categoryNames[self.stampCategory]][self.stampNum]

    def renderText(self):
        PaintLayout.drawText(self.surface, self.getStampName(), (0, 0, 0), self.stampTextRect, 20)
        PaintLayout.drawText(self.surface, self.getStampCategory(), (0, 0, 0), self.stampCategoryTextRect, 20)

    def renderImage(self):
        draw.rect(self.surface, self.backgroundCol, self.stampRect)
        self.surface.blit(self.getImagePath(), self.stampRect)

    def render(self):
        self.renderImage()
        self.renderText()

    def handle(self, tool):
        mx, my = mouse.get_pos()
        if self.stampNextRect.collidepoint(mx, my):
            self.stampNum += 1
        elif self.stampBackRect.collidepoint(mx, my):
            self.stampNum += len(self.stampNames[self.stampCategory]) - 1
        elif self.stampCategoryNextRect.collidepoint(mx, my):
            self.stampCategory += 1
            self.stampCategory %= Stamp.MAX_STAMPS
        elif self.stampCategoryBackRect.collidepoint(mx, my):
            self.stampCategory = max(0, self.stampCategory - 1)
        elif self.canvasRect.collidepoint(mx, my) and tool == "Stamp":
            self.surface.blit(self.getImagePath(), (mx - 100, my - 190))
        elif self.stampRect.collidepoint(mx, my):
            tool = "Stamp"
        self.stampNum %= len(self.stampNames[self.stampCategory])
        return tool
