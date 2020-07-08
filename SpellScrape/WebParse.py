from lxml import html
import requests, os, json

def spellParse(webString):
    
    #Downloads the page data for the webpage passed in as webString
    page = requests.get(webString)
    tree = html.fromstring(page.content)

    #Setting up a logging file in the cwd
    cwd = os.getcwd()
    with open("{}\logs.txt".format(cwd),'a') as logFile:
        try:
            #Primary scraping block
            spellName = tree.xpath('//*[@id="skrollr-body"]/div[3]/div[1]/main/div/div/div/div/div[1]/span/text()')[0]
            if '/' in spellName:
                spellName = spellName.replace('/','_')
            if ':' in spellName:
                spellName = spellName.replace(':','')
                
            #Logic to determine if the spell is a Cantrip or Higher Level as their respective text is formatted differently
            tempDesc = tree.xpath('//*[@id="page-content"]/p[1]/em/text()')[0].split()
            #print(tempDesc)
            if 'cantrip' in tempDesc:
                spellSchool = tempDesc[0]
                spellLevel = tempDesc[1]
            else:
                spellSchool = tempDesc[1]
                spellLevel = tempDesc[0]
            
            #Scraping the list of all classes that can use the spell
            spellClasses = tree.xpath('//*[@id="page-content"]/p/a/text()')
            
            #Scraping the body text of the page and assigning it to its respective spot
            bodyTxtBlock = tree.xpath('//*[@id="page-content"]/p/text()')

            castingTime = bodyTxtBlock[0].lstrip()
            spellDuration = bodyTxtBlock[6].lstrip()
            spellRange = bodyTxtBlock[2].lstrip()
            
            #Logic to determine where a the description ends, anormally there are some \n characters at the end of each paragraph that can get included.
            for textBlock in bodyTxtBlock[7:]:
                if len(textBlock) <= 2:
                    endPos = bodyTxtBlock.index(textBlock)
                    break
            spellEffect = " ".join(bodyTxtBlock[7:endPos])
            
            #Determining the components needed for each spell
            components = bodyTxtBlock[4].replace(',',' ').split()

            if 'V' in components:
                verbalBool = 'True'
            else:
                verbalBool = 'False'
                
            if 'S' in components:
                somaticBool = 'True'
            else:
                somaticBool = 'False'

            if 'M' in components:
                materialBool = 'True'
            else:
                materialBool = 'False'
            
            #If materials are needed, then list them, otherwise they will be saved as "N/A"
            if materialBool == 'True':
                materials = " ".join(components[components.index('M')+1:])
            else:
                materials = "N/A"
            
            #Putting everything into the Spell Dictionary
            spellD = {
                "spellName":spellName,
                "spellSchool":spellSchool,
                "spellClasses":spellClasses,
                "spellLevel":spellLevel,
                "castingTime":castingTime,
                "spellDuration":spellDuration,
                "spellRange":spellRange,
                "spellEffect":spellEffect,
                "verbalBool":verbalBool,
                "somaticBool":somaticBool,
                "materialBool":materialBool,
                "materials":materials
            }
            
            print('Success: Dumping spell statistics to {}.json'.format(spellName.replace(' ','_')))
            
            #Dumping the dictionary to a json file in the cwd\SpellJsons\ directory
            with open("{}\SpellJsons_Master\{}.json".format(cwd,spellName.replace(' ','_')),'w') as spellJson:
                spellJson.write(json.dumps(spellD, indent=4))
##            with open("{}\SpellJsons_Master\{}.json".format(cwd,spellName.replace('/','_')),'w') as spellJson:
##                spellJson.write(json.dumps(spellD, indent=4))
                
            #Logging whether the spell was created properly
            logFile.write("Successfully created {}.json\n".format(spellName.replace(' ','_')))
            
        except:
            #Unfortunately I do not have a means of determining whether scraping fails from a formatting issue, or a page not existing,
            #so I have a singular catch all exception and kinda need to deal with it. On a normal run more than 400 spells are properly
            #scraped, so I'll call this a success.
            print("An unexpected error has occured. Could not scrape information from {}".format(webString))
            logFile.write("Failed to scrape data from {}\n".format(webString))
            yabbadabba
