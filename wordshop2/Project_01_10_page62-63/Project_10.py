"""
Author: Nguyen Duy Tuan
Date: 29/08/2021
Program: project_10_page_63.py
Problem:
    An employee’s total weekly pay equals the hourly wage multiplied by the total number of regular hours plus any
    overtime pay. Overtime pay equals the total overtime hours multiplied by 1.5 times the hourly wage. Write a
    program that takes as inputs the hourly wage, total regular hours, and total overtime hours and
    displays an employee’s total weekly pay.

Solution:
    Display:
        What is your hourly wage?: 18000
        How many regular hours did you work this week?: 123
        How many overtime hours did you have this week?: 23
        Your total weekly pay is:  126000.0

"""
hourWage = float(input("What is your hourly wage?: "))
regularHours = float(input("How many regular hours did you work this week?: "))
overtimeHours = float(input("How many overtime hours did you have this week?: "))
overtimeWage = (1.5 * hourWage)
totalWeeklyPay = (hourWage * regularHours) + (overtimeHours * overtimeWage)
print("Your total weekly pay is: ", totalWeeklyPay)



