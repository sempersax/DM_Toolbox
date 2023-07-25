# NPC Roster 
# by Torrey Saxton
import numpy as np
#import xlrd as pyxl
import pandas

wb = pandas.read_excel('NPC_Roster.xlsx')

def dragonBornMaleNames():
    global wb
    drMale = wb['DR_MALE'].values
    drMale = np.asarray(drMale,dtype=str)
    drMale = drMale[drMale != 'nan']
    return(str(drMale[np.random.randint(len(drMale))]))

def dragonBornFemaleNames():
    global wb
    drFemale = wb['DR_FEMALE'].values
    drFemale = np.asarray(drFemale,dtype=str)
    drFemale = drFemale[drFemale !='nan']
    return(str(drFemale[np.random.randint(len(drFemale))]))

def dragonBornLastNames():
    global wb
    drLast = wb['DR_LAST'].values
    drLast = np.asarray(drLast,dtype=str)
    drLast = drLast[drLast !='nan']
    return(str(drLast[np.random.randint(len(drLast))]))

def dwarfMaleNames():
    global wb
    dwMale = wb['DW_MALE'].values
    dwMale = np.asarray(dwMale,dtype=str)
    dwMale = dwMale[dwMale !='nan']
    return(str(dwMale[np.random.randint(len(dwMale))]))

def dwarfFemaleNames():
    global wb
    dwFemale = wb['DW_FEMALE'].values
    dwFemale = np.asarray(dwFemale,dtype=str)
    dwFemale = dwFemale[dwFemale !='nan']
    return(str(dwFemale[np.random.randint(len(dwFemale))]))

def dwarfLastNames():
    global wb
    dwLast = wb['DW_LAST'].values
    dwLast = np.asarray(dwLast,dtype=str)
    dwLast = dwLast[dwLast !='nan']
    return(str(dwLast[np.random.randint(len(dwLast))]))

def elfMaleNames():
    global wb
    elfMale = wb['ELF_MALE'].values
    elfMale = np.asarray(elfMale,dtype=str)
    elfMale = elfMale[elfMale !='nan']
    return(str(elfMale[np.random.randint(len(elfMale))]))

def elfFemaleNames():
    global wb
    elfFemale = wb['ELF_FEMALE'].values
    elfFemale = np.asarray(elfFemale,dtype=str)
    elfFemale = elfFemale[elfFemale !='nan']
    return(str(elfFemale[np.random.randint(len(elfFemale))]))

def elfLastNames():
    global wb
    elfLast = wb['ELF_LAST'].values
    elfLast = np.asarray(elfLast,dtype=str)
    elfLast = elfLast[elfLast !='nan']
    return(str(elfLast[np.random.randint(len(elfLast))]))

def gnomeMaleNames():
    global wb
    gnomeMale = wb['GNM_MALE'].values
    gnomeMale = np.asarray(gnomeMale,dtype=str)
    gnomeMale = gnomeMale[gnomeMale !='nan']
    return(str(gnomeMale[np.random.randint(len(gnomeMale))]))

def gnomeFemaleNames():
    global wb
    gnomeFemale = wb['GNM_FEMALE'].values
    gnomeFemale = np.asarray(gnomeFemale,dtype=str)
    gnomeFemale = gnomeFemale[gnomeFemale !='nan']
    return(str(gnomeFemale[np.random.randint(len(gnomeFemale))]))

def gnomeLastNames():
    global wb
    gnomeLast = wb['GNM_LAST'].values
    gnomeLast = np.asarray(gnomeLast,dtype=str)
    gnomeLast = gnomeLast[gnomeLast !='nan']
    return(str(gnomeLast[np.random.randint(len(gnomeLast))]))

def goblinMaleNames():
    global wb
    goblinMale = wb['GOB_MALE'].values
    goblinMale = np.asarray(goblinMale,dtype=str)
    goblinMale = goblinMale[goblinMale !='nan']
    return(str(goblinMale[np.random.randint(len(goblinMale))]))

def goblinFemaleNames():
    global wb
    goblinFemale = wb['GOB_FEMALE'].values
    goblinFemale = np.asarray(goblinFemale,dtype=str)
    goblinFemale = goblinFemale[goblinFemale !='nan']
    return(str(goblinFemale[np.random.randint(len(goblinFemale))]))

def goblinLastNames():
    global wb
    goblinLast = wb['GOB_LAST'].values
    goblinLast = np.asarray(goblinLast,dtype=str)
    goblinLast = goblinLast[goblinLast !='nan']
    return(str(goblinLast[np.random.randint(len(goblinLast))]))

def hElfMaleNames():
    global wb
    hElfMale = wb['HELF_MALE'].values
    hElfMale = np.asarray(hElfMale,dtype=str)
    hElfMale = hElfMale[hElfMale !='nan']
    return(str(hElfMale[np.random.randint(len(hElfMale))]))

def hElfFemaleNames():
    global wb
    hElfFemale = wb['HELF_FEMALE'].values
    hElfFemale = np.asarray(hElfFemale,dtype=str)
    hElfFemale = hElfFemale[hElfFemale !='nan']
    return(str(hElfFemale[np.random.randint(len(hElfFemale))]))

def hElfLastNames():
    global wb
    hElfLast = wb['HELF_LAST'].values
    hElfLast = np.asarray(hElfLast,dtype=str)
    hElfLast = hElfLast[hElfLast !='nan']
    return(str(hElfLast[np.random.randint(len(hElfLast))]))

def hOrcMaleNames():
    global wb
    hOrcMale = wb['HORC_MALE'].values
    hOrcMale = np.asarray(hOrcMale,dtype=str)
    hOrcMale = hOrcMale[hOrcMale !='nan']
    return(str(hOrcMale[np.random.randint(len(hOrcMale))]))

def hOrcFemaleNames():
    global wb
    hOrcFemale = wb['HORC_FEMALE'].values
    hOrcFemale = np.asarray(hOrcFemale,dtype=str)
    hOrcFemale = hOrcFemale[hOrcFemale !='nan']
    return(str(hOrcFemale[np.random.randint(len(hOrcFemale))]))

def hOrcLastNames():
    global wb
    hOrcLast = wb['HORC_LAST'].values
    hOrcLast = np.asarray(hOrcLast,dtype=str)
    hOrcLast = hOrcLast[hOrcLast !='nan']
    return(str(hOrcLast[np.random.randint(len(hOrcLast))]))

def halflingMaleNames():
    global wb
    halflingMale = wb['HFNG_MALE'].values
    halflingMale = np.asarray(halflingMale,dtype=str)
    halflingMale = halflingMale[halflingMale !='nan']
    return(str(halflingMale[np.random.randint(len(halflingMale))]))

def halflingFemaleNames():
    global wb
    halflingFemale = wb['HFNG_FEMALE'].values
    halflingFemale = np.asarray(halflingFemale,dtype=str)
    halflingFemale = halflingFemale[halflingFemale !='nan']
    return(str(halflingFemale[np.random.randint(len(halflingFemale))]))

def halflingLastNames():
    global wb
    halflingLast = wb['HFNG_LAST'].values
    halflingLast = np.asarray(halflingLast,dtype=str)
    halflingLast = halflingLast[halflingLast !='nan']
    return(str(halflingLast[np.random.randint(len(halflingLast))]))

def humanMaleNames():
    global wb
    humMale = wb['HUM_MALE'].values
    humMale = np.asarray(humMale,dtype=str)
    humMale = humMale[humMale !='nan']
    return(str(humMale[np.random.randint(len(humMale))]))

def humanFemaleNames():
    global wb
    humFemale = wb['HUM_FEMALE'].values
    humFemale = np.asarray(humFemale,dtype=str)
    humFemale = humFemale[humFemale !='nan']
    return(str(humFemale[np.random.randint(len(humFemale))]))

def humanLastNames():
    global wb
    humLast = wb['HUM_LAST'].values
    humLast = np.asarray(humLast,dtype=str)
    humLast = humLast[humLast !='nan']
    return(str(humLast[np.random.randint(len(humLast))]))

def orcMaleNames():
    global wb
    orcMale = wb['ORC_MALE'].values
    orcMale = np.asarray(orcMale,dtype=str)
    orcMale = orcMale[orcMale !='nan']
    return(str(orcMale[np.random.randint(len(orcMale))]))

def orcFemaleNames():
    global wb
    orcFemale = wb['ORC_FEMALE'].values
    orcFemale = np.asarray(orcFemale,dtype=str)
    orcFemale = orcFemale[orcFemale !='nan']
    return(str(orcFemale[np.random.randint(len(orcFemale))]))

def orcLastNames():
    global wb
    orcLast = wb['ORC_LAST'].values
    orcLast = np.asarray(orcLast,dtype=str)
    orcLast = orcLast[orcLast !='nan']
    return(str(orcLast[np.random.randint(len(orcLast))]))
