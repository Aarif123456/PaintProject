from pygame import *

class Canvas(object):
    def __init__(self, surface, canvasRect):
        super(Canvas, self).__init__()
        self.canvasRect = canvasRect
        self.surface = surface
        draw.rect(self.surface,(0,0,0),canvasRect,3)
        draw.rect(self.surface,(255,255,255),canvasRect)
        self.undoList,self.redoList=[],[]

    def undo(self):
        if len(self.undoList)>0:
            self.redoList.append(self.surface.subsurface(self.canvasRect).copy())
            self.surface.blit(self.undoList.pop(),self.canvasRect)     

    def redo(self):
        if len(self.redoList)>0:
            self.undoList.append(self.surface.subsurface(self.canvasRect).copy())
            self.surface.blit(self.redoList.pop(),self.canvasRect)

    def clear(self):
        draw.rect(self.surface,(0,0,0),self.canvasRect,3)
        draw.rect(self.surface,(255,255,255),self.canvasRect)
        
    def canvasClicked(self):
        self.undoList.append(self.surface.subsurface(self.canvasRect).copy())
        self.redoList=[]
