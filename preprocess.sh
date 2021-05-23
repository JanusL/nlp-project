#!/bin/bash

echo "Tokenizing testset...."

python scripts/cleanup.py --input data/nlp/asistent_testset.en --output data/nlp/src-test-clean.txt & \
python scripts/cleanup.py --input data/nlp/asistent_testset.sl --output data/nlp/tgt-test-clean.txt

python scripts/bert_tokenize.py --input data/nlp/src-test-clean.txt --output data/nlp/src-test-token.txt & \
python scripts/bert_tokenize.py --input data/nlp/tgt-test-clean.txt --output data/nlp/tgt-test-token.txt

wait

echo "Tokenizing TC3... It has more than 24 000 000 lines, so this will take about 2 hours..."

python scripts/cleanup.py --input data/nlp/TC3.en --output data/nlp/src-clean.txt & \
python scripts/cleanup.py --input data/nlp/TC3.sl --output data/nlp/tgt-clean.txt

python scripts/bert_tokenize.py --input data/nlp/src-clean.txt --output data/nlp/src-token.txt & \
python scripts/bert_tokenize.py --input data/nlp/tgt-clean.txt --output data/nlp/tgt-token.txt

wait

declare -a arr=("random" "spook" "trans" "wikimedia" "wikipedia")

for i in "${arr[@]}"
do
    echo "Tokenizing $i...."
    python scripts/cleanup.py --input data/$i/src-raw.txt --output data/$i/src-clean.txt & \
    python scripts/cleanup.py --input data/$i/tgt-raw.txt --output data/$i/tgt-clean.txt

    python scripts/bert_tokenize.py --input data/$i/src-clean.txt --output data/$i/src-token.txt & \
    python scripts/bert_tokenize.py --input data/$i/tgt-clean.txt --output data/$i/tgt-token.txt

wait
done

echo "Tokenizing orwel...."

python scripts/cleanup.py --input data/orwel/elan-orwl-en.txt --output data/orwel/src-clean.txt & \
python scripts/cleanup.py --input data/orwel/elan-orwl-sl.txt --output data/orwel/tgt-clean.txt

python scripts/bert_tokenize.py --input data/orwel/src-clean.txt --output data/orwel/src-token.txt & \
python scripts/bert_tokenize.py --input data/orwel/tgt-clean.txt --output data/orwel/tgt-token.txt

wait

echo "Tokenizing hp..."

python scripts/cleanup.py --input data/spook/text/spook_en-sl_L004-en.txt --output data/spook/src-clean-hp.txt & \
python scripts/cleanup.py --input data/spook/text/spook_en-sl_L004-sl.txt --output data/spook/tgt-clean-hp.txt

python scripts/bert_tokenize.py --input data/spook/src-clean-hp.txt --output data/spook/src-token-hp.txt & \
python scripts/bert_tokenize.py --input data/spook/tgt-clean-hp.txt --output data/spook/tgt-token-hp.txt

wait

echo "Tokenizing lotr..."

python scripts/cleanup.py --input data/spook/text/spook_en-sl_L005-en.txt --output data/spook/src-clean-lotr.txt & \
python scripts/cleanup.py --input data/spook/text/spook_en-sl_L005-sl.txt --output data/spook/tgt-clean-lotr.txt

python scripts/bert_tokenize.py --input data/spook/src-clean-lotr.txt --output data/spook/src-token-lotr.txt & \
python scripts/bert_tokenize.py --input data/spook/tgt-clean-lotr.txt --output data/spook/tgt-token-lotr.txt




