'''
[program description]

Author: Laith Adi 

ID: 170265190

Email: Adix5190@mylaurier.ca

__updated__ = "2018-10-18"

'''

n = int(input('Enter n: '))
sum = 0
for x in range(0, n + 1):
    if x % 2 != 0:
        sum += x
print('The sum of all odd numbers from 1 to {} is: {}'.format(n, sum))
# Constants
