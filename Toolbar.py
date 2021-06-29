from pygame import *
from PaintHelper import addImage 
from Hover import Hover

class Toolbar(object):
    menuPath = "Resources/design/menubar/"
    
    def __init__(self, surface):
        super().__init__()
        self.surface = surface
        # Related lists
        self.menuRect = []
        self.menuNames = []
        self.menuFunctions = []

    def addFunction(self, name, func):
        self.menuRect.append(Rect(len(self.menuRect)*30+15,0,25,25))
        self.menuNames.append(name)
        self.menuFunctions.append(func)
        Hover.addHover(self.menuRect[-1])
        addImage(self.surface, (25, 25), self.menuRect[-1], f"{Toolbar.menuPath}{name}.png")

    def checkToolbar(self):
        mx,my=mouse.get_pos()
        for i in range(len(self.menuRect)):
            if self.menuRect[i].collidepoint(mx,my):
                self.menuFunctions[i]()