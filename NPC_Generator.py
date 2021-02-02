import numpy as np
import os
import pygame as pg
import time
import NPC_Roster as roster


def race(arguments):
    arguments['raceSel'] = None
    surf = arguments['surf']
    pg.init()
    FONT = pg.font.Font('fonts/GimletSSK.ttf', 24)
    WINDOWWIDTH = surf.get_width()
    WINDOWHEIGHT = surf.get_height()
    template = pg.image.load('images/blank_button.png')
    template = pg.transform.smoothscale(template, (
        int(template.get_width() / 8 * WINDOWWIDTH / 1000), int(template.get_height() / 8 * WINDOWHEIGHT / 629)))

    races = ['Aasimar', 'Dragonborn', 'Dwarf', 'Elf', 'Gnome', 'Goblin', 'Half-Elf', 'Half-Orc', 'Halfling', 'Human',
             'Orc', 'Tiefling']

    names = []

    raceRects = []
    surf.fill((0, 0, 0))
    image = pg.image.load('images/navigation_screen.png')
    image = pg.transform.scale(image, (WINDOWWIDTH, WINDOWHEIGHT))
    surf.blit(image, (0, 0))

    for i in range(0, 3):
        for j in range(0, 4):
            names.append(FONT.render(races[j + i * 4], True, [237, 190, 141], None))
            position = (int(surf.get_width() // 3 + template.get_width() * (i)),
                        int(surf.get_height() / 5 + template.get_height() * (j)))
            surf.blit(template, position)
            raceRects.append(template.get_rect(topleft=position))
            surf.blit(names[j + i * 4], (position[0] + template.get_width() / 2 - names[j + i * 4].get_width() / 2,
                                         position[1] + template.get_height() / 2 - names[j + i * 4].get_height() / 2))

    keys = ['gender'] * len(raceRects)
    keys.append('characters')
    arguments['surf'] = surf
    arguments['raceRects'] = raceRects
    return (raceRects, keys)


def gender(arguments):
    pg.init()
    surf = arguments['surf']
    rects = arguments['raceRects']
    pos = arguments['pos']
    arguments['racePos'] = pos
    WINDOWWIDTH = surf.get_width()
    WINDOWHEIGHT = surf.get_height()
    genders = [None] * 2
    genders[0] = pg.image.load('images/genders/DMTB_FEMALE_Button.png')
    genders[1] = pg.image.load('images/genders/DMTB_MALE_Button.png')
    for i in range(0, len(genders)):
        genders[i] = pg.transform.scale(genders[i], (
        int(genders[i].get_width() / 8 * WINDOWWIDTH / 1000), int(genders[i].get_height() / 8 * WINDOWHEIGHT / 629)))

    races = ['AASIMAR', 'DRAGONBORN', 'DWARF', 'ELF', 'GNOME', 'GOBLIN', 'HALF-ELF', 'HALF-ORC', 'HALFLING', 'HUMAN',
             'ORC', 'TIEFLING']

    for i in range(len(rects)):
        if rects[i].collidepoint(pos):
            arguments['raceSel'] = races[i]

    if arguments['raceSel'] != 'None':
        image = pg.image.load('images/navigation_screen.png')
        image = pg.transform.scale(image, (WINDOWWIDTH, WINDOWHEIGHT))
        surf.fill((0, 0, 0))
        surf.blit(image, (0, 0))
    genRects = []

    if arguments['raceSel'] != 'None':
        surf.blit(genders[0], (int(genders[0].get_width()), int(WINDOWHEIGHT / 2 - genders[0].get_height() / 2)))
        surf.blit(genders[1],
                  (int(WINDOWWIDTH - 2 * genders[1].get_width()), int(WINDOWHEIGHT / 2 - genders[1].get_height() / 2)))
        genRects.append(genders[0].get_rect(
            topleft=(int(genders[0].get_width()), int(WINDOWHEIGHT / 2 - genders[0].get_height() / 2))))
        genRects.append(genders[1].get_rect(topleft=(
        int(WINDOWWIDTH - 2 * genders[1].get_width()), int(WINDOWHEIGHT / 2 - genders[1].get_height() / 2))))

    keys = ['name'] * len(genRects)
    keys.append('NPC')
    arguments['surf'] = surf
    arguments['rectsOld'] = rects
    arguments['posOld'] = pos
    arguments['genRects'] = genRects
    arguments['prevKey'] = 'gender'
    arguments['name'] = []
    return (genRects, keys)


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
    FONT = pg.font.Font('fonts/GimletSSK.ttf', int(48 * surf.get_height() / 629))
    genders = ['FEMALE', 'MALE']

    for i in range(len(rects)):
        if rects[i].collidepoint(pos):
            genderSel = genders[i]

    if raceSel == 'DRAGONBORN':
        if genderSel == 'FEMALE':
            first = roster.dragonBornFemaleNames()
            last = roster.dragonBornLastNames()
        if genderSel == 'MALE':
            first = roster.dragonBornMaleNames()
            last = roster.dragonBornLastNames()

    if raceSel == 'DWARF':
        if genderSel == 'FEMALE':
            first = roster.dwarfFemaleNames()
            last = roster.dwarfLastNames()
        if genderSel == 'MALE':
            first = roster.dwarfMaleNames()
            last = roster.dwarfLastNames()

    if raceSel == 'ELF':
        if genderSel == 'FEMALE':
            first = roster.elfFemaleNames()
            last = roster.elfLastNames()
        if genderSel == 'MALE':
            first = roster.elfMaleNames()
            last = roster.elfLastNames()

    if raceSel == 'GNOME':
        if genderSel == 'FEMALE':
            first = roster.gnomeFemaleNames()
            last = roster.gnomeLastNames()
        if genderSel == 'MALE':
            first = roster.gnomeMaleNames()
            last = roster.gnomeLastNames()

    if raceSel == 'GOBLIN':
        if genderSel == 'FEMALE':
            first = roster.goblinFemaleNames()
            last = roster.goblinLastNames()
        if genderSel == 'MALE':
            first = roster.goblinMaleNames()
            last = roster.goblinLastNames()

    if raceSel == 'HALF-ELF':
        if genderSel == 'FEMALE':
            first = roster.hElfFemaleNames()
            last = roster.hElfLastNames()
        if genderSel == 'MALE':
            first = roster.hElfMaleNames()
            last = roster.hElfLastNames()

    if raceSel == 'HALFLING':
        if genderSel == 'FEMALE':
            first = roster.halflingFemaleNames()
            last = roster.halflingLastNames()
        if genderSel == 'MALE':
            first = roster.halflingMaleNames()
            last = roster.halflingLastNames()

    if raceSel == 'HALF-ORC':
        if genderSel == 'FEMALE':
            first = roster.hOrcFemaleNames()
            last = roster.hOrcLastNames()
        if genderSel == 'MALE':
            first = roster.hOrcMaleNames()
            last = roster.hOrcLastNames()

    if raceSel == 'HUMAN':
        if genderSel == 'FEMALE':
            first = roster.humanFemaleNames()
            last = roster.humanLastNames()
        if genderSel == 'MALE':
            first = roster.humanMaleNames()
            last = roster.humanLastNames()

    if raceSel == 'ORC':
        if genderSel == 'FEMALE':
            first = roster.orcFemaleNames()
            last = roster.orcLastNames()
        if genderSel == 'MALE':
            first = roster.orcMaleNames()
            last = roster.orcLastNames()

    if prevKey == 'name':
        first, last = arguments['name']

    raceText = FONT.render('    RACE: ' + raceSel, True, [0, 0, 0], None)
    genText = FONT.render('GENDER: ' + genderSel, True, [0, 0, 0], None)
    nameText = FONT.render('    NAME: ' + first + ' ' + last, True, [0, 0, 0], None)
    DISPLAYSURF = surf
    scroll = pg.image.load('images/character_scroll.png')
    scroll = pg.transform.scale(scroll, (WINDOWWIDTH, WINDOWHEIGHT))
    image = pg.image.load('images/navigation_screen.png')
    image = pg.transform.smoothscale(image, (WINDOWWIDTH, WINDOWHEIGHT))

    surf.fill((0, 0, 0))
    surf.blit(image, (0, 0))
    surf.blit(scroll, (0, 0))
    surf.blit(raceText, (
    int(scroll.get_width() // 2 - raceText.get_width() // 2), int(scroll.get_height() / 8 + 2 * raceText.get_height())))
    surf.blit(genText, (
    int(scroll.get_width() // 2 - genText.get_width() // 2), int(scroll.get_height() / 8 + 3 * raceText.get_height())))
    surf.blit(nameText, (int(scroll.get_width() // 2 - nameText.get_width() // 2),
                         int(scroll.get_height() / 8 + 3 * raceText.get_height() + genText.get_height())))
    cont = pg.image.load('images/tools/DMTB_NPC_CIRCLE_button.png')
    cont = pg.transform.scale(cont, (int(cont.get_width() / 2), int(cont.get_height() / 2)))
    surf.blit(cont, (int(WINDOWWIDTH - cont.get_width()), int(WINDOWHEIGHT - cont.get_height())))
    contRect = cont.get_rect(topleft=(int(WINDOWWIDTH - cont.get_width()), int(WINDOWHEIGHT - cont.get_height())))

    rects = [contRect]
    keys = ['characters', 'gender']
    arguments['surf'] = surf
    arguments['rectsOld'] = rectsOld
    arguments['posOld'] = posOld
    arguments['prevKey'] = 'name'
    arguments['name'] = (first, last)
    arguments['pos'] = posOld

    return (rects, keys)
