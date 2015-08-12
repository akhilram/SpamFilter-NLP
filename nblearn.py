#learns a naive bayes model from input data
import sys
import re

#initialize file pointers
train = open(sys.argv[1],'r', encoding = 'utf-8', errors = 'ignore')
model = open(sys.argv[2],'w', encoding = 'utf-8', errors = 'ignore')

#initialize vocabulary and model variables
classes = {}
Dict = {}
vocabulary = {}

line = train.readline()

#read the training file and update probability values
while line:
    words = line.split()
    if not classes.get(words[0]):
        classes[words[0]] = (0,0)
    classes[words[0]] = (classes[words[0]][0]+1, classes[words[0]][1]+words.__len__()-1)

    for word in words[1:words.__len__()]:
#stop words processing logic starts here

        word = word.lstrip('\'')
        word = word.rstrip('\'')
        word = word.lstrip()
        word = word.lower()

        if word.__len__() == 0:
            continue
#stop words processing logic ends here
        if not vocabulary.get(word):
            vocabulary[word] = 1

        if Dict.get((word,words[0])):
            Dict[(word,words[0])] += 1
        else:
            Dict[(word,words[0])] = 1
    line = train.readline()

model.write(str(classes.__len__())+'\n')

ClassSet = classes.keys()
for cls in ClassSet:
    model.write(cls + ' ' + str(classes[cls][0]) + ' ' + str(classes[cls][1]) + '\n')

#write into the model file
model.write(str(len(vocabulary))+'\n')
for word in vocabulary.keys():
    model.write(word + ' ')
    for cls in ClassSet:

        if Dict.get((word,cls)):
            model.write(str(Dict[(word,cls)]) + ' ')
        else:
            model.write('0 ')
    model.write('\n')

train.close()
model.close()