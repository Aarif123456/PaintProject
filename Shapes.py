from pygame import *
class Shapes(object):
    def __init__(self, screen):
        super(Shapes, self).__init__()
        self.screen = screen
        self.surface = surface
    
    def ellipse(self, surface, col, fill, canvasRect, coord, perfect, size):
        self.screen.blit(surface,canvasRect)
        (mx,my, startx,starty) = coord
        if perfect:  #perfect use circle
            if (abs(mx-startx)+abs(my-starty))//2> size:
                draw.circle(self.screen,col,(startx,starty),((abs(mx-startx)+abs(my-starty))//2),size*fill)
            else:
                draw.circle(self.screen,col,(startx,starty),((abs(mx-startx)+abs(my-starty))//2),0)
        else:
            if abs(mx-startx)>size*2 and abs(my-starty)> size*2:
                draw.ellipse(self.screen,col,(min(mx,startx),min(my,starty),abs(mx-startx),abs(my-starty)),size*fill)
            else:
                draw.ellipse(self.screen,col,(min(mx,startx),min(my,starty),abs(mx-startx),abs(my-starty)),0)
       

    def rect(self, surface, col, fill, canvasRect, coord, perfect, size):
        self.screen.blit(surface,canvasRect)
        (mx,my, startx,starty) = coord
        if perfect:        
            draw.rect(self.screen,col,((startx),(starty),((mx-startx+my-starty)//2),((mx-startx+my-starty)//2)),size*fill)
        else:
            draw.rect(self.screen,col,((startx),(starty),(mx-startx),(my-starty)),size*fill)
            
    def polygon(self, polylist, col, fill,size):   
        draw.polygon(self.screen,col,polylist,size*fill)

    def line(self,surface, col,canvasRect, coord, size):
        (mx,my, startx,starty) = coord        
        self.screen.blit(surface,canvasRect)
        draw.line(self.screen,(col),((startx),(starty)),(mx,my), size)

    def aaline(self, surface, col, canvasRect, coord):
        (mx,my, startx,starty) = coord
        self.screen.blit(surface,canvasRect)
        draw.aaline(self.screen,(col),(startx,starty),(mx,my))      