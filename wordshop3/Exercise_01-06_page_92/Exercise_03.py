"""
Author: Nguyen Duy Tuan
Date: 30/08/2021
Program: Exercise_01-06_page_92.py
Problem:
    The log 2 of a given number N is given by M in the equation N 5 M2 . Using integer arithmetic,
    the value of M is approximately equal to the number of times N can be evenly divided by 2 until
    it becomes 0. Write a loop that computes this approximation of the log 2 of a given number N.
    You can check your code by importing the math.log function and evaluating the expression
    round(math.log(N, 2)) (note that the math.log function returns a floating-point value).

Solution:
    Display:
        The log 2 of a given number 8 = 3
        3.0

"""
import math

N = 8
x = 0
while 0 <= x <= N:
    if (2 ** x) == N:
        print("The log 2 of a given number", N, "=", x)
    x += 1
print(math.log2(N))




