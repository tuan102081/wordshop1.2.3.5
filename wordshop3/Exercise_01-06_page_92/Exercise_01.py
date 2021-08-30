"""
Author: Nguyen Duy Tuan
Date: 30/08/2021
Program: Exercise_01-06_page_92.py
Problem:
    Translate the following for loops to equivalent while loops:
        a.  for count in range(100):
                print(count)
        b.  for count in range(1, 101):
                print(count)
        c.  for count in range(100, 0, -1):
                print(count)

Solution:

"""
# a)
count = 0
while 0 <= count < 100:
    print(count)
    count += 1
# b)
count = 1
while 0 < count < 101:
    print(count)
    count += 1
# c)
count = 100
while 0 < count <= 100:
    print(count)
    count -= 1
