"""
Author: Nguyen Duy Tuan
Date: 31/08/2021
Program: Exercise_02.py
Problem:
    Assume that the variable data refers to the list [5, 3, 7]. Write the expressions
    that perform the following tasks:
    a. Replace the value at position 0 in data with that value’s negation.
    b. Add the value 10 to the end of data.
    c. Insert the value 22 at position 2 in data.
    d. Remove the value at position 1 in data.
    e. Add the values in the list newData to the end of data.
    f. Locate the index of the value 7 in data, safely.
    g. Sort the values in data.
Solution:
    display:
        a. [-5, 3, 7]
        b. [-5, 3, 7, 10]
        c. [-5, 3, 22, 7, 10]
        d. [-5, 22, 7, 10]
        e. [-5, 22, 7, 10, 2, 0, 8]
        f. 2
        g. [-5, 0, 2, 7, 8, 10, 22]

"""
data = [5, 3, 7]

data[0] = -data[0]
print("a.", data)

data.append(10)
print("b.", data)

data.insert(2, 22)
print("c.", data)

del data[1]
print("d.", data)

newData = [2, 0, 8]
data.extend(newData)
print("e.", data)

index = data.index(7)
print('f.', index)

data.sort()
print("g.", data)






