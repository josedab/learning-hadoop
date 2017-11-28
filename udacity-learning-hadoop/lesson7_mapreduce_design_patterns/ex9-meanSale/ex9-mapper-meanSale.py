#!/usr/bin/python

import sys
from datetime import datetime

for line in sys.stdin:
    data = line.strip().split("\t")

    day = datetime.strptime(data[0], "%Y-%m-%d").weekday()
    saleValue = data[4]

    print "{0}\t{1}".format(day, saleValue)
