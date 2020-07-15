# This is for creating a player character.
# Much of this will be very similar to an NPC, but
# now there is a need for stats.
import numpy as np
import time
import pygame as pg
import json
import char_sheet_fill as cf

def name():
    pg.init()
    screen = pg.display.set_mode((480, 360))
    pcName = "Name?"
    font = pg.font.Font(None, 50)
    change = False
    while True:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN and change == True:
                if event.unicode.isalpha():
                    pcName += event.unicode
                elif event.key == pg.K_BACKSPACE:
                    pcName = pcName[:-1]
                elif event.key == pg.K_RETURN:
                    pg.display.quit()
                    return(pcName)

            if event.type == pg.KEYDOWN and change == False:
                if event.unicode.isalpha():
                    pcName = ""
                    pcName += event.unicode
                    change = True
                elif event.key == pg.K_BACKSPACE:
                    pcName = ""


        screen.fill((0, 0, 0))
        block = font.render(pcName, True, (255, 255, 255))
        rect = block.get_rect()
        rect.center = screen.get_rect().center
        screen.blit(block, rect)
        pg.display.flip()

def level_prompt():
    pg.init()
    screen = pg.display.set_mode((480, 360))
    level = "Level?"
    font = pg.font.Font(None, 50)
    change = False
    while True:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN and change == True:
                if event.unicode.isnumeric():
                    level += event.unicode
                elif event.key == pg.K_BACKSPACE:
                    level = level[:-1]
                elif event.key == pg.K_RETURN:
                    if int(level) > 20:
                        level = "Nice try"
                        change = False
                    else:
                        pg.display.quit()
                        return(int(level))

            if event.type == pg.KEYDOWN and change == False:
                if event.unicode.isnumeric():
                    level = ""
                    level += event.unicode
                    change = True
                elif event.key == pg.K_BACKSPACE:
                    level = ""


        screen.fill((0, 0, 0))
        block = font.render(level, True, (255, 255, 255))
        rect = block.get_rect()
        rect.center = screen.get_rect().center
        screen.blit(block, rect)
        pg.display.flip()

def statRoller():
   # Create 6 spots for stats
    stats = np.zeros(6)
    # Roll 4d6 six times to get stats
    stats = np.asarray([np.random.randint(0,high=7,size=4) for _ in range(len(stats))])
    # S
    stats = np.sort(stats, axis = 1)
    # Eliminate the lowest value from each roll
    stats = stats[:,1:]
    # Sum the rolls
    stats = np.sum(stats, axis = 1)
    # Sort from low to high
    stats = np.sort(stats, axis = 0)
    for i in range(0,len(stats)):
        stats[i] = int(stats[i])
    return(stats)

def statAssignment(vocation,race,stats,**kwargs):
    #initializing kwarg
    mypath="../Dungeon_Master_Tools/characters/"
    pcName = None
    pcName = name()

    level = None
    level = level_prompt()

    
    focus = None
    choice1 = None
    choice2 = None
    for key, value in kwargs.items():
        if key == 'focus' or key == 'FOCUS' or key == 'Focus':
            focus = value
        if key == 'choices':
            # These are for the Half-Elf getting to pick two traits
            # to add one to.
            choice1 = value[0]
            choice2 = value[1]
    print(choice1,choice2)
    if vocation == 'Barbarian':
        const = stats[-1]
        stren = stats[-2]
        dex = stats[-3]
        char = stats[-4]
        wis = stats[-5]
        intel = stats[-6]

    if vocation == 'Bard':
        const = stats[-3]
        stren = stats[-5]
        dex = stats[-2]
        char = stats[-1]
        wis = stats[-4]
        intel = stats[-6]

    if vocation == 'Cleric':
        if focus == 'MELEE' or focus == None:
            const = stats[-3]
            stren = stats[-2]
            dex = stats[-5]
            char = stats[-4]
            wis = stats[-1]
            intel = stats[-6]
        # A cleric can be close or ranged, stats need to reflect choice.
        if focus == 'RANGED':
            const = stats[-3]
            stren = stats[-5]
            dex = stats[-2]
            char = stats[-4]
            wis = stats[-1]
            intel = stats[-6]            
        

    if vocation == 'Druid':
        const = stats[-3]
        stren = stats[-6]
        dex = stats[-2]
        char = stats[-4]
        wis = stats[-1]
        intel = stats[-5]

    if vocation == 'Fighter':
        if focus == 'MELEE' or focus == None:
            const = stats[-2]
            stren = stats[-1]
            dex = stats[-3]
            char = stats[-4]
            wis = stats[-5]
            intel = stats[-6]
        # A fighter can be close or ranged, stats need to reflect choice.
        if focus == 'RANGED':
            const = stats[-2]
            stren = stats[-3]
            dex = stats[-1]
            char = stats[-4]
            wis = stats[-5]
            intel = stats[-6]  
        # An Eldritch Knight can be close or ranged, stats need to reflect choice.
        if focus == 'MELEE ELDRITCH' or focus == 'ELDRITCH':
            const = stats[-3]
            stren = stats[-1]
            dex = stats[-5]
            char = stats[-4]
            wis = stats[-6]
            intel = stats[-2]  
        # A Eldritch Knight can be close or ranged, stats need to reflect choice.
        if focus == 'RANGED ELDRITCH':
            const = stats[-3]
            stren = stats[-5]
            dex = stats[-1]
            char = stats[-4]
            wis = stats[-6]
            intel = stats[-2]
    if vocation == 'Monk':
        const = stats[-3]
        stren = stats[-6]
        dex = stats[-1]
        char = stats[-4]
        wis = stats[-2]
        intel = stats[-5]

    if vocation == 'Paladin':
        const = stats[-2]
        stren = stats[-1]
        dex = stats[-4]
        char = stats[-3]
        wis = stats[-5]
        intel = stats[-6]

    if vocation == 'Ranger':
        const = stats[-3]
        stren = stats[-6]
        dex = stats[-1]
        char = stats[-4]
        wis = stats[-2]
        intel = stats[-5]

    if vocation == 'Rogue':
        if focus == 'THIEF' or focus == None:
            const = stats[-4]
            stren = stats[-3]
            dex = stats[-1]
            char = stats[-2]
            wis = stats[-5]
            intel = stats[-6]
        if focus == 'ASSASSIN':
            const = stats[-4]
            stren = stats[-5]
            dex = stats[-1]
            char = stats[-2]
            wis = stats[-3]
            intel = stats[-6]
        if focus == 'ARCANE TRICKSTER':
            const = stats[-3]
            stren = stats[-6]
            dex = stats[-1]
            char = stats[-4]
            wis = stats[-5]
            intel = stats[-2]

    if vocation == 'Sorcerer':
        const = stats[-3]
        stren = stats[-6]
        dex = stats[-2]
        char = stats[-1]
        wis = stats[-4]
        intel = stats[-5]

    if vocation == 'Warlock':
        const = stats[-2]
        stren = stats[-5]
        dex = stats[-3]
        char = stats[-1]
        wis = stats[-4]
        intel = stats[-6]

    if vocation == 'Wizard':
        # Only stats that matter are Int being highest and Str being lowest.
        # Unless player cares, randomize
        rand = [2,3,4,5]
        cRand = rand[np.random.randint(len(rand))]
        rand.remove(cRand)
        dRand = rand[np.random.randint(len(rand))]
        rand.remove(dRand)
        chRand = rand[np.random.randint(len(rand))]
        rand.remove(chRand)
        wRand = rand[np.random.randint(len(rand))]
        rand.remove(wRand)
        const = stats[-cRand]
        dex = stats[-dRand]
        char = stats[-chRand]
        wis = stats[-wRand]
        stren = stats[-6]
        intel = stats[-1]

    # Ability Modifiers for a given race.  Half-Elf needs worked out.  Subraces
    # need to be implemented as a kwarg.
    if race == 'Dragonborn':
        stren = stren + 2
        char = char + 1
    
    if race == 'Dwarf':
        const = const + 2
    
    if race == 'Elf':
        dex = dex + 2
    
    if race == 'Gnome':
        intel = intel + 2
    
    if race == 'Half-Elf':
        char = char + 2
        if choice1 == 'CONSTITUTION' or choice2 == 'CONSTITUTION' or choice1 == None:
            const = const+1
        if choice1 == 'STRENGTH' or choice2 == 'STRENGTH':
            stren = stren+1    
        if choice1 == 'DEXTERITY' or choice2 == 'DEXTERITY':
            dex = dex+1
        if choice1 == 'CHARISMA' or choice2 == 'CHARISMA' or choice2 == None:
            char = char+1
        if choice1 == 'WISDOM' or choice2 == 'WISDOM':
            wis = wis+1
        if choice1 == 'INTELLIGENCE' or choice2 == 'INTELLIGENCE':
            intel = intel+1





    if race == 'Halfling':
        dex = dex + 2
    
    if race == 'Half-Orc':
        const = const + 1
        stren = stren + 2
    
    if race == 'Human':
        const = const + 1
        stren = stren + 1
        dex = dex + 1
        char = char + 1
        wis = wis + 1
        intel = intel + 1
    
    if race == 'Tiefling':
        char = char + 2
        intel = intel + 1
    
        

    print('Name:',pcName, '\nRace: ',race,'\nClass: ',vocation,'\nStrength: ',stren, '\nDexterity: ',dex,'\nConstitution: ',const,
          '\nIntelligence: ',intel, '\nWisdom: ',wis, '\nCharisma: ',char)
    with open(mypath+"blank_character_dict.json") as json_file:
        data = json.load(json_file)
    data['STR']=int(stren)
    data['STRmod']=int(np.floor((stren-10)/2))
    data['DEX']=int(dex)
    data['DEXmod']=int(np.floor((dex-10)/2))
    data['CON']=int(const)
    data['CONmod']=int(np.floor((const-10)/2))
    data['INT']=int(intel)
    data['INTmod']=int(np.floor((intel-10)/2))
    data['WIS']=int(wis)
    data['WISmod']=int(np.floor((wis-10)/2))
    data['CHA']=int(char)
    data['CHAmod']=int(np.floor((char-10)/2))
    data['characterName1']=pcName
    data['characterName2']=pcName
    data['class1'] = vocation
    data['level1'] = level

    with open("{}\{}.json".format(mypath,pcName),"w") as json_file:
        json_file.write(json.dumps(data, indent=4))

    cf.write_fillable_pdf('DnD_5e_Blank.pdf',pcName)
    return
