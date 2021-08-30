"""
Author: Nguyen Duy Tuan
Date: 31/08/2021
Program: Exercise_06.py
Problem:
    Write a loop that replaces each number in a list named data with its absolute value.
Solution:
    display:
        Absolute :
            [40, 58, -69, -84, 51, 76, -12, 36]  =  40
            Absolute :
            [40, 58, -69, -84, 51, 76, -12, 36]  =  58
            Absolute :
            [40, 58, 69, -84, 51, 76, -12, 36]  =  69
            Absolute :
            [40, 58, 69, 84, 51, 76, -12, 36]  =  84
            Absolute :
            [40, 58, 69, 84, 51, 76, -12, 36]  =  51
            Absolute :
            [40, 58, 69, 84, 51, 76, -12, 36]  =  76
            Absolute :
            [40, 58, 69, 84, 51, 76, 12, 36]  =  12
            Absolute :
            [40, 58, 69, 84, 51, 76, 12, 36]  =  36


"""

values = [-40, 58, -69, -84, 51, 76, -12, 36]

for index, value in enumerate(values):
    values[index] = abs(value)
    print("Absolute : ")
    print(values, " = ", abs(value))



