'''
[program description]

Author: Laith Adi 

ID: 170265190

Email: Adix5190@mylaurier.ca

__updated__ = "2018-10-18"

'''
num = int(input('Number of IAs: '))
print()
sum = 0
for x in range(1, 7):
    print('Week', x)
    for y in range(1, num + 1):
        sum += float(input('    Marking hours for IA {}: '.format(y)))

print()
print('Total marking hours for all IAs: {:.1f}'.format(sum))
