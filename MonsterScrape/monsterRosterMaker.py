import json
import os

cwd = os.getcwd()
mypath="{}/MonsterJsons/".format(cwd)
monsterNames = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
onlyFiles = monsterNames
alphaCR = []
for i in range(0, len(onlyFiles)):
    with open(mypath+onlyFiles[i]) as json_file:
        data = json.load(json_file)
        data['monsterChallenge'] = data['monsterChallenge'].split(' ')
        data['monsterChallenge'] = data['monsterChallenge'][2]
        alphaCR.append([data['monsterName'],data['monsterChallenge']])

print(alphaCR)
with open('{}/monsterRoster.txt'.format(cwd),'w') as roster:
    for listitem in alphaCR:
        roster.write('%s\n' % listitem)
