import xml.etree.ElementTree as ET
import os

fs = os.listdir("raw")

print(fs)

#assert 0

f = {}
f['en'] = open("src-raw.txt", 'w') 
f['sl'] = open("tgt-raw.txt", 'w') 

for i in range(len(fs)):
    print(fs[i])
    filename = {'en' : f'{fs[i][:-4]}-en', 'sl' :  f'{fs[i][:-4]}-sl'}
    tree = ET.parse("raw/"+fs[i]) 
    root = tree.getroot()

    #f = {}
    #with open(f"{filename['en']}.txt", 'w') as f['en'], open(f"{filename['sl']}.txt", 'w') as f['sl']:

    for ch in root[1]:
        for c in ch:
            
            if c.tag == 'tuv' and 'en' in c.attrib['{http://www.w3.org/XML/1998/namespace}lang'] and c[0].text is not None:
                
                    for c2 in ch:
                         if c2.tag == 'tuv' and 'sl' in c2.attrib['{http://www.w3.org/XML/1998/namespace}lang'] and c2[0].text is not None:
                             c[0].text.replace('\n', ' ')
                             c2[0].text.replace('\n', ' ')
                             f['en'].write(c[0].text + "\n")
                             f['sl'].write(c2[0].text + "\n")

                
