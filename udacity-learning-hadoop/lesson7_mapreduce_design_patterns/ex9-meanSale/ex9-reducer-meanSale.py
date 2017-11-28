#!/usr/bin/python

import sys

oldDay = None
numSalesPerDay = 0
sumSales = 0

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for line in sys.stdin:
    data_mapped = line.strip().split("\t");
    if len(data_mapped) != 2:
        continue

    day = int(data_mapped[0])
    saleValue = float(data_mapped[1])

    if oldDay and oldDay != day:
        mean = sumSales / numSalesPerDay
        print "{0}\t{1}".format(weekdays[oldDay], mean)
        sumSales = 0
        numSalesPerDay = 0

    oldDay = day
    sumSales += saleValue
    numSalesPerDay += 1

if oldDay != None:
    mean = sumSales / numSalesPerDay
    print "{0}\t{1}".format(weekdays[oldDay], mean)
