#!/usr/bin/env python

import sys

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

sales_for_each_day_of_the_week = [0] * 7
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 2:
        weekday, sales = data
        weekday = int(weekday)
        sales_for_each_day_of_the_week[weekday] += float(sales)

for weekday, sales_total in enumerate(sales_for_each_day_of_the_week):
    print "{0}\t{1}".format(weekdays[weekday], sales_total)
