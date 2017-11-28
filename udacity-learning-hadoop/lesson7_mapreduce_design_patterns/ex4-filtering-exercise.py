#!/usr/bin/python
import sys
import csv
import re

# To run this code on the actual data, please download the additional dataset.
# You can find instructions in the course materials (wiki) and in the instructor notes.
# There are some things in this data file that are different from what you saw
# in Lesson 3. The dataset is more complicated and closer to what you might
# see in the real world. It was generated by exporting data from a SQL database.
#
# The data in at least one of the fields (the body field) can include newline
# characters, and all the fields are enclosed in double quotes. Therefore, we
# will need to process the data file in a way other than using split(","). To do this,
# we have provided sample code for using the csv module of Python. Each 'line'
# will be a list that contains each field in sequential order.
#
# In this exercise, we are interested in the field 'body' (which is the 5th field,
# line[4]). The objective is to count the number of forum nodes where 'body' either
# contains none of the three punctuation marks: period ('.'), exclamation point ('!'),
# question mark ('?'), or else 'body' contains exactly one such punctuation mark as the
# last character. There is no need to parse the HTML inside 'body'. Also, do not pay
# special attention to newline characters.

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    p = re.compile("[\\?\\.\\!]")
    for line in reader:

        # YOUR CODE HERE
        body = line[4]
        if not p.search(body[:-1]):
            writer.writerow(line)



test_text = """\"\"\t\"\"\t\"\"\t\"\"\t\"This is one sentence\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"Also one sentence!\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"Hey!\nTwo sentences!\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"One. Two! Three?\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"One Period. Two Sentences\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"Three\nlines, one sentence\n\"\t\"\"
"""

# This function allows you to test the mapper with the provided test string
def main():
    import StringIO
    sys.stdin = StringIO.StringIO(test_text)
    mapper()
    sys.stdin = sys.__stdin__

if __name__ == "__main__":
    main()
