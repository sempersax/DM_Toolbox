# This is for the main screen that the DM navigates to tools in.  Creates
# the screen and the relevant buttons (NPCs, Music, Spells, Monsters)
# Each of which will have their own navigation screen later on.

import pygame as pg
import random
import os
import numpy as np
import pygame.surfarray as surfarray
from pygame.locals import *

def createTools(SURFS):
    pg.init()
    surf = SURFS[0]
    WINDOWWIDTH = surf.get_width()
    WINDOWHEIGHT = surf.get_height()
    buttonFiles = os.listdir('images/tools')
    prefix = ['images/tools/']*len(buttonFiles)

    buttonFiles = [k for k in buttonFiles if not 'CIRCLE' in k]
    buttons = [None]*len(buttonFiles)
    for i in range(len(buttonFiles)):
        buttonFiles[i] = prefix[i]+buttonFiles[i]
        buttons[i] = pg.image.load(buttonFiles[i])
        buttons[i] = pg.transform.scale(buttons[i], (int(buttons[i].get_width()/8),int(buttons[i].get_height()/8)))
        
# Character Button
    charSurf = buttons[2]
    charRect = charSurf.get_rect(topleft = (int(charSurf.get_width()*1/5), int(WINDOWHEIGHT/4) - int(charSurf.get_height()/2)))
# Music Button
    musicSurf = buttons[1]
    musicRect = musicSurf.get_rect(topleft = (WINDOWWIDTH - int(musicSurf.get_width()*6/5), int(WINDOWHEIGHT/4) - int(musicSurf.get_height()/2)))
# Spell Button
    spellSurf = buttons[3]
    spellRect = spellSurf.get_rect(topleft = (int(spellSurf.get_width()*1/5), int(WINDOWHEIGHT*3/4) + int(spellSurf.get_height()/2)))
# Monster Button
    monstSurf = buttons[0]
    monstRect = monstSurf.get_rect(topleft = (WINDOWWIDTH - int(monstSurf.get_width()*6/5), int(WINDOWHEIGHT*3/4) + int(monstSurf.get_height()/2)))

    toolSurf = pg.image.load('images/navigation_screen.png')
    toolSurf = pg.transform.scale(toolSurf, (WINDOWWIDTH,WINDOWHEIGHT))
    surf.fill((0,0,0))
    surf.blit(toolSurf,(0,0))
    surf.blit(charSurf, (int(charSurf.get_width()*1/5), int(WINDOWHEIGHT/4) - int(charSurf.get_height()/2)))
    surf.blit(musicSurf, (WINDOWWIDTH - int(musicSurf.get_width()*6/5), int(WINDOWHEIGHT/4) - int(musicSurf.get_height()/2)))
    surf.blit(spellSurf, (int(spellSurf.get_width()*1/5), int(WINDOWHEIGHT*3/4) + int(spellSurf.get_height()/2)))
    surf.blit(monstSurf, (WINDOWWIDTH - int(monstSurf.get_width()*6/5), int(WINDOWHEIGHT*3/4) + int(monstSurf.get_height()/2)))

    rects = [charRect,musicRect,spellRect,monstRect]
    keys = ['characters', 'music', 'spells', 'monsters','menu']
    surfs = [surf]
    return(surfs,rects,keys)

#This is to create a back button, to go back a single screen
def createBack(SURFS):
    pg.init()
    surf = SURFS[0]
    WINDOWWIDTH = surf.get_width()
    WINDOWHEIGHT = surf.get_height()
    backButton = pg.image.load('images/back-circle_button.png')
    backButton = pg.transform.scale(backButton, (int(backButton.get_width()/2),int(backButton.get_height()/2)))
    backRect = backButton.get_rect(topleft =  (int(WINDOWWIDTH-backButton.get_width()*2.7),5))
    surf.blit(backButton, (int(WINDOWWIDTH-backButton.get_width()*2.7),5))
    backRect = [backRect]
    return(surf,backRect)

# This is to create the other 3 buttons so one can switch categories quickly
# All 4 are create, but based on choice, one is not blit to the screen
def createMiniTools(SURFS,choice):
    pg.init()
    surf = SURFS[0]
    toolFiles = os.listdir('images/tools')
    circTools = [k for k in toolFiles if 'CIRCLE' in k]
    prefix = ['images/tools/']*len(toolFiles)
    circs = [None]*len(circTools)
    for i in range(len(circTools)): #this loads all of the tool images at once.
        circTools[i] = prefix[i]+circTools[i]
        circs[i] = pg.image.load(circTools[i])
        circs[i] = pg.transform.scale(circs[i], (int(circs[i].get_width()/2),int(circs[i].get_height()/2)))

    buttons = circs    
    npcButton = buttons[2]
    musicButton = buttons[1]
    spellButton = buttons[3]
    monstButton = buttons[0]
    buttons = [npcButton,musicButton,spellButton,monstButton]
    miniKeys = ['characters','music','spells','monsters']
    if choice == 'characters' or choice == 'NPC' or choice == 'gender' or choice == 'name' or choice == 'continue' or choice == 'player':
        buttons.remove(buttons[0])
        miniKeys.remove(miniKeys[0])
    if choice == 'spells' or choice == 'class' or choice == 'levels' or choice == 'levelNumbers' or choice == 'spellLeft' or choice == 'spellRight' or choice == 'spellDesc' or choice == 'classChose':
        buttons.remove(buttons[2])
        miniKeys.remove(miniKeys[2])
    if choice == 'music' or choice == 'tavern' or choice == 'battle' or choice == 'region':
        buttons.remove(buttons[1])
        miniKeys.remove(miniKeys[1])
    if choice == 'monsters' or choice == 'alphabet' or choice == 'letter' or choice == 'right' or choice == 'left' or choice == 'monsterStats' or choice == 'cr':
        buttons.remove(buttons[3])
        miniKeys.remove(miniKeys[3])
    rects = []
    for i in range(len(buttons)):
        surf.blit(buttons[i], (int(buttons[i].get_width()*(1.5+i)),0))
        rects.append(buttons[i].get_rect(topleft = (int(buttons[i].get_width()*(1.5+i)),0)))

    print(miniKeys)

    return(surf,miniKeys,rects)
    
    
    
