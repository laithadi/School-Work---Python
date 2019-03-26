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
from functions import fraction_product

num1 = int(input("Enter numerator of fraction 1: "))
den1 = int(input("Enter denominator of fraction 1: "))
num2 = int(input("Enter numerator of fraction 2: "))
den2 = int(input("Enter denominator of fraction 2: "))

num, den, product = fraction_product(num1, den1, num2, den2)
print()
print("Product = {:d}/{:d}".format(num, den))
print("Decimal = {:.2f}".format(product))
