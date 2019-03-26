'''
[program description]

Author: Laith Adi 

ID: 170265190

Email: Adix5190@mylaurier.ca

__updated__ = "2018-11-02"

'''
n = int(input("Number of values: "))

negg = 0
zero = 0
poss = 0
even = 0
odd = 0
total = 0
minn = 0
maxx = 0

print()

for i in range(0, n):
    if i == 0:
        value = int(input("First Value: "))
        minn = value
        maxx = value
    else:
        value = int(input("Next Value: "))

    total = total + value

    if maxx < value:
        maxx = value
    if minn > value:
        minn = value
    if value < 0:
        negg += 1
    elif value > 0:
        poss += 1
    else:
        zero += 1
    if value % 2 == 0:
        even += 1
    else:
        odd += 1

avg = total / n

print()

print('Negative Values: {:>5d}'.format(negg))
print('Zero Values: {:>9d}'.format(zero))
print('Positive Values: {:>5d}'.format(poss))
print('Even Values: {:>9d}'.format(even))
print('Odd Values: {:>10d}'.format(odd))
print('Total: {:>15d}'.format(total))
print('Minimum: {:>13d}'.format(minn))
print('Maximum: {:>13d}'.format(maxx))
print('Average: {:>16.2f}'.format(avg))
