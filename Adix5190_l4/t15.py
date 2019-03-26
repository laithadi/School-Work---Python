'''
Lab 4, Task 15

Author: Laith Adi & Ashwin Balaje

ID: 170265190 & 180790110

Email: Adix5190@mylaurier.ca & bala0110@mylaurier.ca

__updated__ = "2018-10-04"

'''

value = float(input('Enter first value: '))
maximum = 0
minimum = 0
total = 0
num_values = 0

while value != 0:
    if value > maximum:
        maximum = value
    if value < minimum:
        minimum = value
    total += value
    num_values += 1
    value = float(input('Enter next value: '))

average_num = total / num_values
print()
print('Minimum: {:.2f}'.format(minimum))
print('Maximum: {:.2f}'.format(maximum))
print('Total: {:.2f}'.format(total))
print('Average: {:.2f}'.format(average_num))
