from transformers import BertTokenizer
from tqdm import tqdm

tokenizer = BertTokenizer("bert.vocab", do_lower_case=False)

fin = open("asistent_testset.sl","r")
fout = open("clean_testset.sl","w")

# ” “ „ « »  ‘ ’ • – —

for l in tqdm(fin):
    l = l.replace('&quot', '"').replace('”','"').replace('“','"').replace('„','"').replace('»','"').replace('«','"')
    l = l.replace('&apos', "'").replace('‘',"'").replace('’',"'")
    l = l.replace('•','-').replace('–','-').replace('—','-')
    #encode = tokenizer(l)
    #tokens = tokenizer.convert_ids_to_tokens(encode["input_ids"])
    #tokens = tokenizer.tokenize(l)
    fout.write(l)
    #print(l[:-1])
    #break

fin.close()
fout.close()
