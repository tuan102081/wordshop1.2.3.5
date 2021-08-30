"""
Author: Nguyen Duy Tuan
Date: 29/08/2021
Program: project_03_page_62.py
Problem:
    Five Star Retro Video rents VHS tapes and DVDs to the same connoisseurs who like to buy LP record
    albums. The store rents new videos for $3.00 a night, and oldies for $2.00 a night. Write a program
    that the clerks at Five Star Retro Video can use to calculate the total charge for a customer’s video
    rentals. The program should prompt the user for the number of each type of video and output the total cost.

Solution:
    Display:
        Please enter the number of your new : 5
        Please enter the number of your oldies: 3
        The total cost is $21

"""
import math
a = int(input("Please enter the number of your new : "))
b = int(input("Please enter the number of your oldies: "))
videos = a * 3
oldies = b * 2
print(f'The total cost is ${videos + oldies}')

