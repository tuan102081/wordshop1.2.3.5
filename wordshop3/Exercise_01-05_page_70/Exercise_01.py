"""
Author: Nguyen Duy Tuan
Date: 30/08/2021
Program: Exercise_01-05_page_70.py
Problem:
Write the outputs of the following loops:
    a. for count in range(5):
        print(count + 1, end = " ")
    b. for count in range(1, 4):
        print(count, end = " ")
    c. for count in range(1, 6, 2):
        print(count, end = " ")
    d. for count in range(6, 1, –1):
        print(count, end = " ")

Solution:
    Display:
        1 2 3 4 5
        1 2 3
        1 3 5
        6 5 4 3 2
"""
for count in range(5):
    print(count + 1, end=" ")
print()
for count in range(1, 4):
    print(count, end=" ")
print()
for count in range(1, 6, 2):
    print(count, end=" ")
print()
for count in range(6, 1, -1):
    print(count, end=" ")



