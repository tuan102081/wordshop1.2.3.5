"""
Author: Nguyen Duy Tuan
Date: 30/08/2021
Program: Exercise_01-04_page_72.py
Problem:
    Write a code segment that displays the values of the integers x, y, and z on a single
    line, such that each value is right-justified with a field width of 6.

Solution:
    Display:
        1      2      3
"""
x, y, z = 1, 2, 3
print("%-6d %-6d %-6d" % (x, y, z))

