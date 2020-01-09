# Dungeon Master Toolbox
# By Torrey Saxton
# This is the main program.  Currently handles all events.

import pygame as pg
import random
import os
import sys
import numpy as np
import Menu_Generator as menGen
import Music_Generator as musGen
import Music_Controls as musCon
import Tool_Navigator as toolNav
import Music_Navigator as musNav
import pygame.surfarray as surfarray
import NPC_Navigator as npcNav
import NPC_Generator as npcGen
import Spell_Navigator as spNav
import Monster_Navigator as monNav
from pygame.locals import *

import time

WINDOWWIDTH = 1000
WINDOWHEIGHT = 629
FPS = 30

## Legend:
## choice = 0 -> Main Menu
## choice = 1 -> Tool Screen
## choice = 2 -> NPC Screen
## choice = 3 -> Music Screen
## choice = 4 -> Spell Screen
## choice = 5 -> Monster Screen
## choice = 6 -> Race Screen (FROM NPC SCREEN)
def main():
    global WINDOWHEIGHT, WINDOWWIDTH,FPSCLOCK
    pg.init()
    pg.mixer.init()
    choice = 0
    choiceold = -10
    musicChoice = 1
    musicChoiceold = -10
    menuScreen = 1
    playing = True
    FPSCLOCK = pg.time.Clock()
    DISPLAYSURF = pg.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),HWSURFACE | DOUBLEBUF|RESIZABLE)
    runTime = 0.
    startTime = time.time()
    while True:
        runTime = runTime + time.time() - startTime
        if runTime >= 600. and choice == 0 :
            menuScreen = np.random.randint(menuScreens)
            startTime = time.time()
            runTime = 0.
            
        checkForQuit()
        if choice == 0:
            DISPLAYSURF, questSurf, questRect,menuScreens = menGen.createMenu(DISPLAYSURF,menuScreen)
            if choice != choiceold:
                musGen.menuMusic()
        DISPLAYSURF, soundSurf, soundRect, playing = musCon.soundControl(DISPLAYSURF, musicChoice, pg.mixer.music.get_busy())
        if choice != 0:
            DISPLAYSURF, menButton, menRect = menGen.reachMenu(DISPLAYSURF)
        if choice >1:
            DISPLAYSURF, backButton, backRect = toolNav.createBack(DISPLAYSURF)
        
            DISPLAYSURF, miniButtons, miniRects = toolNav.createMiniTools(DISPLAYSURF,choice)

        
        for event in pg.event.get():
            if event.type == MOUSEBUTTONUP:
                if soundRect.collidepoint(event.pos):
                    musicChoice = np.remainder(musicChoice+1,2)
                    DISPLAYSURF, soundSurf, soundRect, playing = musCon.soundControl(DISPLAYSURF, musicChoice, pg.mixer.music.get_busy())
                    if playing == False:
                        pg.mixer.music.pause()
                    elif playing == True:
                        pg.mixer.music.unpause()
                if choice == 0:
                    if questRect.collidepoint(event.pos):
                        DISPLAYSURF, npcSurf,npcRect,musicSurf,musicRect,spellSurf,spellRect,monstSurf,monstRect = toolNav.createTools(DISPLAYSURF)
                        choice = 1
                        break
                if choice != 0:
                    DISPLAYSURF, menButton, menRect = menGen.reachMenu(DISPLAYSURF)           
                    if menRect.collidepoint(event.pos):
                        DISPLAYSURF, questSurf, questRect,menuScreens = menGen.createMenu(DISPLAYSURF,menuScreen)
                        musGen.menuMusic()
                        choice = 0
                        break
                if choice == 1: #on main hub
                    if musicRect.collidepoint(event.pos):
                        DISPLAYSURF,tavrnSurf, tavrnRect, bttleSurf, bttleRect, rgionSurf, rgionRect = musNav.createMusic(DISPLAYSURF)
                        choice = 3
                        break
                    if npcRect.collidepoint(event.pos):
                        DISPLAYSURF,racesurf, raceRect = npcNav.createNPC(DISPLAYSURF)
                        choice = 2
                        break
                    if spellRect.collidepoint(event.pos):
                        DISPLAYSURF, surf1, rect1 = spNav.createSpell(DISPLAYSURF)
                        choice = 4
                        break
                    if monstRect.collidepoint(event.pos):
                        DISPLAYSURF, surf1, rect1 = monNav.createMonster(DISPLAYSURF)
                        choice = 5
                        break                        

                if choice == 2: #on npc hub
                    if miniRects[0].collidepoint(event.pos):
                        DISPLAYSURF,tavrnSurf, tavrnRect, bttleSurf, bttleRect, rgionSurf, rgionRect = musNav.createMusic(DISPLAYSURF)
                        choice = 3
                        break                       
                    if miniRects[1].collidepoint(event.pos):
                        DISPLAYSURF, surf1, rect1 = spNav.createSpell(DISPLAYSURF)
                        choice = 4
                        break
                    if miniRects[2].collidepoint(event.pos):
                        DISPLAYSURF, surf1, rect1 = monNav.createMonster(DISPLAYSURF)
                        choice = 5
                        break
                    if raceRect.collidepoint(event.pos):
                        DISPLAYSURF, races = npcGen.race(DISPLAYSURF)
                        subchoice = 6
                        break
                    
                if choice == 3: # on music hub
                    if bttleRect.collidepoint(event.pos):
                        musGen.battleMusic()
                    if tavrnRect.collidepoint(event.pos):
                        musGen.tavernMusic()
                    if miniRects[0].collidepoint(event.pos):
                        DISPLAYSURF,racesurf, raceRect = npcNav.createNPC(DISPLAYSURF)
                        choice = 2
                        break
                    if miniRects[1].collidepoint(event.pos):
                        DISPLAYSURF, surf1, rect1 = spNav.createSpell(DISPLAYSURF)
                        choice = 4
                        break
                    if miniRects[2].collidepoint(event.pos):
                        DISPLAYSURF, surf1, rect1 = monNav.createMonster(DISPLAYSURF)
                        choice = 5
                        break
                    
                if choice == 4: #on Spell hub        
                    if miniRects[0].collidepoint(event.pos):
                        DISPLAYSURF,racesurf, raceRect = npcNav.createNPC(DISPLAYSURF)
                        choice = 2
                        break                       
                    if miniRects[1].collidepoint(event.pos):
                        DISPLAYSURF,tavrnSurf, tavrnRect, bttleSurf, bttleRect, rgionSurf, rgionRect = musNav.createMusic(DISPLAYSURF)
                        choice = 3
                        break        
                    if miniRects[2].collidepoint(event.pos):
                        DISPLAYSURF, surf1, rect1 = monNav.createMonster(DISPLAYSURF)
                        choice = 5
                        break

                if choice == 5: #on Monster Hub
                    if miniRects[0].collidepoint(event.pos):
                        DISPLAYSURF,racesurf, raceRect = npcNav.createNPC(DISPLAYSURF)
                        choice = 2
                        break                       
                    if miniRects[1].collidepoint(event.pos):
                        DISPLAYSURF,tavrnSurf, tavrnRect, bttleSurf, bttleRect, rgionSurf, rgionRect = musNav.createMusic(DISPLAYSURF)
                        choice = 3
                        break        
                    if miniRects[2].collidepoint(event.pos):
                        DISPLAYSURF, surf1, rect1 = spNav.createSpell(DISPLAYSURF)
                        choice = 4
                        break                   

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
        checkForQuit()
        

        choiceold = choice
        musicChoiceold = musicChoice
        pg.display.update()

def terminate():
    pg.quit()
    sys.exit()

def checkForQuit():
    for event in pg.event.get(QUIT):
        terminate()
    for event in pg.event.get(KEYUP):
        if event.key == K_ESCAPE:
            terminate()
        pg.event.post(event)

if __name__ == '__main__':
    main()
