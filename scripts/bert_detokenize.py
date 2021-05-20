from transformers import BertTokenizer
from tqdm import tqdm
import argparse

tokenizer = BertTokenizer("bert.vocab", do_lower_case=False)

parser = argparse.ArgumentParser()

parser.add_argument('--input', help='path to file to detokenize')
parser.add_argument('--output', help='path to file to write detokenized output to')

args=parser.parse_args()

inp = args.input
outp = args.output

fpred = open(inp,"r")
fout = open(outp,"w")

for lp in tqdm(fpred):

    lp = lp[0:-1]
    lp = lp.split(" ")

    ids = tokenizer.convert_tokens_to_ids(lp)
    text = tokenizer.decode(ids)

    fout.write(text + "\n")

fpred.close()
fout.close()
