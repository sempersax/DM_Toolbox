import numpy as np
import os
import pygame as pg
import time 
def race(surf,races):
    pg.init()
    print(races)
    start = time.time()
    raceRects = []
##    start1 = time.time()
##    for i in range(len(files)): #this loads all of the race images at once.
##        races.append(pg.image.load('images/races/'+files[i]))
##        races[i] = pg.transform.scale(races[i], (int(races[i].get_width()/8),int(races[i].get_height()/8)))
##    print('image load time = ',time.time()-start1)
    surf.fill((0,0,0))
    surf.blit(pg.image.load('images/navigation_screen.png'),(0,0))
    start2=time.time()
    for i in range(int(np.ceil(len(races)/4))):
        for j in range(4):
            if(j+i*4)>= len(races):
                break
            position = (int(races[i].get_width()*(1+i)),int(races[i].get_height()*(1.3+j)))
            surf.blit(races[j+i*4], position)
            raceRects.append(races[i].get_rect(topleft = position))
    print('screen blit time = ',time.time()-start2)
    print(time.time()-start)
    return(surf,races)

