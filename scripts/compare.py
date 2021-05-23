from transformers import BertTokenizer
from tqdm import tqdm
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--en', help='original file in english')
parser.add_argument('--sl', help='original translation to slovene, optional', default = None)
parser.add_argument('--pred', help='translation predictions of our model')
parser.add_argument('--out', help='file to write results to')

args=parser.parse_args()

fsrc = open(args.en,"r")
if args.sl is not None:
    ftgt = open(args.sl,"r")
fpred = open(args.pred,"r")
fout = open(args.out,"w")

for lp in tqdm(fpred):

    ls = fsrc.readline()
    if args.sl is not None:
        lt = ftgt.readline()

    fout.write("ANG:\n" + ls)
    if args.sl is not None:
        fout.write("SLO:\n" + lt)

    fout.write("TRANSLATION:\n" + lp)

    fout.write("\n")

fsrc.close()
if args.sl is not None:
    ftgt.close()
fpred.close()
fout.close()
