'''
[program description]

Author: Laith Adi 

ID: 170265190

Email: Adix5190@mylaurier.ca

__updated__ = "2018-11-16"

'''
from functions import is_valid_isbn
isbn = input('Enter an ISBN to test:')
valid = is_valid_isbn(isbn)
if valid:
    print('Valid ISBN')
else:
    print('Invalid ISBN')
