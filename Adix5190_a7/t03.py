'''
[program description]

Author: Laith Adi 

ID: 170265190

Email: Adix5190@mylaurier.ca

__updated__ = "2018-11-16"

'''
from functions import my_find
s = input('String to search:')
r = input('String to search for:')
i = my_find(s, r)
print("'{}' is found at location {} in '{}'".format(r, i, s))
