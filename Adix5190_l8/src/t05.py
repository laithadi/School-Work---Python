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
from functions import get_lotto_numbers

n = int(input('Number of values: '))
low = int(input('Low Value: '))
high = int(input('High Value: '))

numbers = get_lotto_numbers(n, low, high)

print()
print('Lotto numbers', numbers)
