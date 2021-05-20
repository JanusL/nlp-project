from transformers import BertTokenizer
from tqdm import tqdm
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--en', help='original file in english')
parser.add_argument('--sl', help='original translation to slovene')
parser.add_argument('--pred', help='translation predictions of our model')
parser.add_argument('--out', help='file to write results to')

args=parser.parse_args()

fsrc = open(args.en,"r")
ftgt = open(args.sl,"r")
fpred = open(args.pred,"r")
fout = open(args.out,"w")

for lp in tqdm(fpred):

    ls = fsrc.readline()
    lt = ftgt.readline()

    fout.write("ANG:\n" + ls)
    fout.write("SLO:\n" + lt)

    fout.write("TRANSLATION:\n" + lp)

    fout.write("\n")

fsrc.close()
ftgt.close()
fpred.close()
fout.close()
