# The code for generating the main menu

import pygame as pg
import random
import os
import numpy as np
import pygame.surfarray as surfarray
from pygame.locals import *

WINDOWHEIGHT = 629
WINDOWWIDTH = 1000

def createMenu(surf):
    pg.init()
    mensurf = pg.image.load('images/menu_screen_2.jpg')
    mensurf = pg.transform.scale(mensurf, (WINDOWWIDTH,WINDOWHEIGHT))
    qsurf = pg.image.load('images/quest_start.png')
    qheight = qsurf.get_height()
    qwidth = qsurf.get_width()
    qsurf = pg.transform.scale(qsurf, (int(qwidth/3), int(qheight/3)))
    qheight = qsurf.get_height()
    qwidth = qsurf.get_width()    
    qRect = qsurf.get_rect()
    tSurf = pg.image.load('images/title.png')
    surf.blit(mensurf, (0,0))
    surf.blit(qsurf, (WINDOWWIDTH/2 - int(qwidth/2), WINDOWHEIGHT - 100 ) )
    surf.blit(tSurf, (WINDOWWIDTH/2 - int(tSurf.get_width()/2), tSurf.get_height()+10))
    return(surf,qsurf,qRect)

