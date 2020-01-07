# This is for the main screen that the DM navigates to tools in.  Creates
# the screen and the relevant buttons (NPCs, Music, Spells, Monsters)
# Each of which will have their own navigation screen later on.

import pygame as pg
import random
import os
import numpy as np
import pygame.surfarray as surfarray
from pygame.locals import *

WINDOWHEIGHT = 629
WINDOWWIDTH = 1000

def createTools(surf):
    pg.init()
    musicSurf = pg.image.load('images/music_Button.png')
    musicSurf = pg.transform.scale(musicSurf, (int(musicSurf.get_width()/8),int(musicSurf.get_height()/8)))
    musicRect = musicSurf.get_rect(topleft = (WINDOWWIDTH - int(musicSurf.get_width()*6/5), int(WINDOWHEIGHT/4) - int(musicSurf.get_height()/2)))
    toolSurf = pg.image.load('images/navigation_screen.png')
    toolSurf = pg.transform.scale(toolSurf, (WINDOWWIDTH,WINDOWHEIGHT))
    menSurf = pg.image.load
    surf.fill((0,0,0))
    surf.blit(toolSurf,(0,0))
    surf.blit(musicSurf, (WINDOWWIDTH - int(musicSurf.get_width()*6/5), int(WINDOWHEIGHT/4) - int(musicSurf.get_height()/2)))
    return(surf,musicSurf,musicRect)
