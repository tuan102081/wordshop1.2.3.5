"""
Author: Nguyen Duy Tuan
Date: 30/08/2021
Program: Project_02.py
Problem:
        Write a program that accepts the lengths of three sides of a triangle as inputs.
        The program output should indicate whether or not the triangle is a right triangle.
        Recall from the Pythagorean theorem that in a right triangle, the square of one side
        equals the sum of the squares of the other two sides.

Solution:
    Display result:
       Enter the lengths of three sides of a triangle:
        Edge A = 7
        Edge B = 6
        Edge C = 6
        Not a right triangle

"""
print("Enter the lengths of three sides of a triangle: ")
a = int(input("Edge A = "))
b = int(input("Edge B = "))
c = int(input("Edge C = "))
if a + b > c and b + c > a and a + c > b:
    if pow(a, 2) == pow(b, 2) + pow(c, 2) or pow(b, 2) == pow(a, 2) + pow(c, 2) or pow(c, 2) == pow(b, 2) + pow(a, 2):
        print("Is a right triangle")
    else:
        print("Not a right triangle")
else:
    print("Not a triangle")
