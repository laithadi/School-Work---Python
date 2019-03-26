'''
[program description]

Author: Laith Adi 

ID: 170265190

Email: Adix5190@mylaurier.ca

__updated__ = "2018-11-16"

'''
from functions import my_isalpha
s = input('Enter a string to test:')
alpha = my_isalpha(s)
if alpha:
    print('The string is all letters')
else:
    print('The string contains non-letters')
