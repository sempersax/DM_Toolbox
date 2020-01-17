import numpy as np
import os
import pygame as pg
import time
import NPC_Roster as roster
import NPC_Navigator as npcNav
def race(surf,races):
    pg.init()
    start = time.time()
    raceRects = []
##    start1 = time.time()
##    for i in range(len(files)): #this loads all of the race images at once.
##        races.append(pg.image.load('images/races/'+files[i]))
##        races[i] = pg.transform.scale(races[i], (int(races[i].get_width()/8),int(races[i].get_height()/8)))
##    print('image load time = ',time.time()-start1)
    surf.fill((0,0,0))
    surf.blit(pg.image.load('images/navigation_screen.png'),(0,0))
    start2=time.time()
    for i in range(int(np.ceil(len(races)/4))):
        for j in range(4):
            if(j+i*4)>= len(races):
                break
            position = (int(races[i].get_width()*(1+i)),int(races[i].get_height()*(1.3+j)))
            surf.blit(races[j+i*4], position)
            raceRects.append(races[i].get_rect(topleft = position))
    RACERECTS = raceRects[0].unionall(raceRects[1:])
    return(surf,races,raceRects,RACERECTS)

def gender(surf,WINDOWWIDTH,WINDOWHEIGHT,rects,pos,genders):
    pg.init()
    races = ['DRAGONBORN','DWARF','ELF','GNOME','GOBLIN','HALF-ELF','HALF-ORC','HALFLING','HUMAN','ORC']
    raceSel = 'None'
    for i in range(len(rects)):
        if rects[i].collidepoint(pos):
            raceSel = races[i]

    if raceSel != 'None':
        surf.blit(pg.image.load('images/navigation_screen.png'),(0,0))
    genRects = []
    for i in range(len(genders)):
        position=(int(WINDOWWIDTH*i/4+genders[i].get_width()*(i+1)),int(WINDOWHEIGHT/2-genders[i].get_height()/2))
        if raceSel != 'None':
            surf.blit(genders[i], position)
        genRects.append(genders[i].get_rect(topleft = position))
    GENRECTS = genRects[0].unionall(genRects[1:])                
    return(surf,raceSel,genRects,GENRECTS)
        
def name(surf,WINDOWWIDTH,WINDOWHEIGHT,rects,pos,raceSel,Scroll):
    pg.init()
    FONT = pg.font.Font('freesansbold.ttf', 24)
    genders = ['FEMALE', 'MALE']
    scroll = Scroll
    for i in range(len(rects)):
        if rects[i].collidepoint(pos):
            genderSel = genders[i]

    if raceSel == 'DRAGONBORN':
        if genderSel == 'FEMALE':
            first=roster.dragonBornFemaleNames()
            last = roster.dragonBornLastNames()
        if genderSel == 'MALE':
            first = roster.dragonBornMaleNames()
            last = roster.dragonBornLastNames()

    if raceSel == 'DWARF':
        if genderSel == 'FEMALE':
            first=roster.dwarfFemaleNames()
            last = roster.dwarfLastNames()
        if genderSel == 'MALE':
            first = roster.dwarfMaleNames()
            last = roster.dwarfLastNames()

    if raceSel == 'ELF':
        if genderSel == 'FEMALE':
            first=roster.elfFemaleNames()
            last = roster.elfLastNames()
        if genderSel == 'MALE':
            first = roster.elfMaleNames()
            last = roster.elfLastNames()

    if raceSel == 'GNOME':
        if genderSel == 'FEMALE':
            first=roster.gnomeFemaleNames()
            last = roster.gnomeLastNames()
        if genderSel == 'MALE':
            first = roster.gnomeMaleNames()
            last = roster.gnomeLastNames()

    if raceSel == 'GOBLIN':
        if genderSel == 'FEMALE':
            first=roster.goblinFemaleNames()
            last = roster.goblinLastNames()
        if genderSel == 'MALE':
            first = roster.goblinMaleNames()
            last = roster.goblinLastNames()

    if raceSel == 'HALF-ELF':
        if genderSel == 'FEMALE':
            first=roster.hElfFemaleNames()
            last = roster.hElfLastNames()
        if genderSel == 'MALE':
            first = roster.hElfMaleNames()
            last = roster.hElfLastNames()

    if raceSel == 'HALFLING':
        if genderSel == 'FEMALE':
            first=roster.halflingFemaleNames()
            last = roster.halflingLastNames()
        if genderSel == 'MALE':
            first = roster.halflingMaleNames()
            last = roster.halflingLastNames()

    if raceSel == 'HALF-ORC':
        if genderSel == 'FEMALE':
            first=roster.hOrcFemaleNames()
            last = roster.hOrcLastNames()
        if genderSel == 'MALE':
            first = roster.hOrcMaleNames()
            last = roster.hOrcLastNames()

    if raceSel == 'HUMAN':
        if genderSel == 'FEMALE':
            first=roster.humanFemaleNames()
            last = roster.humanLastNames()
        if genderSel == 'MALE':
            first = roster.humanMaleNames()
            last = roster.humanLastNames()

    if raceSel == 'ORC':
        if genderSel == 'FEMALE':
            first=roster.orcFemaleNames()
            last = roster.orcLastNames()
        if genderSel == 'MALE':
            first = roster.orcMaleNames()
            last = roster.orcLastNames()

    raceText = FONT.render('    RACE: '+raceSel,True,[255,255,255],None)
    genText = FONT.render('GENDER: ' + genderSel, True,[255,255,255],None)
    nameText = FONT.render('    NAME: ' + first + ' ' + last, True,[255,255,255],None)
    DISPLAYSURF = surf
    scroll = pg.transform.scale(scroll, (int(scroll.get_width()*2/3),int(scroll.get_height()*2/3)))
    surf.blit(scroll,(int(scroll.get_width()/4),int(scroll.get_height()/8)))
    surf.blit(raceText,(int(scroll.get_width()/4+50),int(scroll.get_height()/8+4.5*raceText.get_height())))
    surf.blit(genText,(int(scroll.get_width()/4+50),int(scroll.get_height()/8+5.5*genText.get_height())))
    surf.blit(nameText,(int(scroll.get_width()/4+50),int(scroll.get_height()/8+6.5*nameText.get_height())))
    cont = pg.image.load('images/music_Button.png')
    cont = pg.transform.scale(cont,(int(cont.get_width()/8),int(cont.get_height()/8)))
    surf.blit(cont,(int(WINDOWWIDTH-cont.get_width()),int(WINDOWHEIGHT-cont.get_height())))
    contRect = cont.get_rect(topleft = (int(WINDOWWIDTH-cont.get_width()),int(WINDOWHEIGHT-cont.get_height())))
    return(DISPLAYSURF,contRect)
