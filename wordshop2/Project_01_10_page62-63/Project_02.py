"""
Author: Nguyen Duy Tuan
Date: 29/08/2021
Program: project_02_page_62.py
Problem:
    You can calculate the surface area of a cube if you know the length of an edge.
    Write a program that takes the length of an edge (an integer) as input and prints
    the cube’s surface area as output.

Solution:
    Display result:
        Enter the length of an edge = 2
        Cube’s surface area =  24

"""
a = int(input("Enter the length of an edge = "))
area = 6 * pow(a, 2)
print("Cube’s surface area = ", area)

