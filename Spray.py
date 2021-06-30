from random import *

from pygame import *


class Spray(object):
    # Controls if spray should spray in circular format 
    CIRCLE_SHAPE = 1

    def __init__(self, surface):
        super(Spray, self).__init__()
        self.surface = surface

    # spray out circles
    def sprayCircle(self, size, speed, radius, spraydesign, col):
        mx, my = mouse.get_pos()
        for i in range(speed):
            x = mx + randint(-radius, radius)
            y = my + randint(-radius, radius)
            if spraydesign == Spray.CIRCLE_SHAPE:
                if ((x - mx) ** 2 + (y - my) ** 2) < radius ** 2:  # equation of circle
                    draw.circle(self.surface, col, (x, y), size)
            else:
                draw.circle(self.surface, col, (x, y), size)

    def spraySquare(self, size, speed, radius, spraydesign, col):
        mx, my = mouse.get_pos()
        for i in range(speed):
            x = mx + randint(-radius, radius)
            y = my + randint(-radius, radius)
            if spraydesign == Spray.CIRCLE_SHAPE:
                if ((x - mx) ** 2 + (y - my) ** 2) < radius ** 2:  # equation of circle
                    draw.rect(self.surface, col, (x, y, size, size))
            else:
                draw.rect(self.surface, col, (x, y, size, size))

    def rainSquare(self, size, speed, radius, spraydesign, col):
        mx, my = mouse.get_pos()
        for i in range(speed):
            x = mx + randint(-radius, radius)
            y = my + randint(-radius, radius)
            if spraydesign == Spray.CIRCLE_SHAPE:
                if ((x - mx) ** 2 + (y - my) ** 2) < radius ** 2:  # equation of circle
                    draw.line(self.surface, col, (x, y), (x + randint(-3, 3), y + randint(-3, 3)), size)
            else:
                draw.line(self.surface, col, (x, y), (x + randint(-3, 3), y + randint(-3, 3)), size)
