# Sound Control Script
# Meant to generate the soundSurf and soundRect in the main code
# Controls whether or not music is playing

import pygame as pg

def soundControl(surf, change, busy):
    if change == 1:
        soundSurf = pg.image.load('images/sound_on.png')
        soundSurf = pg.transform.scale(soundSurf, (int(soundSurf.get_width()/8),int(soundSurf.get_height()/8)))
        soundRect = soundSurf.get_rect()
        surf.blit(soundSurf, (0,0))
        if busy == 0:
            playing = True
        elif busy == 1:
            playing = True
    if change == 0:
        soundSurf = pg.image.load('images/sound_off.png')
        soundSurf = pg.transform.scale(soundSurf, (int(soundSurf.get_width()/8),int(soundSurf.get_height()/8)))
        soundRect = soundSurf.get_rect()
        surf.blit(soundSurf, (0,0))
        if busy == 1:
            playing = False
        elif busy == 0:
            playing = False
    return(surf,soundSurf, soundRect, playing)
