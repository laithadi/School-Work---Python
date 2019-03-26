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
from functions import get_total_change

n = int(input("Enter number of nickels: "))
d = int(input("Enter number of dimes: "))
q = int(input("Enter number of quarters: "))
l = int(input("Enter number of loonies: "))
t = int(input("Enter number of toonies: "))

tv = get_total_change(n, d, q, l, t)
print("Total: ${:.2f}".format(tv))