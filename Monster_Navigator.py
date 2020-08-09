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
import monsterCardDMTB as mc
from itertools import groupby
from operator import itemgetter

##WINDOWHEIGHT = 629
##WINDOWWIDTH = 1000

def monsterLetterFilter(SURFS):
    pg.init()
    surf = SURFS[0]
    fullMonsterNames = SURFS[1]
    monsterNames = SURFS[2]
    letters = SURFS[3]
    prevKey = SURFS[5]
    pos = SURFS[-1]
    WINDOWWIDTH = surf.get_width()
    WINDOWHEIGHT = surf.get_height()


    if prevKey == 'alphabet' or prevKey == 'letters':
        shift = SURFS[4]
        print('shift = ', shift)

    if prevKey == 'alphabet':
        for i in range(0, len(letters)):
            if letters[i].collidepoint(pos):
                monsterNames = monsterNames[i]
    if prevKey == 'monsterStats':
        shift = SURFS[4][0]
        print(monsterNames)
        print('shift = ', shift)

    FONT = pg.font.Font('fonts/GimletSSK.ttf', 16)

    monstSurf = pg.image.load('images/DMTB_MONSTERS_screen.jpg')
    monstSurf = pg.transform.scale(monstSurf, (WINDOWWIDTH,WINDOWHEIGHT))
    surf.fill((0,0,0))
    surf.blit(monstSurf,(0,0))
    template = pg.image.load('images/blank_button.png')
    template = pg.transform.scale(template, (int(template.get_width()/8),int(template.get_height()/8)))

    rightButton = pg.image.load('images/forward-circle_button.png')
    rightButton = pg.transform.scale(rightButton,(int(rightButton.get_width()/2),int(rightButton.get_height()/2)))
    
    leftButton = pg.image.load('images/back-circle_button.png')
    leftButton = pg.transform.scale(leftButton,(int(leftButton.get_width()/2),int(leftButton.get_height()/2)))

    rects = []
    surfs = []
    names = []
    columns =int((WINDOWWIDTH-200)//200)
    rows = int((WINDOWHEIGHT-100)//100)
    grid = columns * rows

    
    if grid *(1+shift) < len(monsterNames):
        rightRect = rightButton.get_rect(topleft = (int(surf.get_width()-1.5*rightButton.get_width()),int(surf.get_height()//2-rightButton.get_height()/2-20)))
        surf.fill((0,0,0))
        surf.blit(monstSurf,(0,0))

        surf.blit(rightButton,(int(surf.get_width()-1.5*rightButton.get_width()),int(surf.get_height()//2-rightButton.get_height()/2-20)))
        if rightRect.collidepoint(pos):
            shift += 1

    if shift > 0:
        leftRect = leftButton.get_rect(topleft = (int(.25*leftButton.get_width()),int(surf.get_height()//2-leftButton.get_height()/2-20)))
        surf.fill((0,0,0))
        surf.blit(monstSurf,(0,0))


        surf.blit(leftButton,(int(0.25*leftButton.get_width()),int(surf.get_height()//2-leftButton.get_height()/2-20)))
        if leftRect.collidepoint(pos):
            rightRect = rightButton.get_rect(topleft = (int(surf.get_width()-1.5*rightButton.get_width()),int(surf.get_height()//2-rightButton.get_height()/2-20)))
            surf.blit(rightButton,(int(surf.get_width()-1.5*rightButton.get_width()),int(surf.get_height()//2-rightButton.get_height()/2-20)))

            shift -=1
        if shift == 0:
            surf.fill((0,0,0))
            surf.blit(monstSurf,(0,0))
        if grid *(1+shift) < len(monsterNames):
            surf.blit(rightButton,(int(surf.get_width()-1.5*rightButton.get_width()),int(surf.get_height()//2-rightButton.get_height()/2-20)))
        


    amount = 0    
    for i in range(0,columns):
        for j in range(0,rows):
            amount+=1
            if i*rows+j+grid*shift > len(monsterNames)-1:
                amount -= 1
                break
            names.append(FONT.render(monsterNames[i*rows+j+grid*shift],True,[237,190,141],None))
            surfs.append(template)
            rects.append(surfs[i*rows+j].get_rect(topleft = (int(70+surfs[i*rows+j].get_width()*(1/8+i)),int(70+surfs[i*rows+j].get_height()*(1/8+j)))))
            surf.blit(surfs[i*rows+j],(int(70+surfs[i*rows+j].get_width()*(1/8+i)),int(70+surfs[i*rows+j].get_height()*(1/8+j))))
            surf.blit(names[i*rows+j], (int(-names[i*rows+j].get_width()//2+95+surfs[i*rows+j].get_width()*(1/2+i)),int(70+surfs[i*rows+j].get_height()*(1/2+j))))



    keys = ["monsterStats"]*(amount)

    if grid *(1+shift) < len(monsterNames):
        rects.append(rightRect)
        keys.append('right')

    if shift > 0:
        rects.append(leftRect)
        keys.append('left')
    
    keys.append("alphabet")
    surfs = [surf,fullMonsterNames,monsterNames,rects,shift,'letters',grid*shift]
    return(surfs,rects, keys)

def AZSelector(SURFS):
    pg.init()
    surf = SURFS[0]
    monsterNames = SURFS[1]
    WINDOWWIDTH = surf.get_width()
    WINDOWHEIGHT = surf.get_height()

    monstSurf = pg.image.load('images/DMTB_MONSTERS_screen.jpg')
    monstSurf = pg.transform.scale(monstSurf, (WINDOWWIDTH,WINDOWHEIGHT))
    surf.fill((0,0,0))
    surf.blit(monstSurf,(0,0))

    images = []
    cwd = os.getcwd()
    mypath = "{}/images/filters/letters/".format(cwd)
    myLetters = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath,f))]
    rects = []
    surfs = []
    height = surf.get_height()
    shift = 0
    yedge = surf.get_height()//6
    xedge = surf.get_width()//5
    j=0
    for i in range(0,len(myLetters)):
        surfs.append(pg.image.load(mypath+myLetters[i]))
        if int(3* yedge+surfs[i].get_height()*(1/8 +i-j )) > surf.get_height():
            shift +=1
            j = i
        rects.append(surfs[i].get_rect(topleft = (int(xedge+surfs[i].get_width()*(1/8 +shift )), int(yedge+surfs[i].get_height()*(1/8+i-j)))))
        surf.blit(surfs[i],(int(xedge+surfs[i].get_width()*(1/8 +shift )), int(yedge+surfs[i].get_height()*(1/8+i-j))))

    surfs = [surf,monsterNames, monsterNames,rects,0,'alphabet']
    keys = ['letter']*len(rects)
    keys.append('monsters')
    return(surfs,rects,keys)

def createMonster(SURFS):
    pg.init()
    surf = SURFS[0]
    WINDOWWIDTH = surf.get_width()
    WINDOWHEIGHT = surf.get_height()

    start = time.time()
    rosterPath = "{}/MonsterScrape/monsterRoster.txt".format(os.getcwd())

    alphaCR = []
    tempAlphaCR = []
    temp = []
    with open(rosterPath, 'r') as roster:
        for line in roster:
            currentPlace = line[:-1].split(',')
            currentPlace[0] = currentPlace[0].replace('[','').replace(']','').replace("'","").replace('"','')
            currentPlace[1] = currentPlace[1].replace('[','').replace(']','').replace("'","").replace(' ','').replace('l','1').replace('"','')
            try:
                currentPlace[1] = int(currentPlace[1])
            except:
                currentPlace[1] = float(Fraction(currentPlace[1]))
            alphaCR.append(currentPlace)
    tempAlphaCR = [i[0] for i in alphaCR]
    temp1 = []
    temp2 = []
    for letter, words in groupby(tempAlphaCR, key = itemgetter(0)):
        for word in words:
            temp1.append(word)
        temp2.append(temp1)
        temp1 = []

    alphaCR = temp2


    searchSurf = pg.image.load('images/music_Button.png')
    searchSurf = pg.transform.scale(searchSurf, (int(searchSurf.get_width()/8),int(searchSurf.get_height()/8)))
    searchRect = searchSurf.get_rect(topleft = (int(searchSurf.get_width()*1/5), int(WINDOWHEIGHT/4) - int(searchSurf.get_height()/2)))

    AZSurf = pg.image.load('images/filters/A-Z_Button.png')
    AZSurf = pg.transform.scale(AZSurf, (int(AZSurf.get_width()/8),int(AZSurf.get_height()/8)))
    AZRect = searchSurf.get_rect(topleft = (surf.get_width()/2-int(AZSurf.get_width()/2), int(WINDOWHEIGHT/3*2) - int(AZSurf.get_height()/2)))

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

    surfs = [surf, alphaCR]
    rects = [searchRect, AZRect, CRRect]
    keys = ['search', 'alphabet', 'cr', 'quest']
    return(surfs, rects, keys)
