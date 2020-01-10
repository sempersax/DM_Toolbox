# This script is to preload all of the images
# This will prevent them being loaded multiple times as a script is called
# and speed up ingame runtimes, as there won't be a wait for images to load
# Will delay start up though, as intention is to call this immediately at start
# program.
import pygame as pg
import numpy as np
import os
import time

pg.init()

def imageLoader():
    raceFiles = os.listdir('images/races')
    start = time.time()
    races=[None]*len(raceFiles)
    prefix = ['images/races/']*len(raceFiles)
    for i in range(len(raceFiles)): #this loads all of the race images at once.
        raceFiles[i] = prefix[i]+raceFiles[i]
        races[i] = pg.image.load(raceFiles[i])
        races[i] = pg.transform.scale(races[i], (int(races[i].get_width()/8),int(races[i].get_height()/8)))

    #Here we load the tool hub buttons, and their miniature versions
    toolFiles = os.listdir('images/tools')
    circTools = [k for k in toolFiles if 'CIRCLE' in k]
    toolFiles = [k for k in toolFiles if not 'CIRCLE' in k]
    prefix = ['images/tools/']*len(toolFiles)
    tools = [None]*len(toolFiles)
    circs = [None]*len(circTools)
    for i in range(len(toolFiles)): #this loads all of the tool images at once.
        toolFiles[i] = prefix[i]+toolFiles[i]
        tools[i] = pg.image.load(toolFiles[i])
        tools[i] = pg.transform.scale(tools[i], (int(tools[i].get_width()/8),int(tools[i].get_height()/8)))
    #for i in range(len(circTools)):
        circTools[i] = prefix[i]+circTools[i]
        circs[i] = pg.image.load(circTools[i])
        circs[i] = pg.transform.scale(circs[i], (int(circs[i].get_width()/2),int(circs[i].get_height()/2)))
    print(time.time()-start)
    return(races,tools, circs)
