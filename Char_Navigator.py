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

def createChar(arguments):
    surf = arguments['surf']
    pg.init()
    WINDOWWIDTH = surf.get_width()
    WINDOWHEIGHT = surf.get_height()

# Player Button
    playSurf = pg.image.load('images/music_Button.png')
    playSurf = pg.transform.smoothscale(playSurf, (int(playSurf.get_width()/8*WINDOWWIDTH/1000),int(playSurf.get_height()/8*WINDOWHEIGHT/629)))

    playPosition = ((int(playSurf.get_width()*1/5), int(WINDOWHEIGHT/4) - int(playSurf.get_height()/2)))
    playRect = playSurf.get_rect(topleft = playPosition)

# NPC Button
    nopcSurf = pg.image.load('images/tools/DMTB_NPC_Button.png')
    nopcSurf = pg.transform.smoothscale(nopcSurf, (int(nopcSurf.get_width()/8*WINDOWWIDTH/1000),int(nopcSurf.get_height()/8*WINDOWHEIGHT/629)))
    nopcPosition = (int(WINDOWWIDTH-nopcSurf.get_width()*6/5), int(WINDOWHEIGHT/4) - int(nopcSurf.get_height()/2))
    nopcRect = nopcSurf.get_rect(topleft = nopcPosition)



# The background
    toolSurf = pg.image.load('images/navigation_screen.png')
    toolSurf = pg.transform.scale(toolSurf, (WINDOWWIDTH,WINDOWHEIGHT))

# Adding the elements to the display
    surf.fill((0,0,0))
    surf.blit(toolSurf,(0,0))
    surf.blit(playSurf, playPosition)
    surf.blit(nopcSurf, nopcPosition)

    rects = [playRect,nopcRect]
    keys = ['diceRoller', 'NPC','quest']
    surfs = {'surf': surf}
#    return(surfs,rects, keys)
    return(rects, keys)
