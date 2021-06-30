import os

from pygame import *

from Hover import Hover
from PaintLayout import PaintLayout


class MusicBox(object):
    def __init__(self, surface):
        super().__init__()
        self.noSound = False
        self.surface = surface
        try:
            mixer.init()
        except Exception as _:
            self.noSound = True

        # music box
        self.musicNameRect = Rect(810, 10, 180, 25)
        draw.rect(surface, (0, 0, 0), self.musicNameRect, 1)
        PaintLayout.drawText(surface, "Music Box", (0, 0, 0), self.musicNameRect, 25)

        # play and stop box 
        self.musicPlayRect = Rect(815, 36, 84, 43)
        self.musicStopRect = Rect(900, 36, 84, 43)
        Hover.addHover(self.musicPlayRect)
        Hover.addHover(self.musicStopRect)
        PaintLayout.drawText(surface, "Play", (0, 0, 0), self.musicPlayRect, 25)
        PaintLayout.drawText(surface, "Stop", (0, 0, 0), self.musicStopRect, 25)

        self.musicNextRect = Rect(900, 80, 84, 25)
        self.musicBackRect = Rect(815, 80, 84, 25)
        PaintLayout.createNextBox(surface, self.musicNextRect)
        PaintLayout.createBackBox(surface, self.musicBackRect)
        self.curSong = 0
        self.songs = []

    def setup(self):
        self.songs = []
        path = "Resources/music box/Songs"
        files = os.listdir(path)
        files.sort()  # because listdir does not guarantee order
        for file in files:
            if file.endswith(".ogg"):
                self.songs.append(f"{path}/{file}")

    def handle(self):
        if self.noSound: return None
        PaintLayout.drawText(self.surface, f"Music Box: {self.curSong + 1}", (0, 0, 0), self.musicNameRect, 25)
        mx, my = mouse.get_pos()
        if self.musicNextRect.collidepoint(mx, my):
            self.curSong += 1
        elif self.musicBackRect.collidepoint(mx, my):
            self.curSong += len(self.songs) - 1
        elif self.musicPlayRect.collidepoint(mx, my):
            mixer.music.stop()
            mixer.music.load(self.songs[self.curSong])
            mixer.music.play(-1)
        elif self.musicStopRect.collidepoint(mx, my):
            mixer.music.stop()
