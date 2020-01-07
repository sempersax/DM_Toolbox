import numpy as np
import os
import pygame as pg

##def battleMusic():
##    _files = os.listdir('music')
##    music = [k for k in _files if 'ogg' in k]
##    number = np.random.randint(len(music))
##    print(music)
##    print(str(music[number]))
##    song = 'Octopath Traveler (Switch) - Battle 1 (Soundtrack sample)'
##
##    pg.mixer.init()
##    fight = pg.mixer.music("music/Battle_1.ogg")
##    pg.mixer.music.play(loops = -1)
##    return

def menuMusic():
    pg.mixer.init()
    menuSounds = pg.mixer.music.load("music/boss_dungeon.ogg")
    pg.mixer.music.play()
    return
