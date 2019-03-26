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
from functions import get_weekday_name

print('These are the weekdays')
for x in range(1, 8):
    name = get_weekday_name(x)
    print(name)
