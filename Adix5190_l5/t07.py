'''
[program description]

Author: Laith Adi 

ID: 170265190

Email: Adix5190@mylaurier.ca

__updated__ = "2018-10-18"

'''
num = int(input('Enter number of bottles: '))

for x in range(num, 1, -1):
    if x != 1:
        print('''
{} bottles of beer on the wall, {} bottles of beer.
Take one down, pass it around, {} bottles of beer on the wall.'''.format(x, x, x - 1))
# changig the range, helps with reducing the if statement within the for loop
print('')
print('''1 bottle of beer on the wall, 1 bottle of beer.
Take one down, pass it around, no more bottles of beer on the wall!
        ''')
# Imports

# Constants
