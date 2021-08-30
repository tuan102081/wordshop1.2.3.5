"""
Author: Nguyen Duy Tuan
Date: 31/08/2021
Program: Exercise_02.py
Problem:
    Assume that the variable data refers to the dictionary {'b':20, 'a':35}. Write the
values of the following expressions:
a. data['a']
b. data.get('c', None)
c. len(data)
d. data.keys()
e. data.values()
f. data.pop('b')
g. data # After the pop above
Solution:
    display:
        35
        None
        2
        dict_keys(['b', 'a'])
        dict_values([20, 35])
        20
        {'a': 35}

"""
data = {'b': 20, 'a': 35}
print(data['a'])
print(data.get('c', None))
print(len(data))
print(data.keys())
print(data.values())
print(data.pop('b'))
print(data)