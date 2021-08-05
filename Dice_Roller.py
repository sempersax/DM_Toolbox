import pygame as pg
import numpy as np
from pygame.locals import *

def diceRoller(arguments):
    pg.init()
    surf = arguments['surf']
    FONT = pg.font.Font('fonts/GimletSSK.ttf', 24)
    HEADER = pg.font.Font('fonts/GimletSSK.ttf', 48)
    WINDOWWIDTH = surf.get_width()
    WINDOWHEIGHT = surf.get_height()
    # The background
    toolSurf = pg.image.load('images/navigation_screen.png')
    toolSurf = pg.transform.scale(toolSurf, (WINDOWWIDTH, WINDOWHEIGHT))

    # Adding the elements to the display
    surf.fill((0, 0, 0))
    surf.blit(toolSurf, (0, 0))

    template = pg.image.load('images/blank_button.png')
    template = pg.transform.smoothscale(template, (
        int(template.get_width() / 8 * WINDOWWIDTH / 1000), int(template.get_height() / 8 * WINDOWHEIGHT / 629)))

    rollerPrompt = FONT.render("Type your roll as \"XdY\"", True, [237, 190, 141], None)
    rollerButton = pg.image.load('images/blank_button.png')
    rollerButton = pg.transform.smoothscale(rollerButton, (
        int(rollerPrompt.get_width() * 1.5), int(rollerPrompt.get_height() * 1.5)))
    surf.blit(rollerButton, (WINDOWWIDTH // 2 - rollerButton.get_width() // 2, 1.75 * rollerButton.get_height()))
    text = str(arguments['text'])

    if text == '':
        surf.blit(rollerPrompt,
                  (WINDOWWIDTH // 2 - rollerPrompt.get_width() // 2, int(1.9 * rollerButton.get_height())))
    elif text != "ROLL ME BABY" and text != '':
        #arguments['keyPress'] = ord(text[0])
        arguments['rolling'] = text.split('d')
        textText = FONT.render(text, True, [237, 190, 141], None)
        surf.fill((0, 0, 0))
        surf.blit(toolSurf, (0, 0))
        rollerButton = pg.transform.smoothscale(rollerButton, (
        int(rollerPrompt.get_width() * 1.5), int(rollerPrompt.get_height() * 1.5)))
        surf.blit(rollerButton, (WINDOWWIDTH // 2 - rollerButton.get_width() // 2, 1.75 * rollerButton.get_height()))
        surf.blit(textText, (WINDOWWIDTH // 2 - textText.get_width() // 2, int(1.9 * rollerButton.get_height())))
    else:
        #arguments['rolling'] = [num for num in arguments['rolling'] != '']
        #print(arguments['rolling'])
        rolls = np.random.randint(1, int(arguments['rolling'][1])+1, size=int(arguments['rolling'][0]))
        arguments['text'] = ''
        total = np.sum(rolls)
        totalText = FONT.render(str(total), True, [237, 190, 141], None)
        surf.fill((0, 0, 0))
        surf.blit(toolSurf, (0, 0))
        rollerButton = pg.transform.smoothscale(rollerButton, (int(rollerPrompt.get_width()*1.5), int(rollerPrompt.get_height()*1.5)))
        surf.blit(rollerButton,(WINDOWWIDTH//2 - rollerButton.get_width()//2, 1.75 * rollerButton.get_height()))
        surf.blit(totalText, (WINDOWWIDTH//2 - totalText.get_width()//2, int(1.9 * rollerButton.get_height())))




    arguments['prevKey'] = 'diceRoller'
    arguments['surf'] = surf
    rects = []
    KEYS = ['characters']
    return rects, KEYS


def rollNumber(arguments):
    pg.init()
    surf = arguments['surf']
    FONT = pg.font.Font('fonts/GimletSSK.ttf', 24)
    HEADER = pg.font.Font('fonts/GimletSSK.ttf', 48)
    WINDOWWIDTH = surf.get_width()
    WINDOWHEIGHT = surf.get_height()
    # The background
    toolSurf = pg.image.load('images/navigation_screen.png')
    toolSurf = pg.transform.scale(toolSurf, (WINDOWWIDTH, WINDOWHEIGHT))

    # Adding the elements to the display
    surf.fill((0, 0, 0))
    surf.blit(toolSurf, (0, 0))

    template = pg.image.load('images/blank_button.png')
    template = pg.transform.smoothscale(template, (
        int(template.get_width() / 8 * WINDOWWIDTH / 1000), int(template.get_height() / 8 * WINDOWHEIGHT / 629)))

    rollerPrompt = FONT.render("What type of dice are you rolling?", True, [237, 190, 141], None)
    rollerButton = pg.image.load('images/blank_button.png')
    rollerButton = pg.transform.smoothscale(rollerButton, (int(rollerPrompt.get_width()*1.5), int(rollerPrompt.get_height()*1.5)))
    surf.blit(rollerButton,(WINDOWWIDTH//2 - rollerButton.get_width()//2, 1.75 * rollerButton.get_height()))
    surf.blit(rollerPrompt, (WINDOWWIDTH//2 - rollerPrompt.get_width()//2, int(1.9 * rollerButton.get_height())))

    diceNames = ['D4', 'D6', 'D8', 'D10', 'D12', 'D20', 'D100']
    diceRects = []
    names = []
    for i in range(0, 2):
        for j in range(0, 4):
            if j + i * 4 > len(diceNames)-1:
                break
            names.append(FONT.render(diceNames[j + i * 4], True, [237, 190, 141], None))
            position = (int(surf.get_width() // 4 + template.get_width() * (i)),
                        int(surf.get_height() / 5 + template.get_height() * (j)))
            surf.blit(template, position)
            diceRects.append(template.get_rect(topleft=position))
            surf.blit(names[j + i * 4], (position[0] + template.get_width() / 2 - names[j + i * 4].get_width() / 2,
                                         position[1] + template.get_height() / 2 - names[j + i * 4].get_height() / 2))

    arguments['prevKey'] = 'diceRoller'
    arguments['surf'] = surf
    KEYS = ['numberDice']*len(diceNames)
    arguments['diceRects'] = diceRects
    return diceRects, KEYS
