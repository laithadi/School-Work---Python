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
from functions import payment

principal = float(input("Amount borrowed : $"))
interest = float(input("Interest rate: "))
interest = interest / 100
months = int(input("Length of loan (months): "))

monthly_payment = payment(principal, interest, months)
print("The monthly payment is ${:.2f}.".format(monthly_payment))
