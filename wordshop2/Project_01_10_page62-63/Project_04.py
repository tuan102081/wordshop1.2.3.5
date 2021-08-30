"""
Author: Nguyen Duy Tuan
Date: 29/08/2021
Program: project_04_page_62.py
Problem:
    Write a program that takes the radius of a sphere (a floating-point number) as
    input and then outputs the sphere’s diameter, circumference, surface area, and volume.

Solution:
    Display result:
        Radius = 7
        Diameter:  14.0
        Circumference:  43.982297150257104
        Surface area :  615.7521601035994
        Volume : 1436.7550402417319

"""
import math
radius = float(input("Radius = "))
diameter = radius * 2
circumference = diameter * math.pi
surfaceArea = math.pi * pow(diameter, 2)
volume = 4/3 * math.pi * pow(radius, 3)
print("Diameter: ", diameter)
print("Circumference: ", circumference)
print("Surface area : ", surfaceArea)
print("Volume : ", volume)
