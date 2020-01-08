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

# NPC Button
    npcSurf = pg.image.load('images/music_Button.png')
    npcSurf = pg.transform.scale(npcSurf, (int(npcSurf.get_width()/8),int(npcSurf.get_height()/8)))
    npcRect = npcSurf.get_rect(topleft = (int(npcSurf.get_width()*1/5), int(WINDOWHEIGHT/4) - int(npcSurf.get_height()/2)))
# Music Button
    musicSurf = pg.image.load('images/music_Button.png')
    musicSurf = pg.transform.scale(musicSurf, (int(musicSurf.get_width()/8),int(musicSurf.get_height()/8)))
    musicRect = musicSurf.get_rect(topleft = (WINDOWWIDTH - int(musicSurf.get_width()*6/5), int(WINDOWHEIGHT/4) - int(musicSurf.get_height()/2)))
# Spell Button
    spellSurf = pg.image.load('images/music_Button.png')
    spellSurf = pg.transform.scale(spellSurf, (int(spellSurf.get_width()/8),int(spellSurf.get_height()/8)))
    spellRect = spellSurf.get_rect(topleft = (int(spellSurf.get_width()*1/5), int(WINDOWHEIGHT*3/4) + int(spellSurf.get_height()/2)))
# Monster Button
    monstSurf = pg.image.load('images/music_Button.png')
    monstSurf = pg.transform.scale(monstSurf, (int(monstSurf.get_width()/8),int(monstSurf.get_height()/8)))
    monstRect = monstSurf.get_rect(topleft = (WINDOWWIDTH - int(monstSurf.get_width()*6/5), int(WINDOWHEIGHT*3/4) + int(monstSurf.get_height()/2)))

    toolSurf = pg.image.load('images/navigation_screen.png')
    toolSurf = pg.transform.scale(toolSurf, (WINDOWWIDTH,WINDOWHEIGHT))
    menSurf = pg.image.load
    surf.fill((0,0,0))
    surf.blit(toolSurf,(0,0))
    surf.blit(npcSurf, (int(npcSurf.get_width()*1/5), int(WINDOWHEIGHT/4) - int(npcSurf.get_height()/2)))
    surf.blit(musicSurf, (WINDOWWIDTH - int(musicSurf.get_width()*6/5), int(WINDOWHEIGHT/4) - int(musicSurf.get_height()/2)))
    surf.blit(spellSurf, (int(spellSurf.get_width()*1/5), int(WINDOWHEIGHT*3/4) + int(spellSurf.get_height()/2)))
    surf.blit(monstSurf, (WINDOWWIDTH - int(monstSurf.get_width()*6/5), int(WINDOWHEIGHT*3/4) + int(monstSurf.get_height()/2)))
    return(surf,npcSurf,npcRect,musicSurf,musicRect,spellSurf,spellRect,monstSurf,monstRect)

def createBack(surf):
    pg.init()
    backButton = pg.image.load('images/circle_button.PNG')
    backButton = pg.transform.scale(backButton, (int(backButton.get_width()/2),int(backButton.get_height()/2)))
    backRect = backButton.get_rect(topleft =  (int(WINDOWWIDTH-backButton.get_width()*2.5),int(backButton.get_height()/4)))
    surf.blit(backButton, (int(WINDOWWIDTH-backButton.get_width()*2.5),int(backButton.get_height()/4)))
    return(surf,backButton,backRect)
                                   
    
    
