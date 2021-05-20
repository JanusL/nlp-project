from transformers import BertTokenizer
from tqdm import tqdm
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--input', help='path to file to clean')
parser.add_argument('--output', help='path to file to write cleaned output to')

args=parser.parse_args()

inp = args.input
outp = args.output

fin = open(inp,"r")
fout = open(outp,"w")

# ” “ „ « »  ‘ ’ • – —

for l in tqdm(fin):
    l = l.replace('&quot;', '"').replace('”','"').replace('“','"').replace('„','"').replace('»','"').replace('«','"')
    l = l.replace('&apos;', "'").replace('‘',"'").replace('’',"'")
    l = l.replace('•','-').replace('–','-').replace('—','-')

    fout.write(l)


fin.close()
fout.close()
