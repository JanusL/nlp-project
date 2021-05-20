import xml.etree.ElementTree as ET
import os
import numpy as np

enfile = open("src-raw.txt", 'w')
slfile = open("tgt-raw.txt", 'w')

for i in range(1, 10):
    filename = {'en' : f'spook_en-sl_L0{i:02}-en', 'sl' :  f'spook_en-sl_L0{i:02}-sl'}
    tree = {fn : ET.parse(f'raw/{filename[fn]}.xml') for fn in filename}
    root = {fn : tree[fn].getroot()  for fn in tree}

    f = {}
    with open(f"text/{filename['en']}.txt", 'w') as f['en'], open(f"text/{filename['sl']}.txt", 'w') as f['sl']:

        for c in root['en'][1][0]:
            sent = []
            if len(c) == 0:
                continue
            for x in c[0]:
                sent.append(x.text)
                
            fi = root['sl'][1][0].find(f".*[@n='{int(c.attrib['n'])}']")
            if fi is None or len(fi) == 0:
                continue
            f['en'].write(" ".join(sent) + "\n")
            enfile.write(" ".join(sent) + "\n")
            sent = []
            for x in fi[0]:
                sent.append(x.text)
            f['sl'].write(" ".join(sent) + "\n")
            slfile.write(" ".join(sent) + "\n")
