from pygame import *

class Hover(object):
    rects = []
    def __init__(self, screen):
        super(Hover, self).__init__()
        self.screen = screen

    def addHover(rect):
        Hover.rects.append(rect)

    def createHover(self):
        mx,my = mouse.get_pos()
        for rect in Hover.rects:
            if rect.collidepoint(mx,my): #clear box
                draw.rect(self.screen,(0,255,0),rect,1)
            else:
                draw.rect(self.screen,(0,0,0),rect,1)
        