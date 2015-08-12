#parses test files to the required input format for the classifier
import os
from os import walk
import sys

path = os.getcwd()
Files = []

# choose appropriate output file
if sys.argv[1]=='spam':
    output = open('spam_test.txt', 'w', encoding= 'utf-8', errors='ignore')
else:
    output = open('sentiment_test.txt','w', encoding= 'utf-8', errors='ignore')

for (dirpath, dirnames, filenames) in walk(path):
    Files.extend(filenames)
    break

# append files to a single file
for f in Files:
    outline = ''
    if f.endswith('~') or f.endswith('.nb') or f.endswith('test.txt') or f=='parsetest.py':
        continue
#for internal testing
    if sys.argv.__len__() == 3:
        if f[0] == 'H':
            output.write('HAM ')
        if f[0] == 'S':
            output.write('SPAM ')
        if f[0] == 'P':
            output.write('POS ')
        if f[0] == 'N':
            output.write('NEG ')
#####################
    input = open(str(f),encoding='utf-8', errors='ignore')
    line = input.readline()
    while line:
        output.write(str.rstrip(line) + ' ')
        line = input.readline()
    output.write('\n')
    input.close()

output.close()
