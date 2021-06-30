from pygame import *


class BasicTool(object):
    def __init__(self, surface):
        super(BasicTool, self).__init__()
        self.surface = surface

    def pencil(self, col: Color, old: tuple):
        mx, my = mouse.get_pos()
        oldmx, oldmy = old
        draw.line(self.surface, col, (oldmx, oldmy), (mx, my), 3)

    def fill(self, col: Color):
        mx, my = mouse.get_pos()
        fillpos = [(mx, my)]
        oldcol = self.surface.get_at((mx, my))
        if oldcol != col:
            while len(fillpos) > 0:
                while len(fillpos) > 0:
                    x, y = fillpos.pop()
                    if self.surface.get_at((x, y)) == oldcol:
                        self.surface.set_at((x, y), col)
                        fillpos += [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

    def eyedrop(self):
        mPos = mouse.get_pos()
        return tuple(self.surface.get_at(mPos))

    def tonechanger(self, tone, canvasRect, size):
        x, y = mouse.get_pos()
        s = min(10, size)
        for i in range(-s * 3, s * 3):
            for j in range(-s * 3, s * 3):
                csx, csy = x + i, y + j
                if canvasRect.collidepoint(csx, csy):
                    tcol = self.surface.get_at((csx, csy))
                    r = min(max(0, tcol[0] - tone), 255)
                    g = min(max(0, tcol[1] - tone), 255)
                    b = min(max(0, tcol[2] - tone), 255)
                    ncol = (r, g, b)
                    self.surface.set_at((csx, csy), ncol)
