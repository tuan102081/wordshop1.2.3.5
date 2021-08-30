"""
Author: Nguyen Duy Tuan
Date: 30/08/2021
Program: Exercise_01-09_page_85.py
Problem:
    Explain how to check for an invalid input number and prevent it being used in a program.
        You may assume that the user enters a number.
Set Case:
    A valid number is a number between 0 and 10 other than that it is invalid

Solution:
    Display:
        2 is Valid

"""
num = 2
if 0 < num <= 10:
    print(num, "is Valid")
else:
    print(num, "is Invalid")


