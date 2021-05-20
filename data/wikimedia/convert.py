import xml.etree.ElementTree as ET
import os
import numpy as np
import re
import tqdm

fs = 'wikimedia'
filename = {'en' : f'raw/en/wikimedia-v20210402', 'sl' :  f'raw/sl/wikimedia-v20210402', 'dict' : f'raw/en-sl'}

tree = {}

tree['dict'] = ET.parse(f'{filename["dict"]}.tmp')  
rootd = tree['dict'].getroot()

# which ones we need
num_en = []
num_sl = []

for child in rootd[0]:
    e, s = child.attrib['xtargets'].split(';')

    [num_sl.append(i) for i in s.split(' ')]
    [num_en.append(i) for i in e.split(' ')]

tree['sl'] = ET.parse(f'{filename["sl"]}.xml')
root = tree['sl'].getroot()

# slovenian

sent_sl = {}
for c in root:
    if c.attrib['id'] in num_sl:
        sent = " ".join([w.text for w in c])
        sent_sl[c.attrib['id']] = sent


# english 

tree['en'] = ET.iterparse(f'{filename["en"]}.xml')  

sent_en = {}
sent = []
curr_sent = False
num_sent = 0
for i, e in enumerate(tree['en']):
    _, el = e

    if el.tag == 's':
        # end of sentence
        if len(sent)>0:
            num_sent += 1
            sent_en[el.attrib['id']] = " ".join(sent)
            
        # write previous
        curr_sent = False
        sent = []
        el.clear()
        continue
    
    if curr_sent:
        sent.append(el.text)
        el.clear()
        continue
    
    ide = el.attrib['id'].split('.')[0]
    
    if ide in num_en:
        curr_sent = True
        sent.append(el.text)
    el.clear()
    
# write to files

f = {}
with open("src-raw.txt", 'w') as f['en'], open("tgt-raw.txt", 'w') as f['sl']:
    for child in rootd[0]:
        e, s = child.attrib['xtargets'].split(';')

        sn = s.split(' ')
        en = e.split(' ')
        
        txt = ''
        for i in en:
            txt += sent_en[i]
            txt += ' '
        f['en'].write(txt)
        
        txt2 = ''
        for i in sn:
            txt2 += sent_sl[i]
            txt2 += ' '
        f['sl'].write(txt2)
