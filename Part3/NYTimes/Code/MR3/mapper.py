#!/usr/bin/env python
"""mapper.py"""

import sys
import operator
from collections import OrderedDict

# input comes from STDIN (standard input)
for line in sys.stdin:
        
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into columns
    id, text = line.split('\t', 1)
    # split text into words
    words = text.split()

    with open("part2") as f:
        wordCount = f.read().splitlines()
    
    temp = {}
    tenWords = []
    for word in wordCount:
        word = word.strip()
        word, count = word.split("\t", 1)
        temp[word] = int(count)

    sortedTemp = OrderedDict(sorted(temp.items(), key=operator.itemgetter(1), reverse=True))
    sortedData = list(sortedTemp)[:10]

    # increase counters
    for word1 in words:
        if word1 not in sortedData:
                continue
        for word2 in words:
                if (word1 == word2) or (word2 not in sortedData):
                        continue
                # write the results to STDOUT (standard output);
                # what we output here will be the input for the
                # Reduce step, i.e. the input for reducer.py
                #
                # tab-delimited; the trivial word count is 1
                print '%s\t%s' % (word1+','+word2, 1)
        