# Dungeon Master Toolbox
# By Torrey Saxton

import pygame as pg
import random
import os
import sys
import numpy as np
import Menu_Generator as menu
import Music_Generator as musgen
import Music_Controls as muscon
import Tool_Navigator as tn
import Music_Navigator as musnav
import pygame.surfarray as surfarray
import NPC_Navigator as npcNav
from pygame.locals import *

import time

WINDOWWIDTH = 1000
WINDOWHEIGHT = 629
FPS = 30

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
            DISPLAYSURF, questSurf, questRect,menuScreens = menu.createMenu(DISPLAYSURF,menuScreen)
            if choice != choiceold:
                musgen.menuMusic()
        DISPLAYSURF, soundSurf, soundRect, playing = muscon.soundControl(DISPLAYSURF, musicChoice, pg.mixer.music.get_busy())
        if choice != 0:
            DISPLAYSURF, menButton, menRect = menu.reachMenu(DISPLAYSURF)
        if choice >1:
            DISPLAYSURF, backButton, backRect = tn.createBack(DISPLAYSURF)
            DISPLAYSURF, miniButtons, miniRects = tn.createMiniTools(DISPLAYSURF,choice)

        
        for event in pg.event.get():
            if event.type == MOUSEBUTTONUP:
                if soundRect.collidepoint(event.pos):
                    musicChoice = np.remainder(musicChoice+1,2)
                    DISPLAYSURF, soundSurf, soundRect, playing = muscon.soundControl(DISPLAYSURF, musicChoice, pg.mixer.music.get_busy())
                    if playing == False:
                        pg.mixer.music.pause()
                    elif playing == True:
                        pg.mixer.music.unpause()
                if questRect.collidepoint(event.pos):
                    DISPLAYSURF, npcSurf,npcRect,musicSurf,musicRect,spellSurf,spellRect,monstSurf,monstRect = tn.createTools(DISPLAYSURF)
                    choice = 1
                    break
                if choice != 0:
                    DISPLAYSURF, menButton, menRect = menu.reachMenu(DISPLAYSURF)           
                    if menRect.collidepoint(event.pos):
                        DISPLAYSURF, questSurf, questRect,menuScreens = menu.createMenu(DISPLAYSURF,menuScreen)
                        musgen.menuMusic()
                        choice = 0
                        break
                if choice == 1: #on main hub
                    if musicRect.collidepoint(event.pos):
                        DISPLAYSURF,tavrnSurf, tavrnRect, bttleSurf, bttleRect, rgionSurf, rgionRect = musnav.createMusic(DISPLAYSURF)
                        choice = 3
                        break
                    if npcRect.collidepoint(event.pos):
                        DISPLAYSURF,racesurf, raceRect = npcNav.createNPC(DISPLAYSURF)
                        choice = 2
                        break

                if choice == 2: #on npc hub
                    if miniRects[0].collidepoint(event.pos):
                        DISPLAYSURF,tavrnSurf, tavrnRect, bttleSurf, bttleRect, rgionSurf, rgionRect = musnav.createMusic(DISPLAYSURF)
                        choice = 3
                        break                       
                
                if choice == 3: # on music hub
                    if bttleRect.collidepoint(event.pos):
                        musgen.battleMusic()
                    if tavrnRect.collidepoint(event.pos):
                        musgen.tavernMusic()
                    if miniRects[0].collidepoint(event.pos):
                        DISPLAYSURF,racesurf, raceRect = npcNav.createNPC(DISPLAYSURF)
                        choice = 2
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
