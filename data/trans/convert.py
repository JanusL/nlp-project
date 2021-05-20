import xml.etree.ElementTree as ET
import os
import numpy as np


files = os.listdir('raw')

f = {}
f["en"] = open("src-raw.txt", 'w')
f["sl"] = open("tgt-raw.txt", 'w')

fs = [f[:-7] for f in files if 'en' in f]
for i in range(len(fs)):
    filename = {'en' : f'{fs[i]}-en', 'sl' :  f'{fs[i]}-sl'}
    tree = {fn : ET.parse(f'raw/{filename[fn]}.tei') for fn in filename}
    root = {fn : tree[fn].getroot()  for fn in tree}


    #with open(f"trans/{filename['en']}.txt", 'w') as f['en'], open(f"trans/{filename['sl']}.txt", 'w') as f['sl']:

    for c in root['en'][0][0]:
        if c is None or c.text is None or len(c.text)==0:
            print(c.tag, c.attrib, c.text)
            continue
        
        fi = root['sl'][0][0].find(f".*[@id='{c.attrib['corresp']}']")
        
        if fi is None or fi.text is None or len(fi.text)==0:
            print(fi.tag, fi.attrib, fi.text)
            continue
        f['en'].write(c.text.replace('\n', ' ') + "\n")
        f['sl'].write(fi.text.replace('\n', ' ') + "\n")
