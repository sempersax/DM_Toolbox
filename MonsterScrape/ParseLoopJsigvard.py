from lxml import html
from WebParseJsigvard import monsterParse
import requests, os

#All the Jsons are written to a subfolder called SpellsJsons, but if you don't have the directory it crashes. This will make sure the directory is created
cwd = os.getcwd()
try:
    os.mkdir("{}\MonsterJsons_Master".format(cwd))
except OSError:
    print("Creation of directory failed, or was not neccessary.")
else:
    print("Successfully created directory {}\MonsterJsons_Master".format(cwd))

#Downloading the page that contains all spells indexed on the site.
#Note, that this site indexes some spells that link to no description, so that is where a majority of errors comes from.v
page = requests.get('https://jsigvard.com/dnd/Monsters.html')

tree = html.fromstring(page.content)


monsterList = tree.xpath('//*[@id="example"]/tbody/tr/td[1]/a/text()')[:]
monsterList = sorted(monsterList)
print(len(monsterList))

    #Main loop to scrape each website in the main list
for monster in monsterList:
    
    #A few spells are indexed on the site with an Unearthed Arcana tag, but it is not included in the webpage.
    #This statement will quickly truncate that and move on.
##    if monster.find('(UA)') >= 0:
##        monsterString = monster.replace('(UA)','').strip()
##    else:
    monsterString = monster
    
    #One spot that this could probably be written better is if I used a re dictionary to cover these replacements,
    #But I havent taken the time to learn re yet, and these four replaces seem to do the trick anyways.
        #print("https://www.dandwiki.com/wiki/5e_SRD:{}".format(monsterString.replace(' ','_').replace(':','').replace("\'",'%27')))
    monsterParse("https://jsigvard.com/dnd/monster.php?m={}".format(monsterString.replace(' ','%20').replace(':','').replace("\'",'')),monsterString)
