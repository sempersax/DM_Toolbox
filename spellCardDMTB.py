import pygame as pg
import random
import os
import sys
import numpy as np
import json
import pygame.surfarray as surfarray
from pygame.locals import *


def spellCard(arguments):
    pg.init()
    surf = arguments['surf']
    backRects = arguments['spellRects']
    prevKey = arguments['prevKey']
    shift = arguments['shift']
    pos = arguments['pos']
    spellNames = arguments['spellNames']
    gridShift = arguments['gridShift']
    oldShift = arguments['shift']

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
            j = 0
            while j < len(tempSpecial):
                if FONT2.render(tempSpecial1, True, [0,0,0], None).get_width() < screen.get_width()-220:
                    tempSpecial1+=str(tempSpecial[j])+' '
                    j+=1
                else:
                    spellEffects.append(FONT2.render(tempSpecial1, True, [0,0,0], None))
                    tempSpecial1 = ' '
                    j -= 1
            spellEffects.append(FONT2.render(tempSpecial1, True, [0,0,0], None))
        else:
            spellEffects.append(FONT2.render(data['spellEffect'], True, [0,0,0], None))

    spellRangeLabel = FONT1.render('Range: ', True, [146,4,4], None)
    spellRange = FONT2.render(data['spellRange'], True, [0,0,0], None)

    components = ''
    materials = ''
    if data['verbalBool'] == 'True':
        components += 'V'

    if data['somaticBool'] == 'True':
        components += 'S'

    if data['materialBool'] == 'True':
        components += 'M'
        materials = data['materials']

    spellComponentsLabel = FONT1.render('Components: ', True, [146,4,4], None)
    spellComponents = FONT2.render(components, True, [0,0,0], None)

    spellMaterialsLabel = FONT1.render('Materials: ', True, [146,4,4], None)
    spellMaterials = FONT2.render(materials, True, [0,0,0], None)

    
    
    DISPLAYSURF.blit(spellName, (int(screen.get_width()/2-spellName.get_width()/2), int(screen.get_height()/10-40) ))
    DISPLAYSURF.blit(spellName, (int(screen.get_width()/2-spellName.get_width()/2), int(screen.get_height()*9/10-25) ))
    DISPLAYSURF.blit(spellSchool, (int(screen.get_width()/2-spellSchool.get_width()/2), int(screen.get_height()/10-40+spellName.get_height()) ))
    DISPLAYSURF.blit(spellSchool, (int(screen.get_width()/2-spellSchool.get_width()/2), int(screen.get_height()*9/10-25+spellName.get_height()) ))
    # Putting Level on Card
    DISPLAYSURF.blit(spellLevelLabel, (edge,int(screen.get_height()/10*2)))
    DISPLAYSURF.blit(spellLevel, (edge+spellLevelLabel.get_width(), int(screen.get_height()/10*2+3)))
    # Putting Casting Time on Card
    DISPLAYSURF.blit(spellTimeLabel, (edge, int(screen.get_height()/10*2 + spellLevelLabel.get_height()+3)))
    DISPLAYSURF.blit(spellTime, (edge+spellTimeLabel.get_width(), int(screen.get_height()/10*2 + spellLevelLabel.get_height()+3)))
    # Putting Duration on Card
    DISPLAYSURF.blit(spellDurationLabel, (edge, int(screen.get_height()/10*2 + 2*spellLevelLabel.get_height()+3)))
    DISPLAYSURF.blit(spellDuration, (edge+spellLevelLabel.get_width(), int(screen.get_height()/10*2 + 2*spellLevelLabel.get_height()+3)))
    #Putting Range on Card
    DISPLAYSURF.blit(spellRangeLabel, (int(screen.get_width() - spellRangeLabel.get_width()*8.2), int(screen.get_height()/10*2)))
    DISPLAYSURF.blit(spellRange, (int(screen.get_width() - spellRangeLabel.get_width()*7.2), int(screen.get_height()/10*2)))
    #Putting components on Card
    DISPLAYSURF.blit(spellComponentsLabel, (int(screen.get_width() - spellRangeLabel.get_width()*8.2), int(screen.get_height()/10*2+spellRangeLabel.get_height())))
    DISPLAYSURF.blit(spellComponents, (int(screen.get_width() - spellRangeLabel.get_width()*8.2+spellComponentsLabel.get_width()), int(screen.get_height()/10*2+spellRangeLabel.get_height())))

    if materials != '':
        #Putting materials on Card
        DISPLAYSURF.blit(spellMaterialsLabel, (edge, int(screen.get_height()/10*2+4*spellLevelLabel.get_height())))
        DISPLAYSURF.blit(spellMaterials, (edge+spellMaterialsLabel.get_width(), int(screen.get_height()/10*2+4*spellLevelLabel.get_height())))    
        shift = 6
    else:
        shift = 4
    try:
        DISPLAYSURF.blit(spellEffectLabel, (edge, int(screen.get_height()/10*2+spellLevelLabel.get_height()*shift)))
        shift +=1
        for i in range(0,len(spellEffects)):
                DISPLAYSURF.blit(spellEffects[i], (edge, int(screen.get_height()/10*2 + spellLevelLabel.get_height()*shift+3)))
                shift+=1
    except:
        pass


    cont = pg.image.load('images/tools/DMTB_SPELLS_CIRCLE_button.png')
    cont = pg.transform.scale(cont,(int(cont.get_width()/2),int(cont.get_height()/2)))
    surf.blit(cont,(int(WINDOWWIDTH-cont.get_width()),int(WINDOWHEIGHT-cont.get_height())))
    contRect = cont.get_rect(topleft = (int(WINDOWWIDTH-cont.get_width()),int(WINDOWHEIGHT-cont.get_height())))


    pg.display.update()
    rects = [contRect]
    keys = ['spells',arguments['prevKey']]
    arguments['surf'] = DISPLAYSURF
    arguments['prevKey'] = 'spellDesc'
    return(rects,keys)
