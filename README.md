TODO
====
[ ] Move readme to udacity folder. This readme should be generic
[ ] Code review the examples and

Useful
======
Links to have in mind:
- Resource Manager: http://localhost:50070
- JobTracker: http://localhost:8088/
- Node Specific Info: http://localhost:8042/


Datasets
========
Download and unzip data sets from:
- http://content.udacity-data.com/courses/ud617/access_log.gz
- http://content.udacity-data.com/courses/ud617/purchases.txt.gz


Running a map reduce job with Hadoop Streaming:
```
hadoop jar /usr/local/Cellar/hadoop/2.8.2/libexec/share/hadoop/tools/lib/hadoop-streaming-2.8.2.jar -mapper ./ex7-mapper-invertedIndex.py --reducer ./ex7-reducer-invertedIndex.py -file ./ex7-mapper-invertedIndex.py -file ./ex7-reducer-invertedIndex.py -input nodes -output output1
```
