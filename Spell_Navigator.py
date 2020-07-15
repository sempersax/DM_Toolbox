# This is for the main screen that the DM navigates to for referencing spells in.  Creates
# the screen and the relevant buttons 
# Each of which will have their own navigation screen later on.

import pygame as pg
import random
import os
import numpy as np
import pygame.surfarray as surfarray
from pygame.locals import *

##WINDOWHEIGHT = 629
##WINDOWWIDTH = 1000

def createSpell(surf):
    pg.init()
    WINDOWWIDTH = surf.get_width()
    WINDOWHEIGHT = surf.get_height()

# Tavern Button
    raceSurf = pg.image.load('images/blank_button.png')
    raceSurf = pg.transform.scale(raceSurf, (int(raceSurf.get_width()/8),int(raceSurf.get_height()/8)))
    raceRect = raceSurf.get_rect(topleft = (int(raceSurf.get_width()*1/5), int(WINDOWHEIGHT/4) - int(raceSurf.get_height()/2)))

    spellSurf = pg.image.load('images/DMTB_SPELL_screen.jpg')
    spellSurf = pg.transform.scale(spellSurf, (WINDOWWIDTH,WINDOWHEIGHT))
    surf.fill((0,0,0))
    surf.blit(spellSurf,(0,0))
    surf.blit(raceSurf, (int(raceSurf.get_width()*1/5), int(WINDOWHEIGHT/4) - int(raceSurf.get_height()/2)))
    return(surf,raceSurf, raceRect, spellSurf)
