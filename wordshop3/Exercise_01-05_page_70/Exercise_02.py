"""
Author: Nguyen Duy Tuan
Date: 30/08/2021
Program: Exercise_01-05_page_70.py
Problem:
    Write a loop that prints your name 100 times. Each output should begin on a
new line.

Solution:
    Display:
        Pom(1)
        ...
        ...
        Pom(100)

"""
name = "Pom"
for i in range(100):
    print(name, "(" + str(i + 1) + ")")

