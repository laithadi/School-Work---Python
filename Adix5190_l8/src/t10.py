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
# Imports
from functions import generate_integer_list
from functions import min_search

# Constants

n = int(input('Enter number of elements in list: '))
low = int(input('Enter lowest value range for list: '))
high = int(input('Enter highest value range for list: '))
values = generate_integer_list(n, low, high)
print()
print('Values:', values)

indexes = min_search(values)
print('Indexes of minimums:', indexes)