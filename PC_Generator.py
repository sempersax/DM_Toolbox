# This is for creating a player character.
# Much of this will be very similar to an NPC, but
# now there is a need for stats.
import numpy as np
import time

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
    return(stats)

def statAssignment(vocation,race,stats):
    if vocation == 'BARBARIAN':
        const = stats[-1]
        stren = stats[-2]
        dex = stats[-3]
        char = stats[-4]
        wis = stats[-5]
        intel = stats[-6]

    if vocation == 'BARD':
        const = stats[-3]
        stren = stats[-5]
        dex = stats[-2]
        char = stats[-1]
        wis = stats[-4]
        intel = stats[-6]

    if vocation == 'CLERIC':
        #if focus == 'MELEE':
        const = stats[-3]
        stren = stats[-2]
        dex = stats[-5]
        char = stats[-4]
        wis = stats[-1]
        intel = stats[-6]
        # A cleric can be close or ranged, stats need to reflect choice.
##        if focus == 'RANGED':
##        const = stats[-3]
##        stren = stats[-5]
##        dex = stats[-2]
##        char = stats[-4]
##        wis = stats[-1]
##        intel = stats[-6]            
        

    if vocation == 'DRUID':
        const = stats[-3]
        stren = stats[-6]
        dex = stats[-2]
        char = stats[-4]
        wis = stats[-1]
        intel = stats[-5]

    if vocation == 'FIGHTER':
        #if focus == 'MELEE':
        const = stats[-2]
        stren = stats[-1]
        dex = stats[-3]
        char = stats[-4]
        wis = stats[-5]
        intel = stats[-6]
        # A fighter can be close or ranged, stats need to reflect choice.
##        if focus == 'RANGED':
##        const = stats[-2]
##        stren = stats[-3]
##        dex = stats[-1]
##        char = stats[-4]
##        wis = stats[-5]
##        intel = stats[-6]  
        # A fighter can be close or ranged, stats need to reflect choice.
##        if focus == 'MELEE ELDRITCH':
##        const = stats[-3]
##        stren = stats[-1]
##        dex = stats[-5]
##        char = stats[-4]
##        wis = stats[-6]
##        intel = stats[-2]  
        # A fighter can be close or ranged, stats need to reflect choice.
##        if focus == 'RANGED ELDRITCH':
##        const = stats[-3]
##        stren = stats[-5]
##        dex = stats[-1]
##        char = stats[-4]
##        wis = stats[-6]
##        intel = stats[-2]
    if vocation == 'MONK':
        const = stats[-3]
        stren = stats[-6]
        dex = stats[-1]
        char = stats[-4]
        wis = stats[-2]
        intel = stats[-5]

    if vocation == 'PALADIN':
        const = stats[-2]
        stren = stats[-1]
        dex = stats[-4]
        char = stats[-3]
        wis = stats[-5]
        intel = stats[-6]

    if vocation == 'RANGER':
        const = stats[-3]
        stren = stats[-6]
        dex = stats[-1]
        char = stats[-4]
        wis = stats[-2]
        intel = stats[-5]

    if vocation == 'ROGUE':
        #if focus == 'THIEF'
        const = stats[-4]
        stren = stats[-3]
        dex = stats[-1]
        char = stats[-2]
        wis = stats[-5]
        intel = stats[-6]
##        #if focus == 'ASSASSIN'
##        const = stats[-4]
##        stren = stats[-5]
##        dex = stats[-1]
##        char = stats[-2]
##        wis = stats[-3]
##        intel = stats[-6]
##        #if focus == 'ARCANE TRICKSTER'
##        const = stats[-3]
##        stren = stats[-6]
##        dex = stats[-1]
##        char = stats[-4]
##        wis = stats[-5]
##        intel = stats[-2]

    if vocation == 'SORCERER':
        const = stats[-3]
        stren = stats[-6]
        dex = stats[-2]
        char = stats[-1]
        wis = stats[-4]
        intel = stats[-5]

    if vocation == 'WARLOCK':
        const = stats[-2]
        stren = stats[-5]
        dex = stats[-3]
        char = stats[-1]
        wis = stats[-4]
        intel = stats[-6]

    if vocation == 'WIZARD':
        # Only stats that matter are Int being highest and Str being lowest.
        # Unless player cares, randomize
        rand = [2,3,4,5]
        cRand = rand[np.randomint(len(rand))]
        rand = rand[rand != cRand]
        dRand = rand[np.randomint(len(rand))]
        rand = rand[rand != dRand]
        chRand = rand[np.randomint(len(rand))]
        rand = rand[rand != chRand]
        wRand = rand[np.randomint(len(rand))]
        rand = rand[rand != wRand]
        const = stats[-cRand]
        dex = stats[-dRand]
        char = stats[-chRand]
        wis = stats[-wRand]
        stren = stats[-6]
        intel = stats[-1]

    # Ability Modifiers for a given race.  Half-Elf needs worked out.  Subraces
    # need to be implemented as a kwarg.
    if race == 'DRAGONBORN':
        stren = stren + 2
        char = char + 1
    
    if race == 'DWARF':
        const = const + 2
    
    if race == 'ELF':
        dex = dex + 2
    
    if race == 'GNOME':
        intel = intel + 2
    
    if race == 'HALF-ELF':
        char = char + 2
    
    if race == 'HALFLING':
        dex = dex + 2
    
    if race == 'HALF-ORC':
        const = const + 1
        stren = stren + 2
    
    if race == 'HUMAN':
        const = const + 1
        stren = stren + 1
        dex = dex + 1
        char = char + 1
        wis = wis + 1
        intel = intel + 1
    
    if race == 'TIEFLING':
        char = char + 2
        intel = intel + 1
    
        

    print('Race: ',race,'\nClass: ',vocation,'\nStrength: ',stren, '\nDexterity: ',dex,'\nConstitution: ',const,
          '\nIntelligence: ',intel, '\nWisdom: ',wis, '\nCharisma: ',char)
    return
