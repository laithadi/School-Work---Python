'''
[program description]

Author: Laith Adi 

ID: 170265190

Email: Adix5190@mylaurier.ca

__updated__ = "2018-10-18"

'''
num = int(input('Enter n: '))
sum_1 = 0
for x in range(1, num + 1):
    sum_1 += (1 / x)

print('The sum of the series 1 to 1/{} is: {}'.format(num, sum_1))
