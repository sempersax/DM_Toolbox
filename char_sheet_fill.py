import os
import pdfrw
import json
import numpy as np

#write_fillable_pdf('DnD_5e_Blank.pdf', 'Bofa')

char_sheet_path = 'DnD_5e_Blank.pdf'


ANNOT_KEY = '/Annots'
ANNOT_FIELD_KEY = '/T'
ANNOT_VAL_KEY = '/V'
ANNOT_RECT_KEY = '/Rect'
SUBTYPE_KEY = '/Subtype'
WIDGET_SUBTYPE_KEY = '/Widget'

stat_dict =dict([
    ('STR' , '20'),
    ('STRmod','+5'),
    ('DEX' , '20'),
    ('DEXMod','+5'),
    ('CON' , '20'),
    ('CONmod','+5'),
    ('INT' , '20'),
    ('INTmod','+5'),
    ('WIS' , '20'),
    ('WISmod','+5'),
    ('CHA' , '20'),
    ('CHamod','+5'),
    ('characterName' , 'Leroy Jenkins'),
    ('CLASS LEVEL' , ['Druid',3]),
    ('PLAYER NAME' , 'Bofa'),
    ('RACE' , 'Human'),
    ('BACKGROUND1','underdog'),
    ('ProfBonus','+2'),
    ('AGE','66'),
    ('spellCastingClass','Druid')
    ])

##def generate_stat_dict():
##    

def json_import(json_file):
    with open(json_file) as file:
        data = json.load(file)

    return(data)

def spell_dict(CLASS,LEVEL):
    mypath="../SpellScrape/SpellJsons/"
    onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
    #print(onlyfiles)
    spellList=[None]*len(onlyfiles)
    for i in range(0,len(onlyfiles)):
        with open(mypath+onlyfiles[i]) as json_file:
            data = json.load(json_file)
            for j in range(0,len(data['spellClasses'])):
                if data['spellClasses'][j] == CLASS:
                    print(data['spellName'])
                    if data['spellLevel'] <= LEVEL:
                        spellList[i]=[data['spellName'],data['spellLevel'],CLASS,data['spellSave'],
                                      data['castingTime'],data['spellRange'],data['verbalBool'],
                                      data['somaticBool'],data['materialBool'],data['spellDuration']]
                        
    spellList=list(filter(None, spellList))
    spellList=sorted(spellList,key=lambda x: x[1])
    return(spellList)


def write_fillable_pdf(input_pdf_path, char_name):
    data_dict = json_import('characters/'+char_name+'.json')
    template_pdf = pdfrw.PdfReader(input_pdf_path)
    template_pdf.Root.AcroForm.update(pdfrw.PdfDict(NeedAppearances=pdfrw.PdfObject('true')))

    CLASS = data_dict['class1']
    LEVEL = data_dict['level1']
    spellDict= spell_dict(CLASS,LEVEL)
    #print(spellDict)
    data_dict['spellName1']='=== CANTRIPS ==='
    data_dict['spellSource1']='(At Will)'
    mod=1
    count1 = 0
    count2 = 0
    count3 = 0
    for i in range(1,len(spellDict)):
        data_dict['spellName'+str(i+mod)]=spellDict[i][0]
        #print(data_dict['spellName'+str(i+mod)],' ',i+mod)
        data_dict['spellSource'+str(i+mod)]=spellDict[i][2]
        data_dict['spellSaveAtk'+str(i+mod)]=spellDict[i][3]
        data_dict['spellTime'+str(i+mod)]=spellDict[i][4]
        data_dict['spellRange'+str(i+mod)]=spellDict[i][5]
        if spellDict[i][6] == 'True':
            count1 = 3
        if spellDict[i][7] == 'True':
            count2 = 5
        if spellDict[i][8] == 'True':
            count3 = 7
        count = count1+count2+count3
        if count == 3:
            data_dict['spellComp'] = 'V'
        if count == 5:
            data_dict['spellComp'] = 'S'
        if count == 7:
            data_dict['spellComp'] = 'M'
        if count == 8:
            data_dict['spellComp'] = 'V,S'
        if count == 10:
            data_dict['spellComp'] = 'V,M'
        if count == 12:
            data_dict['spellComp'] = 'M,S'
        if count == 15:
            data_dict['spellComp'] = 'V,S,M'
        data_dict['spellDuration'+str(i+mod)]=spellDict[i][9]
        if i < len(spellDict)-1:
            if spellDict[i+1][1] != spellDict[i][1]:
                mod = mod+1
                data_dict['spellName'+str(i+mod)] = '=== '+str(spellDict[i+2][1]) +' ==='

            
        
        
    #print(data_dict)
    for i in range(0,4):#len(template_pdf.pages)):
        annotations = template_pdf.pages[i][ANNOT_KEY]
        for annotation in annotations:
            #print(annotation[SUBTYPE_KEY])
            if annotation[ANNOT_FIELD_KEY]:
                key = annotation[ANNOT_FIELD_KEY][1:-1]
                #print('    \"'+str(key)+'\": \"\",')
                if key in data_dict.keys():
                    annotation.update(
                        pdfrw.PdfDict(V='{}'.format(data_dict[key]))
                        )

    output_pdf_path='characters/'+char_name+'.pdf'
    pdfrw.PdfWriter().write(output_pdf_path, template_pdf)


