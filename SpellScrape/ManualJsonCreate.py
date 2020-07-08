import json, os

#Spell Descriptors
spellName = "Acid Splash"
spellSchool = "Conjuration"
spellClasses = "Sorcerer, Wizard"
spellLevel = "Cantrip"
castingTime = "1 Action"
spellDuration = "Instantaneous"
spellRange = "60 ft"
spellEffect = "You hurl a bubble of acid. Choose one or two creatures you can see within range. If you choose two, they must be within 5 feet of each other. A target must succeed on a Dexterity saving throw or take 1d6 acid damage. This spell’s damage increases by 1d6 when you reach 5th level (2d6), 11th level (3d6), and 17th level (4d6)."
verbalBool = True
somaticBool = True
materialBool = False
materials = "N/A"


spellD = {
    "spellName":spellName,
    "spellSchool":spellSchool,
    "spellClasses":spellClasses,
    "spellLevel":spellLevel,
    "castingTime":castingTime,
    "spellDuration":spellDuration,
    "spellRange":spellRange,
    #"saveBool":saveBool,
    "spellEffect":spellEffect,
    "verbalBool":verbalBool,
    "somaticBool":somaticBool,
    "materialBool":materialBool,
    "materials":materials
}
print(type(spellD))
cwd = os.getcwd()
with open("{}\SpellJsons\{}.json".format(cwd,spellName.replace(" ","_")),"w") as file:
    file.write(json.dumps(spellD, indent=4))

