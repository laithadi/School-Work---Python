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
from functions import generate_integer_list, list_categorize

n = int(input('Enter number of elements in list: '))
low = int(input('Enter lowest value range for list: '))
high = int(input('Enter highest value range for list: '))
values = generate_integer_list(n, low, high)
print()
print('Values:', values)

negatives, positives, zeroes, evens, odds = list_categorize(values)

print()
print('Negatives:', negatives)
print('Positives:', positives)
print('Zeroes:', zeroes)
print('Evens:', evens)
print('Odds', odds)
