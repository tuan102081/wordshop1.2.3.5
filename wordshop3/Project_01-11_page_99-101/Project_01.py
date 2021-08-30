"""
Author: Nguyen Duy Tuan
Date: 30/08/2021
Program: Project_01.py
Problem:
        Write a program that accepts the lengths of three sides of a triangle as inputs.
        The program output should indicate whether or not the triangle is an equilateral triangle.

Solution:
    Display result:
        Enter the lengths of three sides of a triangle:
        Edge A = 7
        Edge B = 6
        Edge C = 6
        Not an equilateral triangle


"""
print("Enter the lengths of three sides of a triangle: ")
a = int(input("Edge A = "))
b = int(input("Edge B = "))
c = int(input("Edge C = "))

if a + b > c and b + c > a and a + c > b:
    if a == b == c:
        print("Is an equilateral triangle")
    else:
        print("Not an equilateral triangle")
else:
    print("Not a triangle")

