from pygame import *
from PaintHelper import addImage 
from PaintLayout import PaintLayout

class Palette(object):
    maxPalette = 5
    
    def __init__(self, surface, backgroundCol):
        super(Palette, self).__init__()
        self.surface = surface
        self.backgroundCol = backgroundCol
        self.paletteRect = Rect(412,540,145,145)
        self.paletteNextRect = Rect(412+73,686,72,30)
        self.paletteBackRect = Rect(412,686,72,30)
        draw.rect(surface,(0,0,0),self.paletteRect,1)
        PaintLayout.createNextBox(surface, self.paletteNextRect)
        PaintLayout.createBackBox(surface, self.paletteBackRect)
        self.curPalette = 1

    def renderPalette(self):
        draw.rect(self.surface, self.backgroundCol, self.paletteRect,0)
        addImage(self.surface, (145, 145), self.paletteRect, f"Resources/palette/Palette{self.curPalette}.png")

    def checkPalette(self, col):
        mx,my = mouse.get_pos()
        if self.paletteRect.collidepoint(mx,my):
            col.r,col.g,col.b,col.a = tuple(self.surface.get_at((mx,my)))
        elif self.paletteNextRect.collidepoint(mx,my):
            self.curPalette = min(self.curPalette+1, Palette.maxPalette)
        elif self.paletteBackRect.collidepoint(mx,my):
            self.curPalette = max(self.curPalette-1, 1) 



        