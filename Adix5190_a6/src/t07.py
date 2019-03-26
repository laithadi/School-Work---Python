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
from functions import hours_required
from functions import paint_cost
from functions import paint_required
from functions import wall_area


print("Enter paint and labour standards:")

standard_area = int(input("Standard wall area (sq ft / gallon): "))
area_per_hour = int(input("Area painted per hour (sq ft / hour): "))
labour = int(input("Labour charges ($ / hour): "))
print()

print("Enter customer information:")

cost = int(input("Cost of paint (1 gallon): $"))
height = int(input("Height of wall (ft): "))
width = int(input("Width of wall (ft): "))

area = wall_area(width, height)
total = paint_required(area, standard_area)
hours = hours_required(area, area_per_hour)
pc = paint_cost(total, cost)
labour = labour * hours
total_cost = pc + labour
print()

print("Paint required: {:d}".format(total))
print("Hours labour required: {:d} hours".format(hours))
print("Paint cost:  $    {:.2f}".format(pc))
print("Labour cost: $    {:.2f}".format(labour))
print("             ----------")
print("Total cost:  $   {:.2f}".format(total_cost))
