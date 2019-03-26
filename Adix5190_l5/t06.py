'''
[program description]

Author: Laith Adi 

ID: 170265190

Email: Adix5190@mylaurier.ca

__updated__ = "2018-10-18"

'''
cals_per_minute = float(input('Enter calories burned per minute: '))
beg_min = int(input('Enter beginning number of minutes: '))
end_min = int(input('Enter ending number of minutes: '))
increment = int(input('Enter the increment in minutes: '))

print()

for x in range(beg_min, end_min + increment, increment):
    print('Calories burned after {} minutes: {}'.format(x, cals_per_minute * x))
