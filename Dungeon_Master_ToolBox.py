# Dungeon Master Toolbox
# By Torrey Saxton
# This is the main program.  Currently handles all events.

import pygame as pg
import sys
import Menu_Generator as menGen
import Music_Generator as musGen
import Music_Controls as musCon
import Tool_Navigator as toolNav
import Music_Navigator as musNav
import Char_Navigator as charNav
import NPC_Generator as npcGen
# import PC_Generator as pcGen
import Spell_Navigator as spNav
import Monster_Navigator as monNav
import Dice_Roller as dice

import monsterCardDMTB as mc
import spellCardDMTB as sc

from pygame.locals import *

import datetime

global WINDOWHEIGHT, WINDOWWIDTH

WINDOWWIDTH = 1000
WINDOWHEIGHT = 629

FPS = 30


def main():
    global WINDOWHEIGHT, WINDOWWIDTH, FPSCLOCK

    pg.init()
    pg.mixer.init()
    FPSCLOCK = pg.time.Clock()
    DISPLAYSURF = pg.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), HWSURFACE | DOUBLEBUF | RESIZABLE)
    #  surfs = [DISPLAYSURF]
    pg.display.set_caption('Dungeon Master Toolbox')
    loadingScreen = pg.image.load('images/Loading_screen.jpg')
    loadingScreen = pg.transform.scale(loadingScreen, (WINDOWWIDTH, WINDOWHEIGHT))
    DISPLAYSURF.blit(loadingScreen, (0, 0))
    pg.display.update()
    pos = (0, 0)

    # This is the heart of the program - all of these key value pairs tell the program which function to call and when
    dispatcher = {
        "menu": menGen.createMenu,
        "quest": toolNav.createTools,
        # Character Keys
        "characters": charNav.createChar,
        "NPC": npcGen.race,
        "gender": npcGen.gender,
        "name": npcGen.name,
        "diceRoller": dice.diceRoller,
        # Music Keys
        "music": musNav.createMusic,
        "tavern": musGen.tavernMusic,
        "battle": musGen.battleMusic,
        "region": None,
        # Spell Keys
        "spells": spNav.createSpell,
        "class": spNav.createClasses,
        "classChose": spNav.spellClassFilter,
        "spellClassLeft": spNav.spellClassFilter,
        "spellClassRight": spNav.spellClassFilter,
        "levels": spNav.createLevels,
        "levelNumbers": spNav.spellLevelFilter,
        "spellLeft": spNav.spellLevelFilter,
        "spellRight": spNav.spellLevelFilter,
        "spellDesc": sc.spellCard,
        # Monster Keys
        "monsters": monNav.createMonster,
        "alphabet": monNav.AZSelector,
        "letter": monNav.monsterLetterFilter,
        "right": monNav.monsterLetterFilter,
        "left": monNav.monsterLetterFilter,
        "monsterStats": mc.monsterStatCard,
        "cr": monNav.CRSelector,
        "crNumbers": monNav.monsterCRFilter,
        "monstCRRight": monNav.monsterCRFilter,
        "monstCRLeft": monNav.monsterCRFilter,
        "monstDesc": mc.monsterStatCard,
        "searchMonst": monNav.searchMonster,
        "rightSearch": monNav.searchMonster,
        "leftSearch": monNav.searchMonster
    }
    arguments = {
        'surf': DISPLAYSURF,
        'text': ''
    }
    KEYOLD = 'menu'
    KEY = 'menu'
    KEYS = []
    startTime = datetime.datetime.now()

    while True:
        checkForQuit()
        runTime = datetime.datetime.now() - startTime
        elapsed = runTime.total_seconds()
        if KEY == 'menu' and elapsed >= 3.:
            arguments['pos'] = pos
            rects, KEYS = dispatcher[KEY](arguments)
            #  DISPLAYSURF = arguments['surf']
            pg.display.update()

            startTime = datetime.datetime.now()

        for event in pg.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYUP:
                if KEY == 'searchMonst':
                    if event.key != K_BACKSPACE and 96 < event.key < 124:
                        arguments['text'] += str(pg.key.name(event.key))
                        arguments['keyPress'] = event.key
                    elif event.key == K_BACKSPACE:
                        arguments['text'] = arguments['text'][:-1]
                    else:
                        pass
                elif KEY == 'diceRoller':
                    if 47 < event.key < 58 or event.key == 100:
                        arguments['text'] += str(pg.key.name(event.key))
                        arguments['keyPress'] = event.key
                    elif event.key == K_BACKSPACE:
                        arguments['text'] = arguments['text'][:-1]
                    elif event.key == K_RETURN:
                        arguments['text'] = "ROLL ME BABY"
                KEYOLD = ''

                if event.key == K_ESCAPE:
                    terminate()

            if event.type == MOUSEBUTTONUP:
                pos = pg.mouse.get_pos()
                for i in range(0, len(rects)):
                    if rects[i].collidepoint(event.pos):
                        KEY = KEYS[i]
                        if 'ight' in KEY or 'eft' in KEY:
                            KEYOLD = ''
            if event.type == pg.VIDEORESIZE:
                WINDOWWIDTH, WINDOWHEIGHT = event.size
                DISPLAYSURF = pg.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), HWSURFACE | DOUBLEBUF | RESIZABLE)
                DISPLAYSURF.fill((0, 0, 0))
                pg.display.update()
                KEYOLD = ''

        if KEY != KEYOLD:
            arguments['pos'] = pos
            try:
                # arguments, rects, KEYS = dispatcher[KEY](**arguments)
                rects, KEYS = dispatcher[KEY](arguments)

                #  DISPLAYSURF = arguments['surf']

                if KEY != 'menu':
                    menRect = menGen.reachMenu(arguments)
                    backRect = toolNav.createBack(arguments)
                    arguments['choice'] = KEY
                    miniKeys, miniRects = toolNav.createMiniTools(arguments)
                    KEYS.append('menu')
                    KEYS = KEYS + miniKeys
                    rects = rects + backRect + menRect + miniRects
            except:
                print(KEY)
                print("Unexpected error:", sys.exc_info()[0])
                raise
                # pass

            pg.display.update()
        KEYOLD = KEY


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
