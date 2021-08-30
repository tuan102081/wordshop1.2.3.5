"""
Author: Nguyen Duy Tuan
Date: 30/08/2021
Program: Exercise_01-09_page_85.py
Problem:
    Construct truth tables for the following Boolean expressions:
        a.  not (A or B)
        b.  not A and not B

Solution:
    Display:
                A                 B  !A or !B       !A and !B
                3                 5     False           False

"""
a = 3
b = 5
print("%18s%18s%10s%16s" % ("A", "B", "!A or !B", "!A and !B"))
print("%18s%18s%10s%16s" % (a, b, not (a or b), not a and not b))





