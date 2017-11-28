#!/usr/bin/python

import sys
import csv

nodes = []
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for line in reader:
        word = line[0]
        nodeId = line[1]

        if word != oldKey:
            writer.writerow([oldKey, sorted(nodes)])
            nodes = []

        oldKey = word
        nodes.append(int(nodeId))

if oldKey != None:
    writer.writerow([oldKey, sorted(nodes)])
