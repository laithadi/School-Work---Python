'''
[program description]

Author: Laith Adi 

ID: 170265190

Email: Adix5190@mylaurier.ca

__updated__ = "2018-10-18"

'''
n = int(input('Enter a number: '))
print()
count = n - 1
num_of_tags = -2
for x in range(0, n):
    count -= 1
    num_of_tags += 2
    for y in range(0, n + 1):
        if y <= count:
            print(' ', end="")
    for z in range(0, num_of_tags + 1):
        print('#', end="")

    print()
