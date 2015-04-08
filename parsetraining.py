import os
from os import walk
import sys

path = os.getcwd()
Files = []

if sys.argv[1] == 'spam':
    output = open('spam_training.txt', 'w', encoding= 'utf-8', errors = 'ignore')
else:
    output = open('sentiment_training.txt', 'w', encoding= 'utf-8', errors = 'ignore')

for (dirpath,dirnames,filenames) in walk(path):
    Files.extend(filenames)
    break

for f in Files:
    outline = ''
    if f.endswith('~') or f.endswith('.nb') or f == 'spam_training.txt' or f == 'parsetraining.py' or f.endswith('training.txt'):
        print('gotcha')
        continue
    if(f[0] == 'S'):
        output.write('SPAM ')
    elif(f[0] == 'H'):
        output.write('HAM ')
    elif(f[0] == 'P'):
        output.write('POS ')
    elif(f[0] == 'N'):
        output.write('NEG ')
    input = open(str(f), 'r', encoding='utf-8', errors='ignore')
    line = input.readline()
    while line:
        output.write(str.rstrip(line) + ' ')
        line = input.readline()
    output.write('\n')    
    input.close()

output.close()

        
