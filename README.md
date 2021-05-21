The repository of the NLP course project.

### To train a translation model, follow the steps bellow:

* Install OpenNMT-py, transformers, nltk and numpy using pip
* Download the vocabulary from https://huggingface.co/EMBEDDIA/crosloengual-bert (vocab.txt), rename it to bert.vocab and place it into the root directory.
* Download the needed data. SPOOK, TRANS, ORWELL (in ELAN) and RANDOM (razni TMXi - IT) can be downloaded from the onedrive and Wikipedia and Wikimedia from https://opus.nlpl.eu/.
* Put the data in apropriate folders, untill you get the folder structure bellow.
* Convert each dataset not in .txt format to .txt formats using the scripts provided in the apropriate folders. NOTE: Wikimedia is huge and requires a lot of memory and will take a lot of time to process. Wikipedia will also take about an hour. If you only wish to see how training works, you can probably skip these two.
* Run the preprocess.sh script to clean and preprocess all the data. NOTE: TC3 is a huge file, meaning this can take about an hour. You can remove TC3 part from the script if you only wish to see how training works.
* Run shuffle.py from data/nlp to shuffle TC3 data before each training start.
* Open the training.yaml script to setup the weights of each dataset
* Use onmt_train -config training.yaml to start training
* Open the finetune.yaml to setup datasets to finetune on
* Use onmt_train -config finetune.yaml to start finetuning

### To test one of the models, follow the steps bellow:

* Download the models from https://drive.google.com/drive/folders/1RgJY3nI-Vlvbt8deW3tPuvn5rWa69WHp?usp=sharing
* Run translate.sh (model) (input file) (output file)
* To calculate evaluation scores, run scripts/evaluate.py
* To generate a line-by-line english-slovene-predictions file, run scripts/compare.py

### Folder structure before converting and tokenizing:
```
data
├── nlp
│   ├── asistent_testset.en
│   ├── asistent_testset.sl
│   ├── shuffled
│   ├── shuffle.py
│   ├── TC3.en
│   └── TC3.sl
├── orwel
│   ├── convert.py
│   └── raw
│       └── orwl-txt.tei
├── random
│   ├── convert.py
│   └── raw
│       ├── Arnes_webpage_general.tmx
│       ├── FeelTheFuture_webpage_general.tmx
│       ├── hp_printer_navodila.tmx
│       ├── hp-probook-navodila.tmx
│       ├── Huawei_Y6_navodila.tmx
│       ├── Logitech_miska_navodila.tmx
│       ├── NIL_webpage_general.tmx
│       ├── Office_support.tmx
│       ├── Samsung_tablica_navodila.tmx
│       ├── Uporabna_informatika_abstrakti_2.tmx
│       ├── Uporabna_informatika_abstrakti_3.tmx
│       ├── Uporabna_informatika_abstrakti_4.tmx
│       └── uporabna_informatika_abstrakti_5.tmx
├── spook
│   ├── convert.py
│   ├── raw
│   │   ├── spook_en-sl_L001-en.xml
│   │   ├── spook_en-sl_L001-sl.xml
│   │   ├── spook_en-sl_L002-en.xml
│   │   ├── spook_en-sl_L002-sl.xml
│   │   ├── spook_en-sl_L003-en.xml
│   │   ├── spook_en-sl_L003-sl.xml
│   │   ├── spook_en-sl_L004-en.xml
│   │   ├── spook_en-sl_L004-sl.xml
│   │   ├── spook_en-sl_L005-en.xml
│   │   ├── spook_en-sl_L005-sl.xml
│   │   ├── spook_en-sl_L006-en.xml
│   │   ├── spook_en-sl_L006-sl.xml
│   │   ├── spook_en-sl_L007-en.xml
│   │   ├── spook_en-sl_L007-sl.xml
│   │   ├── spook_en-sl_L008-en.xml
│   │   ├── spook_en-sl_L008-sl.xml
│   │   ├── spook_en-sl_L009-en.xml
│   │   └── spook_en-sl_L009-sl.xml
│   └── text
├── trans
│   ├── convert.py
│   └── raw
│       ├── dajs-en.tei
│       ├── dajs-sl.tei
│       ├── dajs-xx.tei
│       ├── free-en.tei
│       ├── free-sl.tei
│       ├── free-xx.tei
│       ├── frnk-en.tei
│       ├── frnk-sl.tei
│       ├── frnk-xx.tei
│       ├── hate-en.tei
│       ├── hate-sl.tei
│       ├── hate-xx.tei
│       ├── homo-en.tei
│       ├── homo-sl.tei
│       ├── homo-xx.tei
│       ├── knj1-en.tei
│       ├── knj1-sl.tei
│       ├── knj1-xx.tei
│       ├── knjl-xx.tei
│       ├── last-en.tei
│       ├── last-sl.tei
│       ├── last-xx.tei
│       ├── levi-en.tei
│       ├── levi-sl.tei
│       ├── levi-xx.tei
│       ├── mdns-en.tei
│       ├── mdns-sl.tei
│       ├── mdns-xx.tei
│       ├── med1-en.tei
│       ├── med1-sl.tei
│       ├── med1-xx.tei
│       ├── med2-en.tei
│       ├── med2-sl.tei
│       ├── med2-xx.tei
│       ├── med3-en.tei
│       ├── med3-sl.tei
│       ├── med3-xx.tei
│       ├── mpsl-en.tei
│       ├── mpsl-sl.tei
│       ├── mpsl-xx.tei
│       ├── prag-en.tei
│       ├── prag-sl.tei
│       ├── prag-xx.tei
│       ├── rekr-en.tei
│       ├── rekr-sl.tei
│       ├── rekr-xx.tei
│       ├── romi-en.tei
│       ├── romi-sl.tei
│       ├── romi-xx.tei
│       ├── sint-en.tei
│       ├── sint-sl.tei
│       ├── sint-xx.tei
│       ├── spo1-en.tei
│       ├── spo1-sl.tei
│       ├── spo1-xx.tei
│       ├── spo2-en.tei
│       ├── spo2-sl.tei
│       ├── spo2-xx.tei
│       ├── spo3-en.tei
│       ├── spo3-sl.tei
│       ├── spo3-xx.tei
│       ├── spo4-en.tei
│       ├── spo4-sl.tei
│       ├── spo4-xx.tei
│       ├── sta1-en.tei
│       ├── sta1-sl.tei
│       ├── sta1-xx.tei
│       ├── sta2-en.tei
│       ├── sta2-sl.tei
│       ├── sta2-xx.tei
│       ├── sta3-en.tei
│       ├── sta3-sl.tei
│       ├── sta3-xx.tei
│       ├── sta4-en.tei
│       ├── sta4-sl.tei
│       ├── sta4-xx.tei
│       ├── sta5-en.tei
│       ├── sta5-sl.tei
│       ├── sta5-xx.tei
│       ├── sta6-en.tei
│       ├── sta6-sl.tei
│       ├── sta6-xx.tei
│       ├── sta7-en.tei
│       ├── sta7-sl.tei
│       ├── sta7-xx.tei
│       ├── sta8-en.tei
│       ├── sta8-sl.tei
│       ├── sta8-xx.tei
│       ├── sta9-en.tei
│       ├── sta9-sl.tei
│       ├── sta9-xx.tei
│       ├── svne-en.tei
│       ├── svne-sl.tei
│       ├── svne-xx.tei
│       ├── tei2.dtd
│       ├── tele-en.tei
│       ├── tele-sl.tei
│       └── tele-xx.tei
├── wikimedia
│   ├── convert.py
│   └── raw
│       ├── en
│       │   └── wikimedia-v20210402.xml
│       ├── en-sl.tmp
│       └── sl
│           └── wikimedia-v20210402.xml
└── wikipedia
    ├── convert.py
    └── raw
        ├── en
        │   └── wiki0.sl-en.xml
        └── sl
            └── wiki0.sl-en.xml

```
