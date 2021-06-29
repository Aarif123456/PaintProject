from pygame import *
from random import randint
class Brush: 

    def __init__(self, surface):
        super(Brush, self).__init__()
        self.surface = surface
        self.sticky = False

    def getCoordinates(self,size):
        x,y = mouse.get_pos()
        if  self.sticky:
            x -= x%((int)(size*1.5))
            y -= y%((int)(size*1.5))
        return (x,y)

    def circle(self,col,width):
        mx,my=self.getCoordinates(width)
        draw.circle(self.surface,(col),(mx,my),width)

    def rect(self,col,width):
        mx,my=self.getCoordinates(width)
        draw.rect(self.surface,(col),(mx,my,width,width),width)

    def line(self,old,col,width):
        mx,my=self.getCoordinates(width)
        oldmx,oldmy=old
        draw.line(self.surface,(col),(mx,my),(oldmx,oldmy),width)

    def explosion(self,col,width):
        mx,my=self.getCoordinates(width)
        draw.line(self.surface,(col),(mx,my),(mx+randint(-width,width),my+randint(-width,width)))

    def toggleSticky(self):
        self.sticky = not self.sticky

    def colormasher(self, width, canvasRect):
        mx,my=self.getCoordinates(width)
        # count number of time rectangle resized.
        tries = 0 
        # We resize so we don"t accidentally don"t get color from outside the canvas
        while tries <10:
            colorrect = Rect(mx-width//2,my-width//2,width,width)
            if canvasRect.contains(colorrect): break
            tries += 1
            width //= 2
            
        col=transform.average_color(self.surface,colorrect)
        draw.rect(self.surface,col,colorrect)