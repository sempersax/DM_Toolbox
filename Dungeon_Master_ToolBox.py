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
import Char_Navigator as charNav
import NPC_Generator as npcGen
import PC_Generator as pcGen
import Spell_Navigator as spNav
import Monster_Navigator as monNav
import Image_Loader as imgLoad
import monsterCardDMTB as mc

from pygame.locals import *

import datetime

global WINDOWHEIGHT, WINDOWWIDTH


WINDOWWIDTH = 1000
WINDOWHEIGHT = 629
##infoObject = pg.display.Info()
##
##WINDOWWIDTH = infoObject.current_w
##WINDOWHEIGHT = infoObject.current_h
FPS = 30


## Legend:
## choice = 0 -> Main Menu
## choice = 1 -> Tool Screen
## choice = 2 -> Character Screen
## choice = 3 -> Music Screen
## choice = 4 -> Spell Screen
## choice = 5 -> Monster Screen
## choice = 6 -> NPC Screen (FROM CHARACTER SCREEN)
## choice = 7 -> PC Screen (FROM CHARACTER SCREEN)

def main():
    global WINDOWHEIGHT, WINDOWWIDTH,FPSCLOCK

    pg.init()
    pg.mixer.init()
    FPSCLOCK = pg.time.Clock()
    DISPLAYSURF = pg.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),HWSURFACE | DOUBLEBUF|RESIZABLE)
    surfs = [DISPLAYSURF]
    pg.display.set_caption('Dungeon Master Toolbox')
    loadingScreen = pg.image.load('images/Loading_screen.jpg')
    loadingScreen = pg.transform.scale(loadingScreen, (WINDOWWIDTH,WINDOWHEIGHT))
    DISPLAYSURF.blit(loadingScreen,(0,0))
    pg.display.update()
    pos = (0,0)

    # This is the heart of the program - all of these key value pairs tell the program which function to call and when
    dispatcher = {
        "menu" : menGen.createMenu,
        "quest" : toolNav.createTools,
        "characters" : charNav.createChar,
        "NPC" : npcGen.race,
        "gender" : npcGen.gender,
        "name" : npcGen.name,
        "music" : musNav.createMusic,
        "tavern" : musGen.tavernMusic,
        "battle" : musGen.battleMusic,
        "region" : None,
        "spells" : spNav.createSpell,
        "monsters" : monNav.createMonster,
        "alphabet" : monNav.AZSelector
        }
    KEYOLD = ''
    BACKKEY = ''
    KEY = 'menu'
    KEYS = []
    startTime = datetime.datetime.now()

    while True:           
        checkForQuit()
        runTime = datetime.datetime.now() - startTime
        elapsed = runTime.total_seconds()
        if  KEY == 'menu' and elapsed >= 3. :
            surfs, rects, KEYS = dispatcher[KEY](surfs)
            DISPLAYSURF = surfs[0]
            pg.display.update()

            startTime = datetime.datetime.now()

        for event in pg.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    terminate()
            if event.type == MOUSEBUTTONUP:
                pos = pg.mouse.get_pos()
                for i in range(0, len(rects)):
                    if rects[i].collidepoint(event.pos):
                        KEY = KEYS[i]

        if KEY != KEYOLD:
            surfs.append(pos)
            surfs, rects, KEYS = dispatcher[KEY](surfs)
            DISPLAYSURF = surfs[0]
            if KEY != 'menu':
                DISPLAYSURF, menRect = menGen.reachMenu(DISPLAYSURF)
                surfs[0], backRect = toolNav.createBack(surfs)
                surfs[0], miniKeys, miniRects = toolNav.createMiniTools(surfs,KEY)
                KEYS.append('menu')
                KEYS = KEYS+miniKeys
                rects = rects + backRect+menRect+miniRects

            pg.display.update()
        KEYOLD = KEY
        #print(keyold,key)

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
