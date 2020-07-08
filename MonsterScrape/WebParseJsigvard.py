from lxml import html
from lxml.cssselect import CSSSelector
import requests, os, json

def monsterParse(webString,monsterString):
    
    #Downloads the page data for the webpage passed in as webString
    page = requests.get(webString)
    tree = html.fromstring(page.text)
    
    #Setting up a logging file in the cwd
    cwd = os.getcwd()
    with open("{}\logs.txt".format(cwd),'a') as logFile:
        try:
            #Primary scraping block
            monsterName = monsterString

            #setting up to scrape all of the following from <span> tags
            sel = CSSSelector('span')
            results = sel(tree)
            data = [result.text_content() for result in results]          
            monsterLanguages = ''
            monsterSkills = ''
            monsterHP = ''
            monsterImmunities = ''
            monsterResistances = ''
            monsterCImmunities = ''
            monsterSavings = ''
            monsterSenses = ''
            monsterVulnerabilities = ''
            monsterSpecials = ''
            monsterActions = ''
            monsterSpells = ''
            spells = ''
            imin = 0
              
            
            for i in range(0, len(data)):
                #checking for size and alignment in the same entry to try and circumvent actions that also have alignment or size in them 
                if 'Tiny' in data[i] or 'Small' in data[i] or 'Medium' in data[i] or 'Large' in data[i] or 'Huge' in data[i] or 'Gargantuan' in data[i]:
                    if 'good' in data[i] or 'evil' in data[i] or 'neutral' in data[i] or 'alignment' in data[i] or 'unaligned' in data[i] or 'construct':
                        monsterType = data[i]
                elif 'Armor Class' in data[i]:
                    monsterArmor = data[i]
                elif 'Skills' in data[i]:
                    monsterSkills = data[i]
                elif 'Senses' in data[i]:
                    monsterSenses = data[i]
                elif 'Languages' in data[i]:
                    monsterLanguages = data[i]
                elif 'Hit Points' in data[i]:
                    monsterHP = data[i]
                elif 'Speed' in data[i]:
                    monsterSpeed = data[i]
                elif 'Saving Throws' in data[i]:
                    monsterSavings = data[i]
                elif 'Damage Immunities' in data[i]:
                    monsterImmunities = data[i]
                elif 'Damage Resistances' in data[i]:
                    monsterResistances = data[i]
                elif 'Condition Immunities' in data[i]:
                    monsterCImmunities = data[i]
                elif 'Damage Vulnerabilities' in data[i]:
                    monsterVulnerabilities = data[i]
                elif 'Roll20' in data[i]:
                    imin = i+1
                elif 'Actions' in data[i]:
                    monsterActions = data[i:]
                    monsterSpecials = data[imin:i]
                    break



#The following three were in a noticeably different format, this grabs them in a different way to put in properly. a.attack -> <a class = "attack">
            sel = CSSSelector('a.attack')
            results = sel(tree)
            traits = [result.text_content() for result in results]
            for i in range(0,len(traits)):
                if 'Legendary Actions' in traits[i]:
                    tempLegend = traits[i]
                elif 'Roar' in traits[i]:
                    tempRoar = traits[i]
                elif 'Spellcasting' in traits[i] and 'Innate' not in traits[i]:
                    tempSpells = traits[i]
                    
                elif 'Innate' in traits[i]:
                    tempInnate = traits[i]
                   

#These were in a different format.  Grabs them in a different way to put in properly
            for i in range(0, len(monsterActions)):
                if 'Roar' in monsterActions[i]:
                    monsterActions[i] = tempRoar
                elif 'Legendary Actions' in monsterActions[i]:
                    monsterActions[i] = tempLegend
                    
#Spellcasting was in a different format.  This grabs it in a different way to put in properly
            for i in range(0, len(monsterSpecials)):
                if 'Spellcasting' in monsterSpecials[i] and 'Innate' not in monsterSpecials[i] and 'Shared' not in monsterSpecials[i]:
                    monsterSpecials[i] = tempSpells
                    
                elif 'Innate' in monsterSpecials[i]:
                    monsterSpecials[i] = tempInnate
                    

#Strangely, CR wasn't in <span> like the rest
            challenge = tree.xpath('//div[./b[.="Challenge"]]/text()')
            for i in range(0,len(challenge)):
                if '\n' not in challenge[i]:
                    monsterChallenge = 'Challenge ' + str(challenge[i])

#This grabs the ability scores and modifiers from the table
            sel = CSSSelector('tr')
            results = sel(tree)
            match = results[1]
            data = match.text_content()
            data = str(data)
            data = data.split(')')
            datatemp = data[0:len(data)-1]
            data = datatemp
            for i in range(0,len(data)):
                data[i] = data[i]+')'

            monsterSTR = data[0]
            monsterDEX = data[1]
            monsterCON = data[2]
            monsterINT = data[3]
            monsterWIS = data[4]
            monsterCHA = data[5]

            
            #Putting everything into the monster Dictionary
            monsterD = {
                "monsterName" : monsterName,
                "monsterType" : monsterType,
                "monsterArmor": monsterArmor,
                "monsterHP" : monsterHP,
                "monsterSpeed" : monsterSpeed,
                "monsterSTR" : monsterSTR,
                "monsterDEX" : monsterDEX,
                "monsterCON" : monsterCON,
                "monsterINT" : monsterINT,
                "monsterWIS" : monsterWIS,
                "monsterCHA" : monsterCHA,
                "monsterSavings" : monsterSavings,
                "monsterSkills" : monsterSkills,
                "monsterVulnerabilities" : monsterVulnerabilities,
                "mosnterResistances" : monsterResistances,
                "monsterImmunities" : monsterImmunities,
                "monsterCImmunities" : monsterCImmunities,
                "monsterSenses" : monsterSenses,
                "monsterLanguages" : monsterLanguages,
                "monsterChallenge" : monsterChallenge,
                "monsterSpecials" : monsterSpecials,
                "monsterActions" : monsterActions
            }
            print('Success: Dumping monster statistics to {}.json'.format(monsterName.replace(' ','_').replace('/','_')))
            
            #Dumping the dictionary to a json file in the cwd\monsterJsons_Master\ directory
            with open("{}\monsterJsons_Master\{}.json".format(cwd,monsterName.replace(' ','_').replace('/','_')),'w') as monsterJson:
                monsterJson.write(json.dumps(monsterD, indent=4))
                
            
        except:
            #Unfortunately I do not have a means of determining whether scraping fails from a formatting issue, or a page not existing,
            #so I have a singular catch all exception and kinda need to deal with it. On a normal run more than 400 monsters are properly
            #scraped, so I'll call this a success.
            print("An unexpected error has occured. Could not scrape information from {}".format(webString))
            #Only logging when failing, less to look at that way
            logFile.write("Failed to scrape data from {}\n".format(webString))
            
