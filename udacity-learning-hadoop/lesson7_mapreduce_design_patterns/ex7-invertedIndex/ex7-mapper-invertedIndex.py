#!/usr/bin/python

import sys
import csv
import re

regexp = re.compile(r'\W+')
for line in sys.stdin:
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)


    for line in reader:
        words = regexp.split(line[4].lower())
        for word in words:
            writer.writerow([word, line[0]])
