The repository of the NLP course project.

To train a translation model on TC3 dataset, follow the steps bellow:

* Install OpenNMT-py using pip
* Put the TC3 train and test data into /data
* Use the scripts in /preprocess to clean and tokenize all the data
* Before each training run, use the shuffle script to shuffle the train data
* Use 'onmt_build_vocam -config training.yaml -n_sample -1' to build the vocabulary
* Use onmt_train -config training.yaml to start training
