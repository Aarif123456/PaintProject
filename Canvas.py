from tkinter import Tk, filedialog

from pygame import *

from Hover import Hover
from PaintHelper import addImage


class Canvas(object):
    def __init__(self, surface, rect):
        super(Canvas, self).__init__()
        self.rect = rect
        self.surface = surface
        draw.rect(self.surface, (0, 0, 0), rect, 3)
        draw.rect(self.surface, (255, 255, 255), rect)
        self.undoList, self.redoList = [], []
        self.clearRect = Rect(700, 485, 40, 40)

    def undo(self):
        if len(self.undoList) > 0:
            self.redoList.append(self.surface.subsurface(self.rect).copy())
            self.surface.blit(self.undoList.pop(), self.rect)

    def redo(self):
        if len(self.redoList) > 0:
            self.undoList.append(self.surface.subsurface(self.rect).copy())
            self.surface.blit(self.redoList.pop(), self.rect)

    def clear(self):
        draw.rect(self.surface, (0, 0, 0), self.rect, 3)
        draw.rect(self.surface, (255, 255, 255), self.rect)

    def canvasChanged(self):
        self.undoList.append(self.surface.subsurface(self.rect).copy())
        self.redoList = []

    def openFile(self):
        Tk().withdraw()
        fileFormats = [("Portable Network Graphics", "*.png"),
                       ("Windows Bitmap", "*.bmp"),
                       ("JPEG / JFIF", "*.jpg"),
                       ("CompuServer GIF", "*.gif")]
        file = filedialog.askopenfile(mode="r", title="Load", filetypes=fileFormats)
        if file is not None:
            self.renderImage(file)
            self.canvasChanged()

    def renderImage(self, file):
        canvasSurface = self.surface.subsurface(self.rect)
        addImage(canvasSurface, (self.rect.width, self.rect.height), (0, 0), file.name)

    def saveFile(self):
        Tk().withdraw()
        file = filedialog.asksaveasfile(mode="w", title="Save As", defaultextension=".png")
        if file is not None:
            image.save(self.surface.subsurface(self.rect), file.name)

    def createClearBox(self, backgroundCol):
        draw.rect(self.surface, backgroundCol, self.clearRect, 0)
        Hover.addHover(self.clearRect)
        addImage(self.surface, (40, 40), self.clearRect, "Resources/design/menubar/clear.png")

    def checkClear(self):
        mx, my = mouse.get_pos()
        if self.clearRect.collidepoint(mx, my):
            self.clear()
