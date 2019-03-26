'''
[program description]

Author: Laith Adi 

ID: 170265190

Email: Adix5190@mylaurier.ca

__updated__ = "2018-10-18"

'''
num = int(input('Enter the number of values: '))
print()
value = float(input('First value: '))
min = value
max = value
total = value
average = value
for x in range(0, num - 1):
    value = float(input('Next value: '))
    if value < min:
        min = value
    if value > max:
        max = value
    total += value

print('''
Minimum: {}
Maximum: {}
Total: {}
Average: {}
'''.format(min, max, total, total / num))
