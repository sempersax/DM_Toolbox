# This is for the main screen that the DM navigates to for referencing spells in.  Creates
# the screen and the relevant buttons 
# Each of which will have their own navigation screen later on.

import pygame as pg
import random
import os
import numpy as np
import pygame.surfarray as surfarray
from pygame.locals import *


def createSpell(arguments):
    pg.init()
    surf = arguments['surf']
    WINDOWWIDTH = surf.get_width()
    WINDOWHEIGHT = surf.get_height()

    # Spells Button
    classesurf = pg.image.load('images/classes/DMTB_CLASS_Button.png')
    classesurf = pg.transform.scale(classesurf, (int(classesurf.get_width() / 8), int(classesurf.get_height() / 8)))
    classRect = classesurf.get_rect(
        topleft=(int(classesurf.get_width() * 1 / 5), int(WINDOWHEIGHT / 4) - int(classesurf.get_height() / 2)))

    levelSurf = pg.image.load('images/Levels_Button.png')
    levelSurf = pg.transform.scale(levelSurf, (int(levelSurf.get_width() / 8), int(levelSurf.get_height() / 8)))
    levelRect = levelSurf.get_rect(topleft=(
    int(WINDOWWIDTH - levelSurf.get_width() * 6 / 5), int(WINDOWHEIGHT / 4) - int(levelSurf.get_height() / 2)))

    spellSurf = pg.image.load('images/DMTB_SPELL_screen.jpg')
    spellSurf = pg.transform.scale(spellSurf, (WINDOWWIDTH, WINDOWHEIGHT))

    surf.fill((0, 0, 0))
    surf.blit(spellSurf, (0, 0))
    surf.blit(levelSurf, (
    (int(WINDOWWIDTH - levelSurf.get_width() * 6 / 5), int(WINDOWHEIGHT / 4) - int(levelSurf.get_height() / 2))))
    surf.blit(classesurf,
              (int(classesurf.get_width() * 1 / 5), int(WINDOWHEIGHT / 4) - int(classesurf.get_height() / 2)))

    arguments['surf'] = surf
    rects = [classRect, levelRect]
    keys = ['class', 'levels', 'quest']
    return (rects, keys)


def createClasses(arguments):
    pg.init()
    surf = arguments['surf']
    WINDOWWIDTH = surf.get_width()
    WINDOWHEIGHT = surf.get_height()
    FONT = pg.font.Font('fonts/GimletSSK.ttf', 24)

    spellSurf = pg.image.load('images/DMTB_SPELL_screen.jpg')
    spellSurf = pg.transform.scale(spellSurf, (WINDOWWIDTH, WINDOWHEIGHT))

    surf.fill((0, 0, 0))
    surf.blit(spellSurf, (0, 0))

    classFiles = os.listdir('images/classes')

    template = pg.image.load('images/blank_button.png')
    template = pg.transform.smoothscale(template, (
    int(template.get_width() / 8 * WINDOWWIDTH / 1000), int(template.get_height() / 8 * WINDOWHEIGHT / 629)))
    classRects = []

    classNames = ['Bard', 'Cleric', 'Druid', 'Paladin', 'Ranger', 'Sorcerer', 'Warlock', 'Wizard']
    names = []
    for i in range(0, 2):
        for j in range(0, 4):
            names.append(FONT.render(classNames[j + i * 4], True, [237, 190, 141], None))
            position = (int(surf.get_width() // 3 + template.get_width() * (i)),
                        int(surf.get_height() / 5 + template.get_height() * (j)))
            surf.blit(template, position)
            classRects.append(template.get_rect(topleft=position))
            surf.blit(names[j + i * 4], (position[0] + template.get_width() / 2 - names[j + i * 4].get_width() / 2,
                                         position[1] + template.get_height() / 2 - names[j + i * 4].get_height() / 2))

    keys = ['classChose'] * len(classRects)
    keys.append('spells')
    arguments['surf'] = surf
    arguments['spellClass'] = classRects
    arguments['prevKey'] = 'class'
    return (classRects, keys)


def createLevels(arguments):
    pg.init()
    surf = arguments['surf']
    WINDOWWIDTH = surf.get_width()
    WINDOWHEIGHT = surf.get_height()
    spellSurf = pg.image.load('images/DMTB_SPELL_screen.jpg')
    spellSurf = pg.transform.scale(spellSurf, (WINDOWWIDTH, WINDOWHEIGHT))

    surf.fill((0, 0, 0))
    surf.blit(spellSurf, (0, 0))

    cwd = os.getcwd()
    mypath = "{}/images/filters/NUMBERS/".format(cwd)
    myNumbers = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
    myNumbers = myNumbers[0:10]
    rects = []
    surfs = []
    shift = 0
    yedge = surf.get_height() // 6
    xedge = surf.get_width() // 2 - 80
    j = 0
    for i in range(0, len(myNumbers)):
        surfs.append(pg.image.load(mypath + myNumbers[i]))
        if int(3 * yedge + surfs[i].get_height() * (1 / 8 + i - j)) > surf.get_height():
            shift += 1
            j = i
        rects.append(surfs[i].get_rect(topleft=(
        int(xedge + surfs[i].get_width() * (1 / 8 + shift)), int(yedge + surfs[i].get_height() * (1 / 8 + i - j)))))
        surf.blit(surfs[i], (
        int(xedge + surfs[i].get_width() * (1 / 8 + shift)), int(yedge + surfs[i].get_height() * (1 / 8 + i - j))))

    keys = ['levelNumbers'] * len(rects)
    keys.append('spells')
    arguments['surf'] = surf
    arguments['spellLevel'] = rects
    arguments['prevKey'] = 'levels'
    arguments['shift'] = 0
    return (rects, keys)


def spellLevelFilter(arguments):
    pg.init()
    surf = arguments['surf']
    levels = arguments['spellLevel']
    keyPrev = arguments['prevKey']
    pos = arguments['pos']
    shift = arguments['shift']
    WINDOWWIDTH = surf.get_width()
    WINDOWHEIGHT = surf.get_height()

    if keyPrev == 'levels':
        for i in range(0, len(levels)):
            if levels[i].collidepoint(pos):
                spellLevel = int(i)
        spellNames = []
        rosterPath = "{}/SpellScrape/spellRoster.txt".format(os.getcwd())
        with open(rosterPath, 'r') as roster:
            for line in roster:
                currentPlace = line[:-1].split(',')
                currentPlace[0] = currentPlace[0].replace('[', '').replace(']', '').replace("'", "").replace('"', '')
                currentPlace[1] = currentPlace[1].replace('[', '').replace(']', '').replace("'", "").replace(' ',
                                                                                                             '').replace(
                    'l', '1').replace('"', '')
                currentPlace[-1] = currentPlace[-1].replace('[', '').replace(']', '').replace("'", "").replace(' ',
                                                                                                               '').replace(
                    'l', '1').replace('"', '')
                currentPlace[-1] = int(currentPlace[-1])
                if currentPlace[-1] == spellLevel:
                    spellNames.append(currentPlace[0])

    if keyPrev == 'spellDesc':
        spellNames = arguments['spellNames']

    if keyPrev == 'spellStats':
        shift = arguments['shift']
        spellNames = arguments['spellNames']

    FONT = pg.font.Font('fonts/GimletSSK.ttf', 16)

    spellSurf = pg.image.load('images/DMTB_SPELL_screen.jpg')
    spellSurf = pg.transform.scale(spellSurf, (WINDOWWIDTH, WINDOWHEIGHT))
    surf.fill((0, 0, 0))
    surf.blit(spellSurf, (0, 0))

    template = pg.image.load('images/blank_button.png')
    template = pg.transform.scale(template, (int(template.get_width() / 8), int(template.get_height() / 8)))

    rightButton = pg.image.load('images/forward-circle_button.png')
    rightButton = pg.transform.scale(rightButton, (int(rightButton.get_width() / 2), int(rightButton.get_height() / 2)))

    leftButton = pg.image.load('images/back-circle_button.png')
    leftButton = pg.transform.scale(leftButton, (int(leftButton.get_width() / 2), int(leftButton.get_height() / 2)))

    rects = []
    surfs = []
    names = []
    columns = int((WINDOWWIDTH - 200) // 200)
    rows = int((WINDOWHEIGHT - 100) // 100)
    grid = columns * rows

    if grid * (1 + shift) < len(spellNames):
        rightRect = rightButton.get_rect(topleft=(int(surf.get_width() - 1.5 * rightButton.get_width()),
                                                  int(surf.get_height() // 2 - rightButton.get_height() / 2 - 20)))
        surf.fill((0, 0, 0))
        surf.blit(spellSurf, (0, 0))

        surf.blit(rightButton, (int(surf.get_width() - 1.5 * rightButton.get_width()),
                                int(surf.get_height() // 2 - rightButton.get_height() / 2 - 20)))
        if rightRect.collidepoint(pos):
            shift += 1

    if shift > 0:
        leftRect = leftButton.get_rect(
            topleft=(int(.25 * leftButton.get_width()), int(surf.get_height() // 2 - leftButton.get_height() / 2 - 20)))
        surf.fill((0, 0, 0))
        surf.blit(spellSurf, (0, 0))

        surf.blit(leftButton,
                  (int(0.25 * leftButton.get_width()), int(surf.get_height() // 2 - leftButton.get_height() / 2 - 20)))
        if leftRect.collidepoint(pos):
            rightRect = rightButton.get_rect(topleft=(int(surf.get_width() - 1.5 * rightButton.get_width()),
                                                      int(surf.get_height() // 2 - rightButton.get_height() / 2 - 20)))
            surf.blit(rightButton, (int(surf.get_width() - 1.5 * rightButton.get_width()),
                                    int(surf.get_height() // 2 - rightButton.get_height() / 2 - 20)))

            shift -= 1
        if shift == 0:
            surf.fill((0, 0, 0))
            surf.blit(spellSurf, (0, 0))
        if grid * (1 + shift) < len(spellNames):
            surf.blit(rightButton, (int(surf.get_width() - 1.5 * rightButton.get_width()),
                                    int(surf.get_height() // 2 - rightButton.get_height() / 2 - 20)))

    amount = 0
    for i in range(0, columns):
        for j in range(0, rows):
            amount += 1
            if i * rows + j + grid * shift > len(spellNames) - 1:
                amount -= 1
                break
            names.append(FONT.render(spellNames[i * rows + j + grid * shift], True, [237, 190, 141], None))
            surfs.append(template)
            rects.append(surfs[i * rows + j].get_rect(topleft=(int(70 + surfs[i * rows + j].get_width() * (1 / 8 + i)),
                                                               int(70 + surfs[i * rows + j].get_height() * (
                                                                           1 / 8 + j)))))
            surf.blit(surfs[i * rows + j], (int(70 + surfs[i * rows + j].get_width() * (1 / 8 + i)),
                                            int(70 + surfs[i * rows + j].get_height() * (1 / 8 + j))))
            surf.blit(names[i * rows + j], (
            int(-names[i * rows + j].get_width() // 2 + 95 + surfs[i * rows + j].get_width() * (1 / 2 + i)),
            int(70 + surfs[i * rows + j].get_height() * (1 / 2 + j))))

    keys = ["spellDesc"] * (amount)

    if grid * (1 + shift) < len(spellNames):
        rects.append(rightRect)
        keys.append('spellRight')

    if shift > 0:
        rects.append(leftRect)
        keys.append('spellLeft')

    keys.append("levels")
    arguments['surf'] = surf
    arguments['spells'] = rects
    arguments['prevKey'] = 'levelNumbers'
    arguments['shift'] = shift
    arguments['spellNames'] = spellNames
    arguments['gridShift'] = grid * shift
    arguments['spellRects'] = rects
    return (rects, keys)


def spellClassFilter(arguments):
    pg.init()
    surf = arguments['surf']
    classes = arguments['spellClass']
    keyPrev = arguments['prevKey']
    pos = arguments['pos']

    WINDOWWIDTH = surf.get_width()
    WINDOWHEIGHT = surf.get_height()

    classNames = ['Bard', 'Cleric', 'Druid', 'Paladin', 'Ranger', 'Sorcerer', 'Warlock', 'Wizard']
    if keyPrev == 'class':
        shift = 0
        for i in range(0, len(classes)):
            if classes[i].collidepoint(pos):
                spellClass = classNames[i]
        spellNames = []
        rosterPath = "{}/SpellScrape/spellRoster.txt".format(os.getcwd())
        with open(rosterPath, 'r') as roster:
            for line in roster:
                currentPlace = line[:-1].split(',')
                print(currentPlace[1])
                for element in currentPlace:
                    if spellClass in element:
                        spellNames.append(
                            currentPlace[0].replace('[', '').replace("'", "").replace('_', ' ').replace('"', ''))

    if keyPrev == 'classChose':
        spellNames = arguments['spellNames']
        shift = arguments['shift']

    if keyPrev == 'spellDesc':
        spellNames = arguments['spellNames']
        shift = arguments['shift']

    FONT = pg.font.Font('fonts/GimletSSK.ttf', 16)

    spellSurf = pg.image.load('images/DMTB_SPELL_screen.jpg')
    spellSurf = pg.transform.scale(spellSurf, (WINDOWWIDTH, WINDOWHEIGHT))
    surf.fill((0, 0, 0))
    surf.blit(spellSurf, (0, 0))

    template = pg.image.load('images/blank_button.png')
    template = pg.transform.scale(template, (int(template.get_width() / 8), int(template.get_height() / 8)))

    rightButton = pg.image.load('images/forward-circle_button.png')
    rightButton = pg.transform.scale(rightButton, (int(rightButton.get_width() / 2), int(rightButton.get_height() / 2)))

    leftButton = pg.image.load('images/back-circle_button.png')
    leftButton = pg.transform.scale(leftButton, (int(leftButton.get_width() / 2), int(leftButton.get_height() / 2)))

    rects = []
    surfs = []
    names = []
    columns = int((WINDOWWIDTH - 200) // 200)
    rows = int((WINDOWHEIGHT - 100) // 100)
    grid = columns * rows

    if grid * (1 + shift) < len(spellNames):
        rightRect = rightButton.get_rect(topleft=(int(surf.get_width() - 1.5 * rightButton.get_width()),
                                                  int(surf.get_height() // 2 - rightButton.get_height() / 2 - 20)))
        surf.fill((0, 0, 0))
        surf.blit(spellSurf, (0, 0))

        surf.blit(rightButton, (int(surf.get_width() - 1.5 * rightButton.get_width()),
                                int(surf.get_height() // 2 - rightButton.get_height() / 2 - 20)))
        if rightRect.collidepoint(pos):
            shift += 1

    if shift > 0:
        leftRect = leftButton.get_rect(
            topleft=(int(.25 * leftButton.get_width()), int(surf.get_height() // 2 - leftButton.get_height() / 2 - 20)))
        surf.fill((0, 0, 0))
        surf.blit(spellSurf, (0, 0))

        surf.blit(leftButton,
                  (int(0.25 * leftButton.get_width()), int(surf.get_height() // 2 - leftButton.get_height() / 2 - 20)))
        if leftRect.collidepoint(pos):
            rightRect = rightButton.get_rect(topleft=(int(surf.get_width() - 1.5 * rightButton.get_width()),
                                                      int(surf.get_height() // 2 - rightButton.get_height() / 2 - 20)))
            surf.blit(rightButton, (int(surf.get_width() - 1.5 * rightButton.get_width()),
                                    int(surf.get_height() // 2 - rightButton.get_height() / 2 - 20)))

            shift -= 1
        if shift == 0:
            surf.fill((0, 0, 0))
            surf.blit(spellSurf, (0, 0))
        if grid * (1 + shift) < len(spellNames):
            surf.blit(rightButton, (int(surf.get_width() - 1.5 * rightButton.get_width()),
                                    int(surf.get_height() // 2 - rightButton.get_height() / 2 - 20)))

    amount = 0
    for i in range(0, columns):
        for j in range(0, rows):
            amount += 1
            if i * rows + j + grid * shift > len(spellNames) - 1:
                amount -= 1
                break
            names.append(FONT.render(spellNames[i * rows + j + grid * shift], True, [237, 190, 141], None))
            surfs.append(template)
            rects.append(surfs[i * rows + j].get_rect(topleft=(int(70 + surfs[i * rows + j].get_width() * (1 / 8 + i)),
                                                               int(70 + surfs[i * rows + j].get_height() * (
                                                                           1 / 8 + j)))))
            surf.blit(surfs[i * rows + j], (int(70 + surfs[i * rows + j].get_width() * (1 / 8 + i)),
                                            int(70 + surfs[i * rows + j].get_height() * (1 / 8 + j))))
            surf.blit(names[i * rows + j], (
            int(-names[i * rows + j].get_width() // 2 + 95 + surfs[i * rows + j].get_width() * (1 / 2 + i)),
            int(70 + surfs[i * rows + j].get_height() * (1 / 2 + j))))

    keys = ["spellDesc"] * (amount)

    if grid * (1 + shift) < len(spellNames):
        rects.append(rightRect)
        keys.append('spellClassRight')

    if shift > 0:
        rects.append(leftRect)
        keys.append('spellClassLeft')

    keys.append("class")
    arguments['surf'] = surf
    arguments['spells'] = rects
    arguments['prevKey'] = 'classChose'
    arguments['shift'] = shift
    arguments['spellNames'] = spellNames
    arguments['gridShift'] = grid * shift
    arguments['spellRects'] = rects
    return rects, keys
