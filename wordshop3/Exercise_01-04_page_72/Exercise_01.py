"""
Author: Nguyen Duy Tuan
Date: 30/08/2021
Program: Exercise_01-04_page_72.py
Problem:
    Assume that the variable amount refers to 24.325. Write the outputs of the following statements:
        a. print("Your salary is $%0.2f" % amount)
        b. print("The area is %0.1f" % amount)
        c. print("%7f" % amount)

Solution:
    Display:
        Your salary is $ 24.32
        The area is 24.3
        24.325000

"""
amount = 24.325

print("Your salary is $ " + ("%0.2f" % amount))

print("The area is " + ("%0.1f" % amount))

print("%7f" % amount)

