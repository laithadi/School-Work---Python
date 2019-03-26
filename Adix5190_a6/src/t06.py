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
from functions import time_split


initial_seconds = int(input("Number of seconds: "))
days, hours, minutes, seconds = time_split(initial_seconds)
print()

print("Days: {:d}, Hours: {:d}, Minutes: {:d}, Seconds: {:d}".format(
    days, hours, minutes, seconds))
