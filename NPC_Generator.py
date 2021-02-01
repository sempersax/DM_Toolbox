import numpy as np
import os
import pygame as pg
import time
import NPC_Roster as roster
#import NPC_Navigator as npcNav
def race(arguments):
    surf = arguments['surf']
    pg.init()
    WINDOWWIDTH = surf.get_width()
    WINDOWHEIGHT = surf.get_height()

    raceFiles = os.listdir('images/races')
    start = time.time()
    races=[None]*len(raceFiles)
    prefix = ['images/races/']*len(raceFiles)
    for i in range(len(raceFiles)): #this loads all of the race images at once.
        raceFiles[i] = prefix[i]+raceFiles[i]
        races[i] = pg.image.load(raceFiles[i])
        races[i] = pg.transform.smoothscale(races[i], (int(races[i].get_width()/8*WINDOWWIDTH/1000),int(races[i].get_height()/8*WINDOWHEIGHT/629)))

    raceRects = []
    surf.fill((0,0,0))
    image = pg.image.load('images/navigation_screen.png')
    image = pg.transform.scale(image, (WINDOWWIDTH,WINDOWHEIGHT))
    surf.blit(image,(0,0))
    start2=time.time()
    for i in range(int(np.ceil(len(races)/4))):
        for j in range(4):
            if(j+i*4)>= len(races):
                break
            position = (int(surf.get_width()/5+races[i].get_width()*(i)),int(surf.get_height()/5+races[i].get_height()*(j)))
            surf.blit(races[j+i*4], position)
            raceRects.append(races[i].get_rect(topleft = position))
    rects = raceRects
    keys = ['gender']*len(raceRects)
    keys.append('characters')
    surfs = {'surf':surf,
             'rects':raceRects}
    arguments['surf'] = surf
    arguments['raceRects'] = raceRects
    #return(surfs,raceRects,keys)
    return(raceRects,keys)

def gender(arguments):
    pg.init()
    surf = arguments['surf']
    rects = arguments['raceRects']
    pos = arguments['pos']
    WINDOWWIDTH = surf.get_width()
    WINDOWHEIGHT = surf.get_height()
    genders = [None]*2
    genders[0] = pg.image.load('images/genders/DMTB_FEMALE_Button.png')
    genders[1] = pg.image.load('images/genders/DMTB_MALE_Button.png')
    for i in range(0,len(genders)):
        genders[i] = pg.transform.scale(genders[i], (int(genders[i].get_width()/8*WINDOWWIDTH/1000),int(genders[i].get_height()/8*WINDOWHEIGHT/629)))

    races = ['DRAGONBORN','DWARF','ELF','GNOME','GOBLIN','HALF-ELF','HALF-ORC','HALFLING','HUMAN','ORC']

    try:
        raceSel = arguments['raceSel']
    except KeyError:
        raceSel = 'None'
        for i in range(len(rects)):
            if rects[i].collidepoint(pos):
                raceSel = races[i]

    if raceSel != 'None':
        image = pg.image.load('images/navigation_screen.png')
        image = pg.transform.scale(image, (WINDOWWIDTH,WINDOWHEIGHT))
        surf.fill((0,0,0))
        surf.blit(image,(0,0))
    genRects = []

    if raceSel != 'None':
        surf.blit(genders[0], (int(genders[0].get_width()),int(WINDOWHEIGHT/2-genders[0].get_height()/2)))
        surf.blit(genders[1], (int(WINDOWWIDTH-2*genders[1].get_width()),int(WINDOWHEIGHT/2-genders[1].get_height()/2)))
        genRects.append(genders[0].get_rect(topleft =(int(genders[0].get_width()),int(WINDOWHEIGHT/2-genders[0].get_height()/2))))
        genRects.append(genders[1].get_rect(topleft =(int(WINDOWWIDTH-2*genders[1].get_width()),int(WINDOWHEIGHT/2-genders[1].get_height()/2))))

    rectsOld = rects
    surfs = {'surf':surf,
             'rectsOld': rectsOld,
             'posOld': pos,
             'pos':pos,
             'raceSel':raceSel,
             'rects': genRects,#[genRects,rects],
             'prevKey':'gender',
             'pos': pos,
             'name': []}
    rects = genRects
    keys = ['name']*len(genRects)
    keys.append('NPC')
    arguments['surf'] = surf
    arguments['rectsOld'] = rectsOld
    arguments['posOld'] = pos
    arguments['raceSel'] = raceSel
    arguments['genRects'] = genRects
    arguments['prevKey'] = 'gender'
    arguments['name'] = []
    #return(surfs,genRects,keys)
    return(genRects,keys)
        
def name(arguments):
    pg.init()
    surf = arguments['surf']
    rectsOld = arguments['rectsOld']
    posOld = arguments['posOld']
    raceSel = arguments['raceSel']
    rects = arguments['genRects']
    prevKey = arguments['prevKey']
    pos = arguments['pos']

    WINDOWWIDTH = surf.get_width()
    WINDOWHEIGHT = surf.get_height()

    genderSel = ''
    FONT = pg.font.Font('fonts/GimletSSK.ttf', int(48 *surf.get_height()/629))
    genders = ['FEMALE', 'MALE']

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

    if prevKey == 'name':
        first, last = arguments['name']

    raceText = FONT.render('    RACE: '+raceSel,True,[0,0,0],None)
    genText = FONT.render('GENDER: ' + genderSel, True,[0,0,0],None)
    nameText = FONT.render('    NAME: ' + first + ' ' + last, True,[0,0,0],None)
    DISPLAYSURF = surf
    scroll = pg.image.load('images/character_scroll.png')
    scroll = pg.transform.scale(scroll,(WINDOWWIDTH, WINDOWHEIGHT))
    image = pg.image.load('images/navigation_screen.png')
    image = pg.transform.smoothscale(image, (WINDOWWIDTH,WINDOWHEIGHT))

    surf.fill((0,0,0))
    surf.blit(image,(0,0))
    surf.blit(scroll,(0,0))
    surf.blit(raceText,(int(scroll.get_width()//2-raceText.get_width()//2),int(scroll.get_height()/8+2*raceText.get_height())))
    surf.blit(genText,(int(scroll.get_width()//2-genText.get_width()//2),int(scroll.get_height()/8+3*raceText.get_height())))
    surf.blit(nameText,(int(scroll.get_width()//2-nameText.get_width()//2),int(scroll.get_height()/8+3*raceText.get_height()+genText.get_height())))
    cont = pg.image.load('images/tools/DMTB_NPC_CIRCLE_button.png')
    cont = pg.transform.scale(cont,(int(cont.get_width()/2),int(cont.get_height()/2)))
    surf.blit(cont,(int(WINDOWWIDTH-cont.get_width()),int(WINDOWHEIGHT-cont.get_height())))
    contRect = cont.get_rect(topleft = (int(WINDOWWIDTH-cont.get_width()),int(WINDOWHEIGHT-cont.get_height())))

    surfs = {'surf':surf,
             'rectsOld':rectsOld,
             'posOld':posOld,
             'raceSel':raceSel,
             'rects':rects,
             'prevKey':'name',
             'pos':pos,
             'name':[first,last]}
    rects = [contRect]
    keys = ['characters','gender']
    arguments['surf'] = surf
    arguments['rectsOld'] = rectsOld
    arguments['posOld'] = posOld
    arguments['prevKey'] = 'name'
    arguments['name'] = (first,last)
    arguments['pos'] = posOld
                        
    #return(surfs, rects, keys)
    return(rects, keys)
