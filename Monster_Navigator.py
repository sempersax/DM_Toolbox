# This is for the main screen that the DM navigates to for creating Monsters in.  Creates
# the screen and the relevant buttons 
# Each of which will have their own navigation screen later on.

import pygame as pg
import random
import os
import numpy as np
import pygame.surfarray as surfarray
from pygame.locals import *
import time
import json
from fractions import Fraction

WINDOWHEIGHT = 629
WINDOWWIDTH = 1000

def createMonster(surf):
    pg.init()

    start = time.time()
    rosterPath = "{}/MonsterScrape/monsterRoster.txt".format(os.getcwd())

    alphaCR = []
    with open(rosterPath, 'r') as roster:
        for line in roster:
            currentPlace = line[:-1].split(',')
            currentPlace[0] = currentPlace[0].replace('[','').replace(']','').replace("'","").replace(' ','')
            currentPlace[1] = currentPlace[1].replace('[','').replace(']','').replace("'","").replace(' ','').replace('l','1')
            #print(currentPlace[0])
            try:
                currentPlace[1] = int(currentPlace[1])
            except:
                currentPlace[1] = float(Fraction(currentPlace[1]))
            alphaCR.append(currentPlace)

    #print(alphaCR)
# Tavern Button
    searchSurf = pg.image.load('images/music_Button.png')
    searchSurf = pg.transform.scale(searchSurf, (int(searchSurf.get_width()/8),int(searchSurf.get_height()/8)))
    searchRect = searchSurf.get_rect(topleft = (int(searchSurf.get_width()*1/5), int(WINDOWHEIGHT/4) - int(searchSurf.get_height()/2)))

    AZSurf = pg.image.load('images/filters/A-Z_Button.png')
    AZSurf = pg.transform.scale(AZSurf, (int(AZSurf.get_width()/8),int(AZSurf.get_height()/8)))
    AZRect = searchSurf.get_rect(topleft = (int(AZSurf.get_width()*1/5), int(WINDOWHEIGHT/4) - int(AZSurf.get_height()/2)))

    CRSurf = pg.image.load('images/filters/CR_Button.png')
    CRSurf = pg.transform.scale(CRSurf, (int(CRSurf.get_width()/8),int(CRSurf.get_height()/8)))
    CRRect = searchSurf.get_rect(topleft = (int(CRSurf.get_width()*1/5), int(WINDOWHEIGHT/4) - int(CRSurf.get_height()/2)))

    monstSurf = pg.image.load('images/DMTB_MONSTERS_screen.jpg')
    monstSurf = pg.transform.scale(monstSurf, (WINDOWWIDTH,WINDOWHEIGHT))
    surf.fill((0,0,0))
    surf.blit(monstSurf,(0,0))
    surf.blit(searchSurf, (int(searchSurf.get_width()*1/5), int(WINDOWHEIGHT/4) - int(searchSurf.get_height()/2)))
    surf.blit(AZSurf, (surf.get_width()/2-int(AZSurf.get_width()/2), int(WINDOWHEIGHT/3*2) - int(AZSurf.get_height()/2)))
    surf.blit(CRSurf, (surf.get_width()-int(CRSurf.get_width()*6/5), int(WINDOWHEIGHT/4) - int(searchSurf.get_height()/2)))
    
    return(surf, searchSurf, searchRect, AZSurf, AZRect, monstSurf)
