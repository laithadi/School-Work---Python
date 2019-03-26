'''
[program description]

Author: Laith Adi 

ID: 170265190

Email: Adix5190@mylaurier.ca

__updated__ = "2018-11-16"

'''
from functions import my_isdigit
s = input('Enter a string to test:')
digits = my_isdigit(s)
if digits:
    print('The string is all digits')
else:
    print('The string contains non-digits')
