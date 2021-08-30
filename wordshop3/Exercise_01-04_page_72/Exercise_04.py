"""
Author: Nguyen Duy Tuan
Date: 30/08/2021
Program: Exercise_01-04_page_72.py
Problem:
    Write a loop that outputs the numbers in a list named salaries. The outputs should be formatted
        in a column that is right-justified, with a field width of 12 and a precision of 2.

Solution:
    Display
        1.00
        2.00
        3.00
        4.00
        5.00
"""
salaries = [1, 2, 3, 4, 5]
for i in salaries:
    print("%12.2f" % i)


