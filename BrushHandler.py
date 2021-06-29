from pygame import *
from PaintHelper import createRandomColor

class BrushHandler(object):
    def __init__(self,  backgroundCol, canvasRect, brush):
        super().__init__()
        self.backgroundCol = backgroundCol
        self.brush = brush
        self.canvasRect = canvasRect

    def handle(self, tool, col, size, _copy, _events):
        mx,my = mouse.get_pos()
        mb = mouse.get_pressed()
        onCanvas = self.canvasRect.collidepoint(mx,my)
        if onCanvas:
            if mb[0] == 1: # Mouse left-click currently down
                if tool == "Eraser":
                    self.brush.circle(self.backgroundCol,size)
                if tool == "Explosion_Brush":
                    self.brush.explosion(col,size)    
            # right click held down
            if mb[2] == 1:
                if tool == "Explosion_Brush":
                    self.brush.explosion(createRandomColor(),size)