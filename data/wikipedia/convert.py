import xml.etree.ElementTree as ET
import os

fs = ['raw/en/wiki0.sl-en.xml', 'raw/sl/wiki0.sl-en.xml']

print(fs)

#assert 0

#for i in range(len(fs)):
filename = {'en' : f'{fs[0][:-10]}-en', 'sl' :  f'{fs[1][:-10]}-sl'}
tree = {'en': ET.parse(fs[0]), 'sl': ET.parse(fs[1])}
root = {l: tree[l].getroot() for l in tree}

f = {}
with open("src-raw.txt", 'w') as f['en'], open("tgt-raw.txt", 'w') as f['sl']:

	for ch in root['en'][1]:
		#print(ch.tag, ch.attrib)

		sent = []
		for chunk in ch:
			if chunk.text is not None:
				sent.append(chunk.text)
			for w in chunk:
				sent.append(w.text)
		#print(sent)

		ch2 = root['sl'][1].find(f".*[@id='{int(ch.attrib['id'])+1}']")
		#print(ch2.tag, ch2.attrib)
		sent2 = []
		for w in ch2:
			sent2.append(w.text)
		#print(sent2)

		sent = " ".join(sent).replace('\n', '')
		sent2 = " ".join(sent2).replace('\n', '')
		#print(sent, sent2)


		f['en'].write(sent + "\n")
		f['sl'].write(sent2 + "\n")

                
