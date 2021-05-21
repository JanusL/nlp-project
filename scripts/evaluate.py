import nltk.translate as nt
import string
import nltk
import argparse
nltk.download('wordnet')

parser = argparse.ArgumentParser()

parser.add_argument('--original', help='original translation filepath')
parser.add_argument('--translated', help='translation from the model filepath')

args=parser.parse_args()

original = args.original
translated = args.translated

txt1 = []
txt2 = []
txt2b = []

with open(translated, 'r') as ft, open(original, 'r') as fo:
    for l1, l2 in zip(ft, fo):
        s1 = l1.replace('\n', '').translate(str.maketrans('','',string.punctuation))
        s2 = l2.replace('\n', '').translate(str.maketrans('','',string.punctuation))

        s1 = s1.split(' ')
        s2 = s2.split(' ')

        #if len(s1) <= 2 or len(s1) <= 2:
        #    continue
        
        txt1.append(s1)
        txt2b.append([s2])
        txt2.append(s2)

print(len(txt1),len(txt2))

scores = {'bleu': nt.bleu_score.corpus_bleu, 
          'chrf': nt.chrf_score.corpus_chrf,
          'gleu': nt.gleu_score.corpus_gleu,
          'meteor': nt.meteor_score.meteor_score,
          'nist': nt.nist_score.corpus_nist,
          #'ribes': nt.ribes_score.corpus_ribes
         }

for s in scores:
    if s in ['bleu', 'nist', 'gleu']:
        score = scores[s](txt2b, txt1)
    elif False and s in ['ribes']:
        corpus_best_ribes = 0.0
        # Iterate through each hypothesis and their corresponding references.
        alpha=0.25 
        beta=0.10
        w = 0
        for references, hypothesis in zip(txt2b, txt1):
            try:
                corpus_best_ribes += nt.ribes_score.sentence_ribes(references, hypothesis, alpha, beta)
            except:
                w += 1
                #print(references, hypothesis, '\n','*'*20)
                
        score = corpus_best_ribes / len(txt1)
        print(w)
    else:
        sc = 0 
        for t1, t2 in zip(txt2b, txt1):
            #print(t1, t2)
            sc += nt.meteor_score.meteor_score([" ".join(t1[0])], " ".join(t2))
        score = sc / len(txt1)

        #score = scores[s](txt2, txt1)
    print(f'{s}: {score}')
