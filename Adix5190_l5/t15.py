'''
[program description]

Author: Laith Adi 

ID: 170265190

Email: Adix5190@mylaurier.ca

__updated__ = "2018-10-18"

'''
min_base = int(input('Enter minimum value of base: '))
max_base = int(input('Enter maximum value of base: '))
increment_base = int(input('Enter increment in base value: '))
min_height = int(input('Enter minimum value of height: '))
max_height = int(input('Enter maximum value of height: '))
increment_height = int(input('Enter increment in height value: '))

print('''
              Cross-Sectional  Moment of  Section
Base  Height  Area             Inertia    Modulus
''')

for x in range(min_base, max_base + 1, increment_base):
    for y in range(min_height, max_height + 1, increment_height):
        print('{}  x  {} {:12.2f} {:16.2f} {:12.2f}'
              .format(x, y, (x * y), (x * (y**3) / 12), (x * (y**2) / 6)))
