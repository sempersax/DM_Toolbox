# This is for the main screen that the DM navigates to for creating Monsters in.  Creates
# the screen and the relevant buttons 
# Each of which will have their own navigation screen later on.

import pygame as pg
import random
import os
import numpy as np
import pygame.surfarray as surfarray
from pygame.locals import *
import time

WINDOWHEIGHT = 629
WINDOWWIDTH = 1000

def createMonster(surf):
    pg.init()
    start = time.time()
    mypath="../Dungeon_Master_Tools/MonsterScrape/MonsterJsons/"
    onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
    for i in range(0,len(onlyfiles)):
        onlyfiles[i] = onlyfiles[i].replace('_', ' ').replace('.json','')
    print('cause ',time.time()-start,' second delay')

# Tavern Button
    searchSurf = pg.image.load('images/music_Button.png')
    searchSurf = pg.transform.scale(searchSurf, (int(searchSurf.get_width()/8),int(searchSurf.get_height()/8)))
    searchRect = searchSurf.get_rect(topleft = (int(searchSurf.get_width()*1/5), int(WINDOWHEIGHT/4) - int(searchSurf.get_height()/2)))

    monstSurf = pg.image.load('images/DMTB_MONSTERS_screen.jpg')
    monstSurf = pg.transform.scale(monstSurf, (WINDOWWIDTH,WINDOWHEIGHT))
    surf.fill((0,0,0))
    surf.blit(monstSurf,(0,0))
    surf.blit(searchSurf, (int(searchSurf.get_width()*1/5), int(WINDOWHEIGHT/4) - int(searchSurf.get_height()/2)))
    return(surf,searchSurf, searchRect,monstSurf)
