# The code for generating the main menu

import pygame as pg
import random
import os
import numpy as np
import pygame.surfarray as surfarray
from pygame.locals import *

WINDOWHEIGHT = 629
WINDOWWIDTH = 1000

def createMenu(surf,choice):
    pg.init()
    _files = os.listdir('images')
    screens = [k for k in _files if 'menu_screen' in k]
    mensurf = pg.image.load('images/'+str(screens[choice]))
    mensurf = pg.transform.scale(mensurf, (WINDOWWIDTH,WINDOWHEIGHT))
    qsurf = pg.image.load('images/DMTB_QUEST.png')
    qheight = qsurf.get_height()
    qwidth = qsurf.get_width()
    #qsurf = pg.transform.scale(qsurf, (int(qwidth/3), int(qheight/3)))
    qheight = qsurf.get_height()
    qwidth = qsurf.get_width()    
    qRect = qsurf.get_rect(topleft = (WINDOWWIDTH/2 - int(qwidth/2), WINDOWHEIGHT - 100 ))
    tSurf = pg.image.load('images/DMTB_COVER.png')
    surf.blit(mensurf, (0,0))
    surf.blit(qsurf, (WINDOWWIDTH/2 - int(qwidth/2), WINDOWHEIGHT - 100 ) )
    surf.blit(tSurf, (WINDOWWIDTH/2 - int(tSurf.get_width()/2), 10))
    return(surf,qsurf,qRect,len(screens))

def reachMenu(surf):
    pg.init()
    menButton = pg.image.load('images/menu_button.png')
    menButton = pg.transform.scale(menButton, (int(menButton.get_width()/2),int(menButton.get_height()/2)))
    menRect = menButton.get_rect(topleft = (int(WINDOWWIDTH-menButton.get_width()*1.5),0))
    surf.blit(menButton, (int(WINDOWWIDTH-menButton.get_width()*1.5),0))
    return(surf, menButton, menRect)
