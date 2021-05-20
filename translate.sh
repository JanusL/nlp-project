#!/bin/bash

echo "Cleaning and tokenizing..."

python scripts/cleanup.py --input $2 --output temp/clean.txt
python scripts/bert_tokenize.py --input temp/clean.txt --output temp/token.txt

echo "Translating..."

onmt_translate -model $1 -src temp/token.txt -output temp/translated.txt -gpu 0 -verbose

echo "Detokenizing..."

python scripts/bert_detokenize.py --input temp/translated.txt --output $3

echo "Done!"
