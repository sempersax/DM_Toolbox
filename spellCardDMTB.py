import pygame as pg
import random
import os
import sys
import numpy as np
import json
import pygame.surfarray as surfarray
from pygame.locals import *


##WINDOWWIDTH = 1000
##WINDOWHEIGHT = 650
##FPS = 30

def spellCard(SURFS):
    pg.init()
    surf = SURFS[0]
    backRects = SURFS[1]
    prevKey = SURFS[2]
    shift = SURFS[3]
    spellNames = SURFS[4]
    spellSelected = SURFS[5]
    pos = SURFS[-1]
    if prevKey == 'spellDesc':
        gridShift = SURFS[6]
        oldShift = SURFS[3]
    if prevKey == 'spellStats':
        gridShift = SURFS[4][1]
        oldShift = SURFS[4][0]
    pos = SURFS[-1]

    for i in range(0,len(backRects)):
        if backRects[i].collidepoint(pos):
            spellJson = spellNames[i+gridShift]
    WINDOWWIDTH = surf.get_width()
    WINDOWHEIGHT = surf.get_height()
    DISPLAYSURF = surf

    TITLE = pg.font.Font('fonts/GimletSSK.ttf',24)
    SUBTITLE = pg.font.Font('fonts/GimletSSK.ttf',20)
    FONT1 = pg.font.Font('fonts/GimletSSK.ttf', 18)
    FONT2 = pg.font.Font('fonts/GimletSSK.ttf', 14)    
    cwd = os.getcwd()
    edge=120

    with open(cwd+'/spellScrape/spellJsons/'+spellJson.replace(' ','_')+'.json') as jsonFile:
        data = json.load(jsonFile)
        print(data)
##        data['spellSchool'] = data['spellSchool'].replace('Armor Class','')
##        data['spellHP'] = data['spellHP'].replace('Hit Points', '')
##        data['spellSpeed'] = data['spellSpeed'].replace('Speed', '')
##        data['spellSavings'] = data['spellSavings'].replace('Saving Throws','')
##        data['spellSkills'] = data['spellSkills'].replace('Skills','')
##        data['spellResistances'] = data['spellResistances'].replace('Damage Resistances', '')
##        data['spellVulnerabilities']=data['spellVulnerabilities'].replace('Damage Vulnerabilities','')
##        data['spellImmunities'] = data['spellImmunities'].replace('Damage Immunities','')
##        data['spellCImmunities'] = data['spellCImmunities'].replace('Condition Immunities','')
##        data['spellLanguages'] = data['spellLanguages'].replace('Languages','')
##        data['spellChallenge'] = data['spellChallenge'].replace('Challenge','')
##        data['spellSenses'] = data['spellSenses'].replace('Senses','')


    
    FPSCLOCK = pg.time.Clock()

    screen = pg.image.load('images/character_scroll.png')
    screen = pg.transform.scale(screen,(WINDOWWIDTH, WINDOWHEIGHT))#(int(screen.get_width()*1.6),int(screen.get_height()*1.15)))
    image = pg.image.load('images/DMTB_SPELL_screen.jpg')
    image = pg.transform.smoothscale(image,(WINDOWWIDTH, WINDOWHEIGHT))

    DISPLAYSURF.fill((0,0,0))
    DISPLAYSURF.blit(image,(0,0))
    DISPLAYSURF.blit(screen, (0,0))
    spellName = TITLE.render(data['spellName'],True,[146,4,4],None)
    spellSchool = SUBTITLE.render(data['spellSchool'],True,[0,0,0], None)

    spellLevelLabel = FONT1.render('Spell Level: ', True, [146,4,4], None)
    spellLevel = FONT2.render(str(data['spellLevel']), True, [0,0,0], None)

    spellTimeLabel = FONT1.render('Casting Time: ', True, [146,4,4], None)
    spellTime = FONT2.render(data['castingTime'], True, [0,0,0], None)

    spellDurationLabel = FONT1.render('Duration: ', True, [146,4,4], None)
    spellDuration = FONT2.render(data['spellDuration'], True, [0,0,0], None)
    
    spellEffectLabel = FONT1.render('Description: ', True, [146,4,4], None)

    if data['spellEffect'] != '':
        spellEffects = []
        
        if FONT2.render(data['spellEffect'], True, [0,0,0], None).get_width() > screen.get_width()-220:
            data['spellEffect'] = data['spellEffect'].split(' ')
            tempSpecial = data['spellEffect']
            tempSpecial1 = ''
            print(tempSpecial,'hello')
            
            for j in range(0,len(tempSpecial)):
                if FONT2.render(tempSpecial1, True, [0,0,0], None).get_width() < screen.get_width()-220:
                    tempSpecial1+=str(tempSpecial[j])+' '
                    print(tempSpecial1)
                else:
                    spellEffects.append(FONT2.render(tempSpecial1, True, [0,0,0], None))
                    tempSpecial1 = ' '

        
    #print(data['spellEffect'])
    DISPLAYSURF.blit(spellName, (int(screen.get_width()/2-spellName.get_width()/2), int(screen.get_height()/10-40) ))
    DISPLAYSURF.blit(spellName, (int(screen.get_width()/2-spellName.get_width()/2), int(screen.get_height()*9/10-25) ))
    DISPLAYSURF.blit(spellSchool, (int(screen.get_width()/2-spellSchool.get_width()/2), int(screen.get_height()/10-40+spellName.get_height()) ))
    DISPLAYSURF.blit(spellSchool, (int(screen.get_width()/2-spellSchool.get_width()/2), int(screen.get_height()*9/10-25+spellName.get_height()) ))
    # Putting Level on Card
    DISPLAYSURF.blit(spellLevelLabel, (edge,int(screen.get_height()/10*2)))
    DISPLAYSURF.blit(spellLevel, (edge+spellLevelLabel.get_width(), int(screen.get_height()/10*2+3)))
    # Putting HP on Card
    DISPLAYSURF.blit(spellTimeLabel, (edge, int(screen.get_height()/10*2 + spellLevelLabel.get_height()+3)))
    DISPLAYSURF.blit(spellTime, (edge+spellTimeLabel.get_width(), int(screen.get_height()/10*2 + spellLevelLabel.get_height()+3)))
    # Putting Speed on Card
    DISPLAYSURF.blit(spellDurationLabel, (edge, int(screen.get_height()/10*2 + 2*spellLevelLabel.get_height()+3)))
    DISPLAYSURF.blit(spellDuration, (edge+spellLevelLabel.get_width(), int(screen.get_height()/10*2 + 2*spellLevelLabel.get_height()+3)))

    shift = 4

    try:
        DISPLAYSURF.blit(spellEffectLabel, (edge, int(screen.get_height()/10*2+spellLevelLabel.get_height()*shift)))
        shift +=1
        for i in range(0,len(spellEffects)):
                DISPLAYSURF.blit(spellEffects[i], (edge, int(screen.get_height()/10*2 + spellLevelLabel.get_height()*shift+3)))
                shift+=1
    except:
        pass


    cont = pg.image.load('images/music_Button.png')
    cont = pg.transform.scale(cont,(int(cont.get_width()/8),int(cont.get_height()/8)))
    surf.blit(cont,(int(WINDOWWIDTH-cont.get_width()),int(WINDOWHEIGHT-cont.get_height())))
    contRect = cont.get_rect(topleft = (int(WINDOWWIDTH-cont.get_width()),int(WINDOWHEIGHT-cont.get_height())))


    pg.display.update()
    surfs = [DISPLAYSURF,spellNames,spellSelected,backRects,[0,gridShift],'spellStats']
    rects = [contRect]
    keys = ['letter','spells']
    return(surfs,rects,keys)
