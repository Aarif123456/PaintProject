from random import *

from pygame import *

screen = display.set_mode((1024, 720))
screen.fill((255, 255, 255))
col = randint(0, 255), randint(0, 255), randint(0, 255)
running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False

    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()
    if mb[0] == 1:
        mx, my = mouse.get_pos()
        draw.line(screen, (randint(0, 255), randint(0, 255), randint(0, 255)), (mx, my),
                  (randint(0, 1024), randint(0, 720)), 2)
    if mb[2] == 1:
        screen.fill((255, 255, 255))
        col = randint(0, 255), randint(0, 255), randint(0, 255)
    oldmx, oldmy, = mx, my
    display.flip()
quit()
