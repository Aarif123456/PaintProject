from pygame import *

screen = display.set_mode((1000, 600))
font.init()
comicFont = font.SysFont("Comic Sans MS", 20)

running = True
while running:
    click = False
    for e in event.get():
        if e.type == QUIT:
            running = False
    mb = mouse.get_pressed()
    mx, my = mouse.get_pos()
    screen.fill((0, 0, 0))
    txtPic = comicFont.render((str((mx, my))), True, (255, 0, 0))
    screen.blit(txtPic, (50, 50))
    if mb[2] == 1:
        screen.fill((0, 0, 0))
    display.flip()
font.quit()
del comicFont
quit()
