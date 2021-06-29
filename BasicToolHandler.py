from pygame import *
from PaintHelper import createRandomColor

class BasicToolHandler(object):
    def __init__(self, backgroundCol, canvasRect, basicTool):
        super(BasicToolHandler, self).__init__()
        self.old = (0,0)
        self.backgroundCol = backgroundCol
        self.basicTool = basicTool
        self.canvasRect = canvasRect

    def handle(self, tool, col, size, _copy, events):
        mx,my = mouse.get_pos()
        mb = mouse.get_pressed()
        onCanvas = self.canvasRect.collidepoint(mx,my)
        oldmx, oldmy = self.old

        for e in events:
            if e.type == MOUSEBUTTONDOWN: 
                if onCanvas:
                    if e.button == 3 and e.button != 4 and e.button != 5:
                        if tool == "Eraser":
                            self.basicTool.fill(self.backgroundCol)
                        elif tool == "Fill_Bucket":
                            self.basicTool.fill(createRandomColor())

        if onCanvas:
            if mb[0] == 1: # Mouse left-click currently down
                if tool == "Pencil":
                    self.basicTool.pencil(col, (oldmx, oldmy))
                elif tool =="Fill_Bucket":
                    self.basicTool.fill(col)
                elif tool == "Smudge":
                    self.basicTool.tonechanger(1, self.canvasRect, size)
            # right click held down
            if mb[2] == 1:
                if tool == "Pencil":
                    self.basicTool.pencil(createRandomColor(), (oldmx,oldmy))
                elif tool == "Smudge":
                    self.basicTool.tonechanger(-1, self.canvasRect, size)   
        self.old = mx,my
        