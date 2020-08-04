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

def monsterStatCard(monsterJson,surf):
    pg.init()
    WINDOWWIDTH = surf.get_width()
    WINDOWHEIGHT = surf.get_height()
    DISPLAYSURF = surf

    TITLE = pg.font.Font('fonts/GimletSSK.ttf',24)
    SUBTITLE = pg.font.Font('fonts/GimletSSK.ttf',20)
    FONT1 = pg.font.Font('fonts/GimletSSK.ttf', 18)
    FONT2 = pg.font.Font('fonts/GimletSSK.ttf', 14)    
    cwd = os.getcwd()
    edge=120

    with open(cwd+'/MonsterScrape/MonsterJsons/'+monsterJson.replace(' ','_')+'.json') as jsonFile:
        data = json.load(jsonFile)
        data['monsterArmor'] = data['monsterArmor'].replace('Armor Class','')
        data['monsterHP'] = data['monsterHP'].replace('Hit Points', '')
        data['monsterSpeed'] = data['monsterSpeed'].replace('Speed', '')
        data['monsterSavings'] = data['monsterSavings'].replace('Saving Throws','')
        data['monsterSkills'] = data['monsterSkills'].replace('Skills','')
        data['monsterResistances'] = data['monsterResistances'].replace('Damage Resistances', '')
        data['monsterVulnerabilities']=data['monsterVulnerabilities'].replace('Damage Vulnerabilities','')
        data['monsterImmunities'] = data['monsterImmunities'].replace('Damage Immunities','')
        data['monsterCImmunities'] = data['monsterCImmunities'].replace('Condition Immunities','')
        data['monsterLanguages'] = data['monsterLanguages'].replace('Languages','')
        data['monsterChallenge'] = data['monsterChallenge'].replace('Challenge','')
        data['monsterSenses'] = data['monsterSenses'].replace('Senses','')
    #print(data)
##    global WINDOWHEIGHT, WINDOWWIDTH,FPSCLOCK
    FPSCLOCK = pg.time.Clock()
##    DISPLAYSURF = pg.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),HWSURFACE | DOUBLEBUF|RESIZABLE)
##    DISPLAYSURF = pg.display.set_mode((0,0), pg.FULLSCREEN)
##    pg.display.set_caption('Card Tester')
##    pg.display.update()
    screen = pg.image.load('images/character_scroll.png')
    screen = pg.transform.scale(screen,(WINDOWWIDTH, WINDOWHEIGHT))#(int(screen.get_width()*1.6),int(screen.get_height()*1.15)))
    DISPLAYSURF.blit(screen, (0,0))
    monsterName = TITLE.render(data['monsterName'],True,[146,4,4],None)
    monsterType = SUBTITLE.render(data['monsterType'],True,[0,0,0], None)
    monsterArmorLabel = FONT1.render('Armor Class: ', True, [146,4,4], None)
    monsterArmor = FONT2.render(data['monsterArmor'], True, [0,0,0], None)
    monsterHPLabel = FONT1.render('Hit Points: ', True, [146,4,4], None)
    monsterHP = FONT2.render(data['monsterHP'],True,[0,0,0],None)
    monsterSpeedLabel = FONT1.render('Speed: ', True, [146,4,4], None)
    monsterSpeed = FONT2.render(data['monsterSpeed'], True, [0,0,0], None)

    monsterSTRLabel = FONT1.render('STR: ', True, [146,4,4], None)
    monsterSTR = FONT2.render(data['monsterSTR'], True, [0,0,0], None)

    monsterDEXLabel = FONT1.render('DEX: ', True, [146,4,4], None)
    monsterDEX = FONT2.render(data['monsterDEX'], True, [0,0,0], None)

    monsterCONLabel = FONT1.render('CON: ', True, [146,4,4], None)
    monsterCON = FONT2.render(data['monsterCON'], True, [0,0,0], None)

    monsterINTLabel = FONT1.render('INT: ', True, [146,4,4], None)
    monsterINT = FONT2.render(data['monsterINT'], True, [0,0,0], None)

    monsterWISLabel = FONT1.render('WIS: ', True, [146,4,4], None)
    monsterWIS = FONT2.render(data['monsterWIS'], True, [0,0,0], None)

    monsterCHALabel = FONT1.render('CHA: ', True, [146,4,4], None)
    monsterCHA = FONT2.render(data['monsterCHA'], True, [0,0,0], None)

    if data['monsterSavings'] != '':
        monsterSavingsLabel = FONT1.render('Saving Throws: ', True, [146,4,4], None)
        monsterSavings = FONT2.render(data['monsterSavings'], True, [0,0,0], None)

    if data['monsterSkills'] != '':
        monsterSkillsLabel = FONT1.render('Skills: ', True, [146,4,4], None)
        monsterSkills = FONT2.render(data['monsterSkills'], True, [0,0,0], None)

    if data['monsterSkills'] != '':
        monsterSkillsLabel = FONT1.render('Skills: ', True, [146,4,4], None)
        monsterSkills = FONT2.render(data['monsterSkills'], True, [0,0,0], None)

    if data['monsterVulnerabilities'] != '':
        monsterVulnerabilitiesLabel = FONT1.render('Damage Vulnerabilities: ', True, [146,4,4], None)
        monsterVulnerabilities = FONT2.render(data['monsterVulnerabilities'], True, [0,0,0], None)

    if data['monsterResistances'] != '':
        monsterResistancesLabel = FONT1.render('Damage Resistances: ', True, [146,4,4], None)
        monsterResistances = FONT2.render(data['monsterResistances'], True, [0,0,0], None)

    if data['monsterImmunities'] != '':
        monsterImmunitiesLabel = FONT1.render('Damage Immunities: ', True, [146,4,4], None)
        monsterImmunities = FONT2.render(data['monsterImmunities'], True, [0,0,0], None)

    if data['monsterCImmunities'] != '':
        monsterCImmunitiesLabel = FONT1.render('Condition Immunities: ', True, [146,4,4], None)
        monsterCImmunities = FONT2.render(data['monsterCImmunities'], True, [0,0,0], None)

    if data['monsterSenses'] != '':
        monsterSensesLabel = FONT1.render('Sense: ',True, [146,4,4], None)
        monsterSenses = FONT2.render(data['monsterSenses'],True,[0,0,0],None)

    if data['monsterLanguages'] != '':
        monsterLanguagesLabel = FONT1.render('Languages: ',True, [146,4,4], None)
        monsterLanguages = FONT2.render(data['monsterLanguages'],True,[0,0,0],None)

    monsterChallengeLabel = FONT1.render('Challenge: ', True, [146,4,4], None)
    monsterChallenge = FONT2.render(data['monsterChallenge'], True, [0,0,0], None)

    if data['monsterSpecials'] != '':
        monsterSpecialsLabel = FONT1.render('Special Abilities:', True, [146,4,4], None)
        monsterSpecials = []
        i=0
        while i < len(data['monsterSpecials']):
            if '\n\n' in data['monsterSpecials'][i]:
                data['monsterSpecials'][i] = data['monsterSpecials'][i].split('\n\n')
                tempData = []
                for k in range(0, len(data['monsterSpecials'][i])):
                    tempData.append(data['monsterSpecials'][i][k])
                del data['monsterSpecials'][i]
                for k in range(0, len(tempData)):
                    data['monsterSpecials'].append(tempData[k])

            if FONT2.render(data['monsterSpecials'][i], True, [0,0,0], None).get_width() > screen.get_width()//2-120:
                tempSpecial = data['monsterSpecials'][i].split(' ')
                tempSpecial1 = ''
                for j in range(0,len(tempSpecial)):
                    if FONT2.render(tempSpecial1, True, [0,0,0], None).get_width() < screen.get_width()//2-120:
                        tempSpecial1+=str(tempSpecial[j])+' '
                        data['monsterSpecials'][i] = tempSpecial1
                    else:
                        tempSpecial1 = ' '.join(tempSpecial[j:])
                        data['monsterSpecials'].insert(i+1,tempSpecial1)
                        break

            monsterSpecials.append(FONT2.render(data['monsterSpecials'][i], True, [0,0,0], None))
            i=i+1

    if data['monsterActions'] != '':
        monsterActionsLabel = FONT1.render('Actions:', True, [146,4,4], None)
        monsterActions = []
        i=1
        while i < len(data['monsterActions']):
            if '\n\n' in data['monsterActions'][i]:
                data['monsterActions'][i] = data['monsterActions'][i].split('\n\n')
                tempData = []
                for k in range(0, len(data['monsterActions'][i])):
                    tempData.append(data['monsterActions'][i][k])
                del data['monsterActions'][i]
                for k in range(0, len(tempData)):
                    data['monsterActions'].insert(i+k,tempData[k])

            if FONT2.render(data['monsterActions'][i], True, [0,0,0], None).get_width() > edge/2+ screen.get_width()//2 - 260:
                tempSpecial = data['monsterActions'][i].split(' ')
                tempSpecial1 = ''
                for j in range(0,len(tempSpecial)):
                    if FONT2.render(tempSpecial1, True, [0,0,0], None).get_width() < edge/2+screen.get_width()//2-260:
                        tempSpecial1+=str(tempSpecial[j])+' '
                        data['monsterActions'][i] = tempSpecial1
                    else:
                        tempSpecial1 = ' '.join(tempSpecial[j:])
                        data['monsterActions'].insert(i+1,tempSpecial1)
                        break

            monsterActions.append(FONT2.render(data['monsterActions'][i], True, [0,0,0], None))
            i=i+1

    DISPLAYSURF.blit(monsterName, (int(screen.get_width()/2-monsterName.get_width()/2), int(screen.get_height()/10-40) ))
    DISPLAYSURF.blit(monsterName, (int(screen.get_width()/2-monsterName.get_width()/2), int(screen.get_height()*9/10-25) ))
    DISPLAYSURF.blit(monsterType, (int(screen.get_width()/2-monsterType.get_width()/2), int(screen.get_height()/10-40+monsterName.get_height()) ))
    DISPLAYSURF.blit(monsterType, (int(screen.get_width()/2-monsterType.get_width()/2), int(screen.get_height()*9/10-25+monsterName.get_height()) ))
    # Putting AC on Card
    DISPLAYSURF.blit(monsterArmorLabel, (edge,int(screen.get_height()/10*2)))
    DISPLAYSURF.blit(monsterArmor, (edge+monsterArmorLabel.get_width(), int(screen.get_height()/10*2+3)))
    # Putting HP on Card
    DISPLAYSURF.blit(monsterHPLabel, (edge, int(screen.get_height()/10*2 + monsterArmorLabel.get_height()+3)))
    DISPLAYSURF.blit(monsterHP, (edge+monsterArmorLabel.get_width(), int(screen.get_height()/10*2 + monsterArmorLabel.get_height()+3)))
    # Putting Speed on Card
    DISPLAYSURF.blit(monsterSpeedLabel, (edge, int(screen.get_height()/10*2 + 2*monsterArmorLabel.get_height()+3)))
    DISPLAYSURF.blit(monsterSpeed, (edge+monsterArmorLabel.get_width(), int(screen.get_height()/10*2 + 2*monsterArmorLabel.get_height()+3)))


    # Putting Abilities on Card
    DISPLAYSURF.blit(monsterSTRLabel, (int(screen.get_width() - monsterSTRLabel.get_width()*8.2), int(screen.get_height()/10*2)))
    DISPLAYSURF.blit(monsterSTR, (int(screen.get_width() - monsterSTRLabel.get_width()*7.2), int(screen.get_height()/10*2+3)))
    
    DISPLAYSURF.blit(monsterDEXLabel, (int(screen.get_width() - monsterSTRLabel.get_width()*8.2-(monsterDEXLabel.get_width()-monsterSTRLabel.get_width())), int(screen.get_height()/10*2+monsterSTRLabel.get_height())))
    DISPLAYSURF.blit(monsterDEX, (int(screen.get_width() - monsterSTRLabel.get_width()*7.2), int(screen.get_height()/10*2+(monsterSTRLabel.get_height()+3))))
    
    DISPLAYSURF.blit(monsterCONLabel, (int(screen.get_width() - monsterSTRLabel.get_width()*8.2-(monsterCONLabel.get_width()-monsterSTRLabel.get_width())), int(screen.get_height()/10*2+monsterSTRLabel.get_height()*2)))
    DISPLAYSURF.blit(monsterCON, (int(screen.get_width() - monsterSTRLabel.get_width()*7.2), int(screen.get_height()/10*2+2*monsterSTRLabel.get_height()+3)))

    # Second Column
    DISPLAYSURF.blit(monsterINTLabel, (int(screen.get_width() - monsterINTLabel.get_width()*4.2), int(screen.get_height()/10*2)))
    DISPLAYSURF.blit(monsterINT, (int(screen.get_width() - monsterINTLabel.get_width()*3.2), int(screen.get_height()/10*2+3)))
    
    DISPLAYSURF.blit(monsterWISLabel, (int(screen.get_width() - monsterINTLabel.get_width()*4.2-(monsterWISLabel.get_width()-monsterINTLabel.get_width())), int(screen.get_height()/10*2+monsterINTLabel.get_height())))
    DISPLAYSURF.blit(monsterWIS, (int(screen.get_width() - monsterINTLabel.get_width()*3.2), int(screen.get_height()/10*2+3+monsterINTLabel.get_height())))
    
    DISPLAYSURF.blit(monsterCHALabel, (int(screen.get_width() - monsterINTLabel.get_width()*4.2-(monsterCHALabel.get_width()-monsterINTLabel.get_width())), int(screen.get_height()/10*2+2*monsterINTLabel.get_height())))
    DISPLAYSURF.blit(monsterCHA, (int(screen.get_width() - monsterINTLabel.get_width()*3.2), int(screen.get_height()/10*2+3+2*monsterINTLabel.get_height())))

    shift = 4
    tempShift = shift-1

    try:
        DISPLAYSURF.blit(monsterSavingsLabel, (edge, int(screen.get_height()/10*2+monsterArmorLabel.get_height()*shift)))
        DISPLAYSURF.blit(monsterSavings, (edge+monsterSavingsLabel.get_width(), int(screen.get_height()/10*2 + monsterArmorLabel.get_height()*shift+3)))
        shift +=1
    except:
        pass

    try:
        DISPLAYSURF.blit(monsterSkillsLabel, (edge, int(screen.get_height()/10*2+monsterArmorLabel.get_height()*shift)))
        DISPLAYSURF.blit(monsterSkills, (edge+monsterSkillsLabel.get_width(), int(screen.get_height()/10*2 + monsterArmorLabel.get_height()*shift+3)))
        shift +=1
    except:
        pass        

    try:
        DISPLAYSURF.blit(monsterVulnerabilitiesLabel, (edge, int(screen.get_height()/10*2+monsterArmorLabel.get_height()*shift)))
        wide = int(monsterVulnerabilitiesLabel.get_width())
        if edge+monsterVulnerabilities.get_width()+wide > int((surf.get_width()//2+screen.get_width()//2)/2):
            shift +=1
            wide = 0
        DISPLAYSURF.blit(monsterVulnerabilities, (edge+wide, int(screen.get_height()/10*2 + monsterArmorLabel.get_height()*shift+3)))
        shift +=1
    except:
        pass

    try:
        DISPLAYSURF.blit(monsterResistancesLabel, (edge, int(screen.get_height()/10*2+monsterArmorLabel.get_height()*shift)))
        wide = int(monsterResistancesLabel.get_width())
        if edge+monsterResistances.get_width()+wide > int((surf.get_width()//2+screen.get_width()//2)/2):
            shift +=1
            wide = 0
            if edge+monsterResistances.get_width()+wide > int((surf.get_width()//2+screen.get_width()//2)/2):
                monsterResistances = []
                
                tempResist = data['monsterResistances'].split(' ')
                tempResist1 = ''
                tempData = []
                for j in range(0,len(tempResist)):
                    if FONT2.render(tempResist1, True, [0,0,0], None).get_width()+edge < int((surf.get_width()//2+screen.get_width()//2)/2):
                        print('hello')
                        tempResist1+=str(tempResist[j])+' '
                    elif FONT2.render(tempResist1, True, [0,0,0], None).get_width()+edge > int((surf.get_width()//2+screen.get_width()//2)/2):
                        tempData.append(tempResist1)
                        tempResist1 = ' '.join(tempResist[j:])
                        tempData.append(tempResist1)
                    
                for j in range(0,len(tempData)):
                    monsterResistances.append(FONT2.render(tempData[j], True, [0,0,0], None))
        print(monsterResistances,'\n','hello','\n')
        print(type(monsterResistances))
        if type(monsterResistances) == list:
            for i in range(0,len(monsterResistances)):
                DISPLAYSURF.blit(monsterResistances[i], (edge+wide, int(screen.get_height()/10*2 + monsterArmorLabel.get_height()*shift+3)))
                shift +=1
        elif type(monsterResistances) != list:
            DISPLAYSURF.blit(monsterResistances, (edge+wide, int(screen.get_height()/10*2 + monsterArmorLabel.get_height()*shift+3)))
            shift +=1
    except:
        pass
    
    try:
        DISPLAYSURF.blit(monsterImmunitiesLabel, (edge, int(screen.get_height()/10*2+monsterArmorLabel.get_height()*shift)))
        wide = int(monsterImmunitiesLabel.get_width())
        if edge+monsterImmunities.get_width()+wide > int((surf.get_width()//2+screen.get_width()//2)/2):
            shift +=1
            wide = 0
        DISPLAYSURF.blit(monsterImmunities, (edge+wide, int(screen.get_height()/10*2 + monsterArmorLabel.get_height()*shift+3)))
        shift +=1
    except:
        pass

    try:
        DISPLAYSURF.blit(monsterCImmunitiesLabel, (edge, int(screen.get_height()/10*2+monsterArmorLabel.get_height()*shift)))
        wide = int(monsterCImmunitiesLabel.get_width())
        if edge+monsterCImmunities.get_width()+wide > int((surf.get_width()//2+screen.get_width()//2)/2):
            shift +=1
            wide = 0
        DISPLAYSURF.blit(monsterCImmunities, (edge+wide, int(screen.get_height()/10*2 + monsterArmorLabel.get_height()*shift+3)))
        shift +=1
    except:
        pass
    
    try:
        DISPLAYSURF.blit(monsterSensesLabel, (edge, int(screen.get_height()/10*2+monsterArmorLabel.get_height()*shift)))
        DISPLAYSURF.blit(monsterSenses, (edge+monsterSensesLabel.get_width(), int(screen.get_height()/10*2 + monsterArmorLabel.get_height()*shift+3)))
        shift +=1
    except:
        pass

    try:
        DISPLAYSURF.blit(monsterLanguagesLabel, (edge, int(screen.get_height()/10*2+monsterArmorLabel.get_height()*shift)))
        DISPLAYSURF.blit(monsterLanguages, (edge+monsterLanguagesLabel.get_width(), int(screen.get_height()/10*2 + monsterArmorLabel.get_height()*shift+3)))
        shift +=1
    except:
        pass

    DISPLAYSURF.blit(monsterChallengeLabel, (edge, int(screen.get_height()/10*2+monsterArmorLabel.get_height()*shift)))
    DISPLAYSURF.blit(monsterChallenge, (edge+monsterChallengeLabel.get_width(), int(screen.get_height()/10*2 + monsterArmorLabel.get_height()*shift+3)))
    shift +=2

    try:
        DISPLAYSURF.blit(monsterSpecialsLabel, (edge, int(screen.get_height()/10*2+monsterArmorLabel.get_height()*shift)))
        shift +=1
        for i in range(0,len(monsterSpecials)):
                DISPLAYSURF.blit(monsterSpecials[i], (edge, int(screen.get_height()/10*2 + monsterArmorLabel.get_height()*shift+3)))
                shift +=1
    except:
        pass
    
    shift = tempShift
    try:
        DISPLAYSURF.blit(monsterActionsLabel, (edge/2+screen.get_width()//2, int(screen.get_height()/10*2+monsterArmorLabel.get_height()*shift)))
        shift +=1
        for i in range(0,len(monsterActions)):
                DISPLAYSURF.blit(monsterActions[i], (edge/2+screen.get_width()//2, int(screen.get_height()/10*2 + monsterArmorLabel.get_height()*shift+3)))
                shift +=1
    except:
        pass
    
##    while True:
##        for event in pg.event.get():
##            if event.type == KEYDOWN:
##                if event.key == K_ESCAPE:
##                    pg.quit()
##                    sys.exit()
##                    break

        pg.display.update()
