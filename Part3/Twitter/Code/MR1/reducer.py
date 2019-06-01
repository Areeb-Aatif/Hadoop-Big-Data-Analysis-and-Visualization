#!/usr/bin/env python
"""reducer1.py"""

from operator import itemgetter
import sys

current_url = None
text = None
previous_url = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    if '\t' in line:
        current_url, text = line.split('\t', 1)
    else:
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    # removing duplicate tweets
    if current_url != previous_url:
        if current_url:
            print '%s\t%s' % (current_url, text)
        previous_url = current_url