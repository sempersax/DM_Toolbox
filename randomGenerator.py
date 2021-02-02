import numpy as np
import os
import pygame as pg
import random

def randomEncounter(playerLevels, difficulty):
    easy = np.array([25,50,75,125,250,300,350,450,550,600,800,1000,1100,1250,1400,1600,2000,2100,2400,2800])
    medium = easy *2
    hard = easy*3
    deadly = easy *4
    cr = np.array([[0, 10], [1/8, 25], [1/4, 50], [1/2, 100], [1, 200], [2, 450], [3,700], [4, 1100], [5, 1800], [6, 2300], [7, 2900], [8, 3900], [9,5000], [10, 5900], [11, 7200], [12, 8400], [13, 10000], [14, 11500], [15, 13000], [16, 15000], [17, 18000], [18, 20000], [19, 22000], [20, 25000], [21, 33000], [22, 41000], [23, 50000], [24, 62000], [25, 75000], [26, 90000], [27, 105000], [28, 120000], [29, 135000], [30, 155000]])

    
    playerNumber = len(playerLevels)
    if difficulty == 'easy':
        diff = easy
        monsterNumber = np.random.randint(1,np.ceil(playerNumber/2)+1)
    if difficulty == 'medium':
        diff = medium
        monsterNumber = np.random.randint(np.ceil(playerNumber/2),playerNumber+1)
    if difficulty == 'hard':
        diff = hard
        monsterNumber = np.random.randint(playerNumber, np.ceil(3*playerNumber/2)+1)
    if difficulty == 'deadly':
        diff = deadly
        monsterNumber = np.random.randint(np.ceil(3*playerNumber/2),2*playerNumber+1)
    

    xpThreshold = 0
    for i in range(0,playerNumber):
        xpThreshold += diff[playerLevels[i]-1]

    monsterValue = xpThreshold / monsterNumber

    crThresh = cr[:,1]-monsterValue
    crIndex = np.argmax(crThresh >= 0.)

    topXP = cr[crIndex][1]
    monstValues = [monsterNumber,0]
    crValues = [cr[crIndex][0]]
    type2 = 0
    
    while topXP * monsterNumber > xpThreshold:
        monsterNumber -= 1
        type2 += 1
        monstValues = [monsterNumber, type2]
        crValues = [cr[crIndex][0],cr[crIndex-1][0]]

    print('XP Threshold = ', xpThreshold)
    print('XP Total = ', topXP * monstValues[0] + cr[crIndex-1][1]*monstValues[1])
    for j in range(0,len(monstValues)):
        for i in range(0,monstValues[j]):
            print('\nMonster '+str(i+1 + j*monstValues[0]), '\nCR: ', crValues[j])

    monstNames = [[]]

    if len(monstValues) > 1:
        for i in range(1, len(monstValues)):
            monstNames.append([])
    rosterPath = "{}/MonsterScrape/monsterRoster.txt".format(os.getcwd())
    with open(rosterPath, 'r') as roster:
        for line in roster:
            #print(line)
            currentPlace = line[:-2].split(',')
            currentPlace[0] = currentPlace[0].replace('[','').replace(']','').replace("'","").replace('"','')
            currentPlace[1] = currentPlace[1].replace('[','').replace(']','').replace("'","").replace(' ','').replace('l','1').replace('"','')
            currentPlace[-2] = currentPlace[-2].replace('[','').replace(']','').replace("'","").replace(' ','').replace('l','1').replace('"','')
            if '/' in currentPlace[-2]:
                currentPlace[-2] = currentPlace[-2].split('/')
                currentPlace[-2] = int(currentPlace[-2][0]) / int(currentPlace[-2][1])

            currentPlace[-2] = int(currentPlace[-2])
            if currentPlace[-2] == crValues[0]:
                #print(currentPlace)
                monstNames[0].append(currentPlace[0])
            try:
                if currentPlace[-2] == int(crValues[1]):
                    monstNames[1].append(currentPlace[0])
            except:
                pass
    #print(monstNames)
    names = []
    for i in range(0, len(monstValues)):
        names += random.sample(monstNames[i],monstValues[i])

    print('\n',names)
