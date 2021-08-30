"""
Author: Nguyen Duy Tuan
Date: 31/08/2021
Program: Exercise_05.py
Problem:
    Assume that data refers to a list of numbers, and result refers to an empty list.
Write a loop that adds the nonzero values in data to the result list, keeping them
in their relative positions and excluding the zeros.
Solution:
    display:


"""
list = [1, -4, 5, -8]
result = []
index = 0

while index < len(list):
    list[index] = abs(list[index])
    index += 1
    result.append(list)

print(result)
