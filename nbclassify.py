import sys
import re

model = open(sys.argv[1], 'r', encoding = 'utf-8', errors = 'ignore')
train = open(sys.argv[2], 'r', encoding = 'utf-8', errors = 'ignore')

startindex = 0

if sys.argv[1]=='spam.nb':
    output = open('spam.out', 'w', encoding = 'utf-8', errors = 'ignore')
else:
    output = open('sentiment.out', 'w', encoding = 'utf-8', errors = 'ignore')

if sys.argv.__len__() == 4:
    startindex = 1
    error = open('error.txt', 'w')
    evaluation = open('evaluation.txt', 'w')

classes = []
total = 0
Dict = {}
p_class = []

eval = []

for i in range(0,46):
    eval += (0,0,0),

count = int(model.readline())
for i in range(0,count):
    line = model.readline()
    words = line.split()
    classes.append((words[0],words[1],words[2]))
    total += int(words[1])
    p_class.append(1)

vcount = int(model.readline())
line = model.readline()
while line:
    words = line.split()
    # words = (re.split('\*| |&|\||>|<|\(|\)|\.|\,|{|}|-|!|~|#|\$|\^|%|:|;|\+|=|\?|/|"|`', line))
    tup = ()
    for i in range(1,words.__len__()):
        new = (str(words[i]),)
        tup = tup + new
    try:
        Dict[words[0]] = tup
    except IndexError:
        line = model.readline()
        continue
    line = model.readline()
ocount = 0

line = train.readline()
while line:
    words = line.split()
    # words = (re.split('\*| |&|\||>|<|\(|\)|\.|\,|{|}|-|!|~|#|\$|\^|%|:|;|\+|=|\?|/|"|`', line))
    for i in range(0,count):
        p_class[i] = 1
    for w in words[startindex : words.__len__()]:

        w = w.lstrip('\'')
        if w.__len__() == 0:
            continue
        norm = False
        if(Dict.get(w)):
            for i in range(0, count):
                try:
                    p_w = int(Dict[w][i])
                except ValueError:
                    p_w = 0
                except IndexError:
                    p_w = 0
                p_c = int(classes[i][2])
                if not p_w == 0:
                    word_p = p_w/p_c
                    p_class[i] *= word_p
                    if p_class[i] < 1e-100:
                        norm = True
                else:
                    word_p = (p_w+1)/(int(classes[i][2])+vcount)
                    p_class[i] *= word_p
                    if p_class[i] < 1e-100:
                        norm = True
                if p_class[i] == 0 or word_p == 0:
                    print(w)
            if norm:
                norm = False
                for j in range(0,count):
                    p_class[j] *= 1e100
        else:
            ocount += 1
            for i in range(0, count):
                word_p = 1/(int(classes[i][2])+vcount)
                p_class[i] *= word_p
                if p_class[i] < 1e-100:
                    norm = True
            if norm:
                norm = False
                for j in range(0,count):
                    p_class[j] *= 1e100
    max = 0.0
    index = -1
    for i in range(0,count):
        p_class[i] = p_class[i]*(int(classes[i][1])/total)
        if p_class[i] > float(max):
            max = p_class[i]
            index = i
#for internal testing
    if sys.argv.__len__() == 4:
        try:
            if words[0][0] == classes[index][0][0]:
                eval[index] = (eval[index][0]+1, eval[index][1], eval[index][2])
        except:
            print('eror')
        if not words[0][0] == classes[index][0][0]:
            error.write(words[0] + '\n')
        try:
            eval[index] = (eval[index][0], eval[index][1]+1, eval[index][2])
        except:
            print('get')
        for p in range(0,count):
            if classes[p][0][0] == words[0][0]:
                break
        eval[p] = (eval[p][0], eval[p][1], eval[p][2]+1)
#####################
    output.write(classes[index][0] + '\n')
    print(classes[index][0])
    line = train.readline()


#for internal quality analysis
if sys.argv.__len__() == 4:
    for i in range(0,count):
        p = float(eval[i][0])/float(eval[i][1])
        r = float(eval[i][0])/float(eval[i][2])
        evaluation.write(classes[i][0] + ' precision ' + str(eval[i][0]) + '/' + str(eval[i][1]) + ' = ' + str(p) + '\n')
        evaluation.write(classes[i][0] + ' recall ' + str(eval[i][0]) + '/' + str(eval[i][2]) + ' = ' + str(r) + '\n')
        evaluation.write(classes[i][0] + ' F-score = ' + str((2*p*r)/(p+r)) + '\n')


