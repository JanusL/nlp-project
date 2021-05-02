from transformers import BertTokenizer
from tqdm import tqdm

tokenizer = BertTokenizer("bert.vocab", do_lower_case=False)

fin = open("clean_testset.sl","r")
fout = open("tgt-test.txt","w")

for l in tqdm(fin):
    #encode = tokenizer(l)
    #tokens = tokenizer.convert_ids_to_tokens(encode["input_ids"])
    tokens = tokenizer.tokenize(l)
    fout.write(" ".join(tokens[:])+"\n")

fin.close()
fout.close()
