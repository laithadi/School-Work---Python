'''
[program description]

Author: Laith Adi 

ID: 170265190

Email: Adix5190@mylaurier.ca

__updated__ = "2018-10-18"

'''
num = int(input('Number of servers: '))
print()
sum = 0
for x in range(1, 8):
    print('Day', x)
    for y in range(1, num + 1):
        sum += float(input('    Tips for server {}: '.format(y)))

print('')
print('Tips per server: ${:.2f}'.format(sum / num))
