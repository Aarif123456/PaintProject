from pygame import *


class CloneStamp(object):
    def __init__(self, surface):
        super().__init__()
        self.surface = surface
        self.first = False  # save original position of mouse to track clone
        self.saved = False  # track if clone has been initiated
        self.cd = 0, 0
        self.start = 0, 0

    def reset(self):
        self.first = False  # save original position of mouse to track clone
        self.saved = False  # track if clone has been initiated

    def save(self):
        self.cd = mouse.get_pos()
        self.first = True
        self.saved = True

    def clone(self, size):
        mx, my = mouse.get_pos()
        if self.first:
            self.start = mx, my
            self.first = False
        if self.saved:
            sx, sy = self.start
            self.stamp((mx - sx, my - sy), size)

    def stamp(self, dif, size):
        difx, dify = dif
        cdx, cdy = self.cd
        mx, my = mouse.get_pos()
        if min(cdx + difx, cdy + dify) > 0:
            clonedrect = Rect(cdx + difx, cdy + dify, size, size)
            cloned = self.surface.subsurface(clonedrect).copy()
            cloned.convert()
            self.surface.blit(cloned, (mx, my))
