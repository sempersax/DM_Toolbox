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
    npcSurf = pg.image.load('images/DMTB_NPC_Button.png')
    npcSurf = pg.transform.scale(npcSurf, (int(npcSurf.get_width()/8),int(npcSurf.get_height()/8)))
    npcRect = npcSurf.get_rect(topleft = (int(npcSurf.get_width()*1/5), int(WINDOWHEIGHT/4) - int(npcSurf.get_height()/2)))
# Music Button
    musicSurf = pg.image.load('images/DMTB_Music_Button.png')
    musicSurf = pg.transform.scale(musicSurf, (int(musicSurf.get_width()/8),int(musicSurf.get_height()/8)))
    musicRect = musicSurf.get_rect(topleft = (WINDOWWIDTH - int(musicSurf.get_width()*6/5), int(WINDOWHEIGHT/4) - int(musicSurf.get_height()/2)))
# Spell Button
    spellSurf = pg.image.load('images/DMTB_SPELLS_Button.png')
    spellSurf = pg.transform.scale(spellSurf, (int(spellSurf.get_width()/8),int(spellSurf.get_height()/8)))
    spellRect = spellSurf.get_rect(topleft = (int(spellSurf.get_width()*1/5), int(WINDOWHEIGHT*3/4) + int(spellSurf.get_height()/2)))
# Monster Button
    monstSurf = pg.image.load('images/DMTB_MONSTERS_Button.png')
    monstSurf = pg.transform.scale(monstSurf, (int(monstSurf.get_width()/8),int(monstSurf.get_height()/8)))
    monstRect = monstSurf.get_rect(topleft = (WINDOWWIDTH - int(monstSurf.get_width()*6/5), int(WINDOWHEIGHT*3/4) + int(monstSurf.get_height()/2)))

    toolSurf = pg.image.load('images/navigation_screen.png')
    toolSurf = pg.transform.scale(toolSurf, (WINDOWWIDTH,WINDOWHEIGHT))
    surf.fill((0,0,0))
    surf.blit(toolSurf,(0,0))
    surf.blit(npcSurf, (int(npcSurf.get_width()*1/5), int(WINDOWHEIGHT/4) - int(npcSurf.get_height()/2)))
    surf.blit(musicSurf, (WINDOWWIDTH - int(musicSurf.get_width()*6/5), int(WINDOWHEIGHT/4) - int(musicSurf.get_height()/2)))
    surf.blit(spellSurf, (int(spellSurf.get_width()*1/5), int(WINDOWHEIGHT*3/4) + int(spellSurf.get_height()/2)))
    surf.blit(monstSurf, (WINDOWWIDTH - int(monstSurf.get_width()*6/5), int(WINDOWHEIGHT*3/4) + int(monstSurf.get_height()/2)))
    return(surf,npcSurf,npcRect,musicSurf,musicRect,spellSurf,spellRect,monstSurf,monstRect)

#This is to create a back button, to go back a single screen
def createBack(surf):
    pg.init()
    backButton = pg.image.load('images/circle_button.PNG')
    backButton = pg.transform.scale(backButton, (int(backButton.get_width()/2),int(backButton.get_height()/2)))
    backRect = backButton.get_rect(topleft =  (int(WINDOWWIDTH-backButton.get_width()*2.5),0))
    surf.blit(backButton, (int(WINDOWWIDTH-backButton.get_width()*2.5),0))
    return(surf,backButton,backRect)

# This is to create the other 3 buttons so one can switch categories quickly
# All 4 are create, but based on choice, one is not blit to the screen
def createMiniTools(surf,choice):
    pg.init()
    
    npcButton = pg.image.load('images/DMTB_NPC_CIRCLE_button.PNG')
    npcButton = pg.transform.scale(npcButton, (int(npcButton.get_width()/2),int(npcButton.get_height()/2)))
    musicButton = pg.image.load('images/DMTB_MUSIC_CIRCLE_button.PNG')
    musicButton = pg.transform.scale(musicButton, (int(musicButton.get_width()/2),int(musicButton.get_height()/2)))
    spellButton = pg.image.load('images/DMTB_SPELLS_CIRCLE_button.PNG')
    spellButton = pg.transform.scale(spellButton, (int(spellButton.get_width()/2),int(spellButton.get_height()/2)))
    monstButton = pg.image.load('images/DMTB_MONSTER_CIRCLE_button.PNG')
    monstButton = pg.transform.scale(monstButton, (int(monstButton.get_width()/2),int(monstButton.get_height()/2)))
    buttons = [npcButton,musicButton,spellButton,monstButton]
    buttons.remove(buttons[choice-2])
    rects = []
    for i in range(len(buttons)):
        surf.blit(buttons[i], (int(buttons[i].get_width()*(1.5+i)),0))
        rects.append(buttons[i].get_rect(topleft = (int(buttons[i].get_width()*(1.5+i)),0)))
    
    return(surf,buttons,rects)
    
    
    
