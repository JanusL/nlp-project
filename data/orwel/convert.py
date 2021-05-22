import xml.etree.ElementTree as ET
import os
import numpy as np


filename = {'en' : 'elan-orwl-en', 'sl' :  'elan-orwl-sl'}
tree = {fn : ET.parse(f'{filename[fn]}.xml') for fn in filename}
root = {fn : tree[fn].getroot()  for fn in tree}

f = {}
with open(f"{filename['en']}.txt", 'w') as f['en'], open(f"{filename['sl']}.txt", 'w') as f['sl']:

    for c in root['en'][1][0]:
        sent = []
        if len(c) == 0:
            continue
        for x in c[0]:
            sent.append(x.text)
        xmlid = '{http://www.w3.org/XML/1998/namespace}id'
        
        fi = root['sl'][1][0].find(f".*[@{xmlid}='{c.attrib[xmlid]}']")
        if fi is None or len(fi) == 0:
            continue
        f['en'].write(" ".join(sent) + "\n")
        sent = []
        for x in fi[0]:
            sent.append(x.text)
        f['sl'].write(" ".join(sent) + "\n")
