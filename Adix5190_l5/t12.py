'''
[program description]

Author: Laith Adi 

ID: 170265190

Email: Adix5190@mylaurier.ca

__updated__ = "2018-10-18"

'''
n = int(input('Enter a number: '))

print()

spaces = -1
for x in range(0, n):
    spaces += 1
    for y in range(0, spaces + 1):
        if x == n - 1:
            print('#', end="")
        else:
            if y == 0:
                print('#', end="")
            elif y == spaces:
                print('#', end="")
            else:
                print(' ', end="")
    print()
