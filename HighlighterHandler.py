from pygame import *

from PaintHelper import createRandomColor


class HighlighterHandler(object):
    def __init__(self, cover, canvasRect, highlighter):
        super().__init__()
        self.highlighter = highlighter
        self.canvasRect = canvasRect
        self.cover = cover
        self.alpha = False
        self.old = (0, 0)

    def handle(self, tool, col, size, _copy, events):
        mx, my = mouse.get_pos()
        mb = mouse.get_pressed()
        onCanvas = self.canvasRect.collidepoint(mx, my)
        oldmx, oldmy = self.old
        for e in events:
            if e.type == MOUSEBUTTONDOWN and e.button == 1:
                if tool == "Sticky_Surface":
                    self.highlighter.toggleSticky()
                if tool == "alpha":
                    self.cover.set_alpha(55 if self.alpha else 255)
                    self.alpha = not self.alpha
                    time.wait(10)
        if onCanvas:
            if mb[0] == 1:
                if tool == "Circle_Brush":
                    self.highlighter.circle(col, size)
                elif tool == "Square_Brush":
                    self.highlighter.rect(col, size)
                elif tool == "Line_Brush":
                    self.highlighter.line((oldmx, oldmy), col, size)

                    # brush right click
            elif mb[2] == 1:
                if tool == "Circle_Brush":
                    self.highlighter.circle(createRandomColor(), size)
                elif tool == "Square_Brush":
                    self.highlighter.rect(createRandomColor(), size)
                elif tool == "Line_Brush":
                    self.highlighter.line((oldmx, oldmy), createRandomColor(), size)

        self.old = mx, my
