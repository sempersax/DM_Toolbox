import os,json

mypath="../SpellScrape/SpellJsons_Master/"
onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
#print(onlyfiles)
spellList=[None]*len(onlyfiles)
for i in range(0,len(onlyfiles)):
    with open(mypath+onlyfiles[i]) as json_file:
        data = json.load(json_file)

        #print(data['spellLevel'])
      
        if data['spellLevel'] == 'cantrip':
            data['spellLevel'] = 0
        if data['spellLevel'] == '1st-level':
            data['spellLevel'] = 1
        if data['spellLevel'] == '2nd-level':
            data['spellLevel'] = 2
        if data['spellLevel'] == '3rd-level':
            data['spellLevel'] = 3
        if data['spellLevel'] == '4th-level':
            data['spellLevel'] = 4
        if data['spellLevel'] == '5th-level':
            data['spellLevel'] = 5
        if data['spellLevel'] == '6th-level':
            data['spellLevel'] = 6
        if data['spellLevel'] == '7th-level':
            data['spellLevel'] = 7
        if data['spellLevel'] == '8th-level':
            data['spellLevel'] = 8
        if data['spellLevel'] == '9th-level':
            data['spellLevel'] = 9

        if 'saving throw' in data['spellEffect']:
            if 'Strength saving throw' in data['spellEffect']:
                data['spellSave'] = 'STR'
                
            elif 'Dexterity saving throw' in data['spellEffect']:
                data['spellSave'] = 'DEX'
                
            elif 'Wisdom saving throw' in data['spellEffect']:
                data['spellSave'] = 'WIS'
                
            elif 'Constitution saving throw' in data['spellEffect']:
                data['spellSave'] = 'CON'
                
            elif 'Intelligence saving throw' in data['spellEffect']:
                data['spellSave'] = 'INT'
                
            elif 'Charisma saving throw' in data['spellEffect']:
                data['spellSave'] = 'CHA'
                
            else:
                data['spellSave']= '--'
                
        else:
            data['spellSave']= '--'
            
                
        
            
    os.remove(mypath+onlyfiles[i])
    with open(mypath+onlyfiles[i], 'w') as json_file:
        json.dump(data, json_file, indent=4)
        json_file.truncate()
