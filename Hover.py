from pygame import *


class Hover(object):
    rects = []

    def __init__(self, screen):
        super(Hover, self).__init__()
        self.screen = screen

    @staticmethod
    def addHover(hoverRect: Rect):
        Hover.rects.append(hoverRect)

    def createHover(self):
        mx, my = mouse.get_pos()
        for hoverRect in Hover.rects:
            if hoverRect.collidepoint(mx, my):  # clear box
                draw.rect(self.screen, (0, 255, 0), hoverRect, 1)
            else:
                draw.rect(self.screen, (0, 0, 0), hoverRect, 1)
