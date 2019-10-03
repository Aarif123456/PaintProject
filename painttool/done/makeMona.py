# pygameRev1.py
from pygame import *
from math import *

screen = display.set_mode((743,1155))
m = image.load("mona.jpg")
screen.blit(m,(0,0))
mon = open("mona.py", "w")
mon.write("""from pygame import *
from math import *

screen = display.set_mode((743,1155))
""")
running = True
display.flip()

for x in range(0,743,4):
    for y in range(0,1155,4):
        c = str(screen.get_at((x,y)))
        mon.write("draw.rect(screen,"+c+",("+str(x)+","+str(y)+",4,4))\n")
    mon.write("display.flip()\n")
    print (x)

    

mon.write("""running = True
while running:
    for evnt in event.get():                # checks all events that happen
        if evnt.type == QUIT:
            running = False
    
quit()""")
mon.close()

quit()
