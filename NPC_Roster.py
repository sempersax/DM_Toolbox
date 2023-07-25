# NPC Roster 
# by Torrey Saxton
import numpy as np
import json


def open_json(file_name):
    with open(file_name, "r") as f:
        file = json.load(f)
    f.close()
    return file


def dragonBornMaleNames():
    drMale = open_json('dr_male.json')
    return(str(drMale[np.random.randint(len(drMale))]))


def dragonBornFemaleNames():
    drFemale = open_json('dr_female.json')
    return(str(drFemale[np.random.randint(len(drFemale))]))


def dragonBornLastNames():
    drLast = open_json('dr_last.json')
    return(str(drLast[np.random.randint(len(drLast))]))


def dwarfMaleNames():
    dwMale = open_json('dw_male.json')
    return(str(dwMale[np.random.randint(len(dwMale))]))


def dwarfFemaleNames():
    dwFemale = open_json('dw_female.json')
    return(str(dwFemale[np.random.randint(len(dwFemale))]))


def dwarfLastNames():
    dwLast = open_json('dw_last.json')
    return(str(dwLast[np.random.randint(len(dwLast))]))


def elfMaleNames():
    elfMale = open_json('elf_male.json')
    return(str(elfMale[np.random.randint(len(elfMale))]))


def elfFemaleNames():
    elfFemale = open_json('elf_female.json')
    return(str(elfFemale[np.random.randint(len(elfFemale))]))


def elfLastNames():
    elfLast = open_json('elf_last.json')
    return(str(elfLast[np.random.randint(len(elfLast))]))


def gnomeMaleNames():
    gnomeMale = open_json('gnm_male.json')
    return(str(gnomeMale[np.random.randint(len(gnomeMale))]))


def gnomeFemaleNames():
    gnomeFemale = open_json('gnm_female.json')
    return(str(gnomeFemale[np.random.randint(len(gnomeFemale))]))


def gnomeLastNames():
    gnomeLast = open_json('gnm_last.json')
    return(str(gnomeLast[np.random.randint(len(gnomeLast))]))


def goblinMaleNames():
    goblinMale = open_json('gob_male.json')
    return(str(goblinMale[np.random.randint(len(goblinMale))]))


def goblinFemaleNames():
    goblinFemale = open_json('gob_female.json')
    return(str(goblinFemale[np.random.randint(len(goblinFemale))]))


def goblinLastNames():
    goblinLast = open_json('gob_last.json')
    return(str(goblinLast[np.random.randint(len(goblinLast))]))


def hElfMaleNames():
    hElfMale = open_json('helf_male.json')
    return(str(hElfMale[np.random.randint(len(hElfMale))]))


def hElfFemaleNames():
    hElfFemale = open_json('helf_female.json')
    return(str(hElfFemale[np.random.randint(len(hElfFemale))]))


def hElfLastNames():
    hElfLast = open_json('helf_last.json')
    return(str(hElfLast[np.random.randint(len(hElfLast))]))


def hOrcMaleNames():
    hOrcMale = open_json('horc_male.json')
    return(str(hOrcMale[np.random.randint(len(hOrcMale))]))


def hOrcFemaleNames():
    hOrcFemale = open_json('horc_female.json')
    return(str(hOrcFemale[np.random.randint(len(hOrcFemale))]))


def hOrcLastNames():
    hOrcLast = open_json('horc_last.json')
    return(str(hOrcLast[np.random.randint(len(hOrcLast))]))


def halflingMaleNames():
    halflingMale = open_json('hfng_male.json')
    return(str(halflingMale[np.random.randint(len(halflingMale))]))


def halflingFemaleNames():
    halflingFemale = open_json('hfng_female.json')
    return(str(halflingFemale[np.random.randint(len(halflingFemale))]))


def halflingLastNames():
    halflingLast = open_json('hfng_last.json')
    return(str(halflingLast[np.random.randint(len(halflingLast))]))


def humanMaleNames():
    humMale = open_json('hum_male.json')
    return(str(humMale[np.random.randint(len(humMale))]))


def humanFemaleNames():
    humFemale = open_json('hum_female.json')
    return(str(humFemale[np.random.randint(len(humFemale))]))


def humanLastNames():
    humLast = open_json('hum_last.json')
    return(str(humLast[np.random.randint(len(humLast))]))


def orcMaleNames():
    orcMale = open_json('orc_male.json')
    return(str(orcMale[np.random.randint(len(orcMale))]))


def orcFemaleNames():
    orcFemale = open_json('orc_female.json')
    return(str(orcFemale[np.random.randint(len(orcFemale))]))


def orcLastNames():
    orcLast = open_json('orc_last.json')
    return(str(orcLast[np.random.randint(len(orcLast))]))
