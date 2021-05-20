from transformers import BertTokenizer
from tqdm import tqdm
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--input', help='path to file to tokenize')
parser.add_argument('--output', help='path to file to write tokenized output to')

args=parser.parse_args()

inp = args.input
outp = args.output

tokenizer = BertTokenizer("bert.vocab", do_lower_case=False)

fin = open(inp,"r")
fout = open(outp,"w")

for l in tqdm(fin):
    tokens = tokenizer.tokenize(l)
    fout.write(" ".join(tokens[:])+"\n")

fin.close()
fout.close()
