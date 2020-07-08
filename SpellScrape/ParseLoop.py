from lxml import html
from WebParse import spellParse
import requests, os

#All the Jsons are written to a subfolder called SpellsJsons, but if you don't have the directory it crashes. This will make sure the directory is created
cwd = os.getcwd()
try:
    os.mkdir("{}\SpellJsons_Master".format(cwd))
except OSError:
    print("Creation of directory failed, or was not neccessary.")
else:
    print("Successfully created directory {}\SpellJsons".format(cwd))

#Downloading the page that contains all spells indexed on the site.
#Note, that this site indexes some spells that link to no description, so that is where a majority of errors comes from.v
page = requests.get('http://dnd5e.wikidot.com/spells')

tree = html.fromstring(page.content)

#Scraping the spell list and truncating a few links that are unneccessary.
spellList = tree.xpath('//*[@id="page-content"]/div/div/div/div/p/a/text()')[:-9]
spellList.remove('Healing Spirit')
spellList.remove('Mind Spike')
spellList.remove('Shadow Blade')
spellList.remove('Catnap')
spellList.remove('Life Transference')
spellList.remove('Summon Lesser Demons')
spellList.remove('Thunder Step')
spellList.remove('Tiny Servant')
spellList.remove('Charm Monster')
spellList.remove('Find Greater Steed')
spellList.remove('Shadow of Moil')
spellList.remove('Sickening Radiance')
spellList.remove('Summon Greater Demon')
spellList.remove('Danse Macabre')
spellList.remove('Dawn')
spellList.remove('Enervation')
spellList.remove('Far Step')
spellList.remove('Holy Weapon')
spellList.remove('Infernal Calling')
spellList.remove('Negative Energy Flood')
spellList.remove('Skill Empowerment')
spellList.remove('Steel Wind Strike')
spellList.remove('Synaptic Static')
spellList.remove('Wall of Light')
spellList.remove('Wrath of Nature')
spellList.remove('Create Homunculus')
spellList.remove('Druid Grove')
spellList.remove('Mental Prison')
spellList.remove('Scatter')
spellList.remove('Soul Cage')
spellList.remove("Tenser's Transformation")
spellList.remove('Crown of Stars')
spellList.remove('Power Word: Pain')
spellList.remove('Temple of the Gods')
spellList.remove('Illusory Dragon')
spellList.remove('Maddening Daze')
spellList.remove('Mighty Fortress')
spellList.remove('Invulnerability')
spellList.remove('Mass Polymorph')
spellList.remove('Psychic Scream')
print(len(spellList))


#Main loop to scrape each website in the main list
for spell in spellList:
    
    #A few spells are indexed on the site with an Unearthed Arcana tag, but it is not included in the webpage.
    #This statement will quickly truncate that and move on.
    if spell.find('(UA)') >= 0:
        spellString = spell.replace('(UA)','').strip()
    else:
        spellString = spell
    
    #One spot that this could probably be written better is if I used a re dictionary to cover these replacements,
    #But I havent taken the time to learn re yet, and these four replaces seem to do the trick anyways.
    spellParse("http://dnd5e.wikidot.com/spell:{}".format(spellString.replace(' ','-').replace('\'','').replace(':','').replace('/','-')))
