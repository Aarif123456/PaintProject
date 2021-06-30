from pygame import *

class PaintLayout(object):
    def __init__(self, screenWidth = 1024, screenHeight = 720):
        super(PaintLayout, self).__init__()
        self.screenWidth=screenWidth
        self.screenHeight=screenHeight
        self.screen = display.set_mode((screenWidth,screenHeight ))
        self.screen.blit(image.load("Resources/design/others/background.png"),(0,0))

        # Surface used to give highlight effect
        self.cover = Surface((screenWidth,screenHeight)).convert() # make blank Surface
        self.cover.set_alpha(255)
        self.cover.set_colorkey((255,255,255))
        
    def createLogo(self, logoLocation):
        self.screen.blit(image.load(logoLocation),(self.screenWidth/2-146,0))

    #text renderer from https://www.pygame.org/wiki/TextWrap
    def drawText(screen, text, color, rect, fontSize, fontFace="Comic Sans MS", aa=False, bkg=None):
        font.init()
        curFont = font.SysFont(fontFace,fontSize)
        rect = Rect(rect)
        y = rect.top
        lineSpacing = -2

        # get the height of the font
        fontHeight = curFont.size("Tg")[1]

        while text:
            i = 1
            # determine if the row of text will be outside our area
            if y + fontHeight > rect.bottom:
                break
            # determine maximum width of line
            while curFont.size(text[:i])[0] < rect.width and i < len(text):
                i += 1
            # if we've wrapped the text, then adjust the wrap to the last word      
            if i < len(text): 
                i = text.rfind(" ", 0, i) + 1
            # render the line and blit it to the surface
            if bkg:
                image = curFont.render(text[:i], 1, color, bkg)
                image.set_colorkey(bkg)
            else:
                image = curFont.render(text[:i], aa, color)
            screen.blit(image, (rect.left, y))
            y += fontHeight + lineSpacing
            # remove the text we just blitted
            text = text[i:]

        return text