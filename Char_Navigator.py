# This is for the main screen that the DM navigates to for creating Characters in.  Creates
# the screen and the relevant buttons (NPC and Player)
# Each of which will have their own navigation screen later on.

import pygame as pg
import random
import os
import numpy as np
import pygame.surfarray as surfarray
from pygame.locals import *

##WINDOWHEIGHT = 629
##WINDOWWIDTH = 1000

def createChar(surf):
    pg.init()
    WINDOWWIDTH = surf.get_width()
    WINDOWHEIGHT = surf.get_height()

# Player Button
    playSurf = pg.image.load('images/music_Button.png')
    playSurf = pg.transform.scale(playSurf, (int(playSurf.get_width()/8),int(playSurf.get_height()/8)))
    playRect = playSurf.get_rect(topleft = (int(playSurf.get_width()*1/5), int(WINDOWHEIGHT/4) - int(playSurf.get_height()/2)))

# NPC Button
    nopcSurf = pg.image.load('images/tools/DMTB_NPC_Button.png')
    nopcSurf = pg.transform.scale(nopcSurf, (int(nopcSurf.get_width()/8),int(nopcSurf.get_height()/8)))
    nopcRect = nopcSurf.get_rect(topleft = (int(WINDOWWIDTH-nopcSurf.get_width()*6/5), int(WINDOWHEIGHT/4) - int(nopcSurf.get_height()/2)))



# The background
    toolSurf = pg.image.load('images/navigation_screen.png')
    toolSurf = pg.transform.scale(toolSurf, (WINDOWWIDTH,WINDOWHEIGHT))

# Adding the elements to the display
    surf.fill((0,0,0))
    surf.blit(toolSurf,(0,0))
    surf.blit(playSurf, (int(playSurf.get_width()*1/5), int(WINDOWHEIGHT/4) - int(playSurf.get_height()/2)))
    surf.blit(nopcSurf, (int(WINDOWWIDTH-nopcSurf.get_width()*6/5), int(WINDOWHEIGHT/4) - int(nopcSurf.get_height()/2)))
    return(surf,playSurf, playRect,nopcSurf,nopcRect)
