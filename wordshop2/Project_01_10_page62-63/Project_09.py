"""
Author: Nguyen Duy Tuan
Date: 29/08/2021
Program: project_09_page_63.py
Problem:
    Write a program that takes as input a number of kilometers and prints the corresponding number of nautical miles.
    Use the following approximations:
    -   A kilometer represents 1/10,000 of the distance between the North Pole and the equator.
    -   There are 90 degrees, containing 60 minutes of arc each, between the North Pole and the equator.
    -   A nautical mile is 1 minute of an arc.

Solution:
    Enter the number of km: 156

    156.0 km = 233.28000000000003 nmi

"""
km = float(input("Enter the number of km: "))
nmi = 90 * 60 / 10000
swap = km * nmi

# print
print("\n" + str(km) + " km = " + str(swap) + " nmi")
