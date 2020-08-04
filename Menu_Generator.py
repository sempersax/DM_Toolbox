# The code for generating the main menu

import pygame as pg
import random
import os
import numpy as np
import pygame.surfarray as surfarray
from pygame.locals import *

##WINDOWHEIGHT = 629
##WINDOWWIDTH = 1000

def createMenu(SURFS):
    pg.init()
    rects = []
    surf = SURFS[0]
    WINDOWWIDTH = surf.get_width()
    WINDOWHEIGHT = surf.get_height()
    screenChoice = np.random.randint(1,high = 5)
    screen = pg.image.load('images/screens/menu_screen_{}.jpg'.format(str(screenChoice)))
    screen = pg.transform.smoothscale(screen, (WINDOWWIDTH, WINDOWHEIGHT))
    qsurf = pg.image.load('images/DMTB_QUEST.png')
    qheight = qsurf.get_height()
    qwidth = qsurf.get_width()
    qRect = qsurf.get_rect(topleft = (WINDOWWIDTH/2 - int(qwidth/2), WINDOWHEIGHT - 100 ))
    tSurf = pg.image.load('images/DMTB_COVER.png')
    surf.blit(screen, (0,0))
    surf.blit(qsurf, (WINDOWWIDTH/2 - int(qwidth/2), WINDOWHEIGHT - 100 ) )
    surf.blit(tSurf, (WINDOWWIDTH/2 - int(tSurf.get_width()/2), 10))
    rects = [qRect]
    keys = ['quest']
    surfs = [surf]
    
    return(surfs,rects,keys)

def reachMenu(surf):
    pg.init()
    WINDOWWIDTH = surf.get_width()
    WINDOWHEIGHT = surf.get_height()
    menButton = pg.image.load('images/menu_button.png')
    menButton = pg.transform.scale(menButton, (int(menButton.get_width()/2),int(menButton.get_height()/2)))
    menRect = menButton.get_rect(topleft = (int(WINDOWWIDTH-menButton.get_width()*1.5),0))
    surf.blit(menButton, (int(WINDOWWIDTH-menButton.get_width()*1.5),0))
    menRect = [menRect]
    return(surf, menRect)
