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
        arguments['rolling'] = list(filter(None, arguments['rolling']))
        if len(arguments['rolling']) == 1:
            arguments['rolling'] = [1, arguments['rolling'][0]]
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


