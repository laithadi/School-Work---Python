"""
-----------------------------------------------------
CP104 - Assignment 6
-----------------------------------------------------
Author: Laith Adi
ID: 170265190
Email: adix5190@mylaurier.ca
__updated__ = "2018-11-09"
-----------------------------------------------------
"""
from functions import time_values

seconds = int(input("Number of seconds: "))
print()

print("{:d} seconds is the same as:".format(seconds))
days, hours, minutes = time_values(seconds)
print("  {:d} days".format(days))
print("  {:d} days".format(hours))
print("  {:d} days".format(minutes))