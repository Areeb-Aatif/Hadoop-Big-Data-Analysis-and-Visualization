#!/usr/bin/env python
"""mapper1.py"""

import sys
import re
import subprocess
from stemming.porter2 import stem

reload(sys)
sys.setdefaultencoding('utf8')

def removeUrl(text):
    return re.sub(r"http\S+", "", text)

def removePunctuation(text):
    punctuations = '''!()-|[]{};:'"=\,<>./?+@#$%^&*_~'''
    for w in text:
        if w in punctuations:
            text = text.replace(w, "")
    return text

def removeStopwords(text):
    filteredText = ''
    with open('english') as f:
        stopwords = f.read().splitlines()

    for w in text.split():
        if w not in stopwords:
            filteredText += w
            filteredText += ' '
    # print(stopwords)
    return filteredText

def stemWords(text):
    filteredText = ''
    for w in text.split():
        filteredText += stem(w)
        filteredText += ' '
    return filteredText

def removeNumbers(text):
    return re.sub("\d+", " ", text)

def removeEmojis(text):
    return text.encode('ascii', 'ignore').decode('ascii')

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    if not line:
        continue
    # split the line into columns
    columns = line.split(",", 1)
    if len(columns) < 2:
        continue

    # print line
    text = columns[1]
    # convert the text into all lowercase
    text = text.lower()
    # remove all URL's
    text = removeUrl(text)
    # remove punctuations from the text
    text = removePunctuation(text)
    # remove numbers from text
    text = removeNumbers(text)
    # remove emojis
    text = removeEmojis(text)
    # remove stopwords
    text = removeStopwords(text)
    # stem words
    text = stemWords(text)
    # remove stopwords
    text = removeStopwords(text)
    # write the results to STDOUT (standard output);
    print '%s\t%s' % (columns[0], text)
