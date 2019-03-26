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
from functions import get_brightness


wattage = int(input("Lightbulb wattage (w): "))
brightness = get_brightness(wattage)

if brightness == -1:
    print("Invalid wattage")
else:
    print("Brightness: {:d} lumens".format(brightness))