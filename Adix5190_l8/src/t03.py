"""
------------------------------------------------------------------------
Lab 8
------------------------------------------------------------------------
Author: Laith Adi 
ID:     170265190
Email:  Adix5190@mylaurier.ca
__updated__ = "2018-11-15"
------------------------------------------------------------------------
"""
from functions import get_digit_name

print('These are the digit names from 1-9')
for i in range(1, 10):
    name = get_digit_name(i)
    print(name)
