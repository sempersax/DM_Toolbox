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

def createMusic(surf):
    pg.init()

# Tavern Button
    tavrnSurf = pg.image.load('images/DMTB_TAVERN_Button.png')
    tavrnSurf = pg.transform.scale(tavrnSurf, (int(tavrnSurf.get_width()/8),int(tavrnSurf.get_height()/8)))
    tavrnRect = tavrnSurf.get_rect(topleft = (int(tavrnSurf.get_width()*1/5), int(WINDOWHEIGHT/4) - int(tavrnSurf.get_height()/2)))
# Battle Button
    bttleSurf = pg.image.load('images/DMTB_BATTLE_Button.png')
    bttleSurf = pg.transform.scale(bttleSurf, (int(bttleSurf.get_width()/8),int(bttleSurf.get_height()/8)))
    bttleRect = bttleSurf.get_rect(topleft = (WINDOWWIDTH - int(bttleSurf.get_width()*6/5), int(WINDOWHEIGHT/4) - int(bttleSurf.get_height()/2)))
# Region Button
    rgionSurf = pg.image.load('images/DMTB_REGION_Button.png')
    rgionSurf = pg.transform.scale(rgionSurf, (int(rgionSurf.get_width()/8),int(rgionSurf.get_height()/8)))
    rgionRect = rgionSurf.get_rect(topleft = (int(rgionSurf.get_width()*1/5), int(WINDOWHEIGHT*3/4) + int(rgionSurf.get_height()/2)))

    toolSurf = pg.image.load('images/navigation_screen.png')
    toolSurf = pg.transform.scale(toolSurf, (WINDOWWIDTH,WINDOWHEIGHT))
    surf.fill((0,0,0))
    surf.blit(toolSurf,(0,0))
    surf.blit(tavrnSurf, (int(tavrnSurf.get_width()*1/5), int(WINDOWHEIGHT/4) - int(tavrnSurf.get_height()/2)))
    surf.blit(bttleSurf, (WINDOWWIDTH - int(bttleSurf.get_width()*6/5), int(WINDOWHEIGHT/4) - int(bttleSurf.get_height()/2)))
    surf.blit(rgionSurf, (int(rgionSurf.get_width()*1/5), int(WINDOWHEIGHT*3/4) + int(rgionSurf.get_height()/2)))
    return(surf,tavrnSurf, tavrnRect, bttleSurf, bttleRect, rgionSurf, rgionRect)
