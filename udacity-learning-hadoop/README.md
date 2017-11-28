
Overview
=====================

Solutions for Udacity course: Learning hadoop

These are exercises followed during the course. In some occasions, I took the liberty of adding extra things I considered useful for learning.

Development environment
==========================
For testing these scripts I have a pseudo-distributed hadoop environment.
Most of the work is



Resource Manager: http://localhost:50070
JobTracker: http://localhost:8088/
Node Specific Info: http://localhost:8042/


Datasets
Alternative - download data sets
Download and unzip data sets from:
http://content.udacity-data.com/courses/ud617/access_log.gz
http://content.udacity-data.com/courses/ud617/purchases.txt.gz


Running examples
===========================
- Download Datasets
- Upload to
Running a map reduce job with Hadoop Streaming:

hadoop jar /usr/local/Cellar/hadoop/2.8.2/libexec/share/hadoop/tools/lib/hadoop-streaming-2.8.2.jar --mapper ./ex7-mapper-invertedIndex.py --reducer ./ex7-reducer-invertedIndex.py -file ./ex7-mapper-invertedIndex.py -file ./ex7-reducer-invertedIndex.py -input nodes -output output1
