'''
[program description]

Author: Laith Adi 

ID: 170265190

Email: Adix5190@mylaurier.ca

__updated__ = "2018-10-18"

'''
start = int(input('Enter start: '))
end = int(input('Enter end: '))
increment = int(input('Enter increment: '))
sum = 0
for x in range(start, end + 1, increment):
    sum += x
print('Total of {} to {} increment {}: {}'.format(start, end, increment, sum))
