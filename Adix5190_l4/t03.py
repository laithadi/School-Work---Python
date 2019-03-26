'''
Lab 4, Task 3

Author: Laith Adi & Ashwin Balaje

ID: 170265190 & 180790110

Email: Adix5190@mylaurier.ca & bala0110@mylaurier.ca

__updated__ = "2018-10-04"

'''

import math

target_num = int(input("Enter target number: "))
n = 0
nearest_pow = 0

while nearest_pow < target_num:
    n += 1
    nearest_pow = int(math.pow(2, n))

print()
print("The nearest power of 2 >= 248 is {}.".format(nearest_pow))
