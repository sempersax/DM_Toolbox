# This is for the main screen that the DM navigates to for creating Monsters in.  Creates
# the screen and the relevant buttons 
# Each of which will have their own navigation screen later on.

import pygame as pg
import random
import os
import numpy as np
import pygame.surfarray as surfarray
from pygame.locals import *

WINDOWHEIGHT = 629
WINDOWWIDTH = 1000

def createMonster(surf):
    pg.init()

# Tavern Button
    raceSurf = pg.image.load('images/music_Button.png')
    raceSurf = pg.transform.scale(raceSurf, (int(raceSurf.get_width()/8),int(raceSurf.get_height()/8)))
    raceRect = raceSurf.get_rect(topleft = (int(raceSurf.get_width()*1/5), int(WINDOWHEIGHT/4) - int(raceSurf.get_height()/2)))
### Battle Button
##    bttleSurf = pg.image.load('images/music_Button.png')
##    bttleSurf = pg.transform.scale(bttleSurf, (int(bttleSurf.get_width()/8),int(bttleSurf.get_height()/8)))
##    bttleRect = bttleSurf.get_rect(topleft = (WINDOWWIDTH - int(bttleSurf.get_width()*6/5), int(WINDOWHEIGHT/4) - int(bttleSurf.get_height()/2)))
### Region Button
##    rgionSurf = pg.image.load('images/music_Button.png')
##    rgionSurf = pg.transform.scale(rgionSurf, (int(rgionSurf.get_width()/8),int(rgionSurf.get_height()/8)))
##    rgionRect = rgionSurf.get_rect(topleft = (int(rgionSurf.get_width()*1/5), int(WINDOWHEIGHT*3/4) + int(rgionSurf.get_height()/2)))

    monstSurf = pg.image.load('images/DMTB_MONSTERS_screen.jpg')
    monstSurf = pg.transform.scale(monstSurf, (WINDOWWIDTH,WINDOWHEIGHT))
    surf.fill((0,0,0))
    surf.blit(monstSurf,(0,0))
    surf.blit(raceSurf, (int(raceSurf.get_width()*1/5), int(WINDOWHEIGHT/4) - int(raceSurf.get_height()/2)))
##    surf.blit(bttleSurf, (WINDOWWIDTH - int(bttleSurf.get_width()*6/5), int(WINDOWHEIGHT/4) - int(bttleSurf.get_height()/2)))
##    surf.blit(rgionSurf, (int(rgionSurf.get_width()*1/5), int(WINDOWHEIGHT*3/4) + int(rgionSurf.get_height()/2)))
    return(surf,raceSurf, raceRect)
