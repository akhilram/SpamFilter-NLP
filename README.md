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