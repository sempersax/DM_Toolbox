import json
import os

cwd = os.getcwd()
mypath="{}/SpellJsons/".format(cwd)
spellNames = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
onlyFiles = spellNames
alphaCR = []
for i in range(0, len(onlyFiles)):
    with open(mypath+onlyFiles[i]) as json_file:
        data = json.load(json_file)
        data['spellLevel'] = data['spellLevel']
        data['spellClasses'] = data['spellClasses']
        alphaCR.append([data['spellName'],data['spellClasses'],data['spellLevel']])
        print(alphaCR[i][2])
print(alphaCR)

with open('{}/spellRoster.txt'.format(cwd),'w') as roster:
    for listitem in alphaCR:
        roster.write('%s\n' % listitem)
