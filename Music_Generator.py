import numpy as np
import os
import pygame as pg

def battleMusic(SURFS):
    _files = os.listdir('music/Battle_Music')
    song = [k for k in _files if 'ogg' in k]
    number = np.random.randint(len(song))
    pg.mixer.init()
    songPlay = pg.mixer.music.load('music/Battle_Music/'+str(song[number]))
    pg.mixer.music.play(loops = -1)
    keys = ['tavern', 'battle', 'region', 'quest']
    return(SURFS,SURFS[1], keys)

def tavernMusic(SURFS):
    _files = os.listdir('music/Tavern_Music')
    song = [k for k in _files if 'ogg' in k]
    number = np.random.randint(len(song))
    pg.mixer.init()
    songPlay = pg.mixer.music.load('music/Tavern_Music/'+str(song[number]))
    pg.mixer.music.play(loops = -1)
    keys = ['tavern', 'battle', 'region', 'quest']
    return(SURFS,SURFS[1], keys)

def menuMusic(SURFS):
    pg.mixer.init()
    menuSounds = pg.mixer.music.load("music/boss_dungeon.ogg")
    pg.mixer.music.play()
    keys = ['tavern', 'battle', 'region', 'quest']
    return(SURFS,SURFS[1], keys)
