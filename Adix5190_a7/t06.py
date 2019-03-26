'''
[program description]

Author: Laith Adi 

ID: 170265190

Email: Adix5190@mylaurier.ca

__updated__ = "2018-11-16"

'''
from functions import number_convert
number = input('Enter phone number:')
digits = number_convert(number)
print('Digits:{}'.format(digits))
