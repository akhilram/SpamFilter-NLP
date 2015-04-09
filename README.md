# Spam Filter

## Description
A Spam filter, that classifies electronic mails using Naive Bayes approach with add-one smoothing.
Features used: Bag of words with associated probabilities

## Running instructions
The filter can be used ad-hoc with the model provided (spam.nb) or it can be retrained with new data.

### 1. Ad-hoc classification
Classification can be done using the following command

python3 nbclassify.py modelfile testfile

The modelfile in this case is spam.nb
The testfile has to be formatted in such a way that each line corresponds to a single batch of text that needs to be classified.

### 2. Retraining and classification
Retraining is to be done in two phases: Data formatting and Model generation

#### Data formatting 
In this stage the individual text files to be used for training are aggregated to one single training file.
Follow the naming convension for naming files. 
SPAM# for files whose contents are spam and HAM# for other files.
Put all such files into a seperate folder along with parsetraining.py and run using the following command

python3 parsetraining.py spam

#### Model generation
The data formatting phase generates a training file spam_training.txt and this file is used to train the model. The training 
is done with the following command

python3 nblearn.py trainingfile modelfile

Model generation phase can also be associated with an evaluation step using a heldout development set, which measures the performance of the model.
The command is as follows

python3 nbclassify.py modelfile devfile eval

This will generate a text file evaluation.txt that contain the evaluation report