"""
Author: Nguyen Duy Tuan
Date: 29/08/2021
Program: project_06_page_62.py
Problem:
    The kinetic energy of a moving object is given by the formula KE = (1/2)mv^2
    where m is the object’s mass and v is its velocity. Modify the program you created
    in Project 5 so that it prints the object’s kinetic energy as well as its momentum.


Solution:
    Display:
        Mass: 20
        Velocity: 7
        The object's momentum is 140.0
        The object's kinetic energy is 490.0

"""
mass = float(input("Mass: "))
velocity = float(input("Velocity: "))
KE = 0.5 * mass * velocity**2
momentum = mass * velocity
print("The object's momentum is "+str(momentum))
print("The object's kinetic energy is "+str(KE))
