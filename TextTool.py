from pygame import *

class TextTool(object):
    numShiftList=[")","!","@","#","$","%","^","&","*","("]
    def __init__(self, surface, fontFace="Comic Sans MS"):
        super(TextTool, self).__init__()
        font.init()
        self.surface = surface
        self.fontFace="Comic Sans MS"

    def text(self,color,msg,x,y, size):
        curFont = font.SysFont(self.fontFace, size)
        txtpic=curFont.render (msg, False, (color))
        self.surface.blit(txtpic,(x,y))
    
    def handleKeystrokes(self, e, msg)->str:
        if key.get_mods()& KMOD_CAPS and not key.get_mods()& KMOD_SHIFT and e.key>96 and e.key<123:              
            msg+=chr(e.key-32)
        elif key.get_mods()& KMOD_SHIFT and not key.get_mods()& KMOD_CAPS and e.key>96 and e.key<123: 
            msg+=chr(e.key-32)
        # handle shift on number 
        elif key.get_mods()& KMOD_SHIFT and e.key>47 and e.key<60: 
            msg+=TextTool.numShiftList[e.key-48]
        # handle space bar
        elif e.key==32: 
            msg+=" "
        # normal case    
        elif e.key>32 and e.key<126:         
            msg+=chr(e.key)
        # handle backspace
        elif e.key==8:
            msg=msg[:-1]
        return msg

    