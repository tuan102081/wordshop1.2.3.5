"""
Author: Nguyen Duy Tuan
Date: 27/08/2021
Program: Project_06_page33.py
Problem:
    Write and test a program that computes the area of a circle. This program should
    request a number representing a radius as input from the user. It should use the formula
    3.14 * radius ** 2 to compute the area and then output this result suitably labeled.
Solution:
"""

radius = float(input("Enter with radius = "))
area =3.14 * radius ** 2
print("This is area", area, "circle units.")