'''
[program description]

Author: Laith Adi 

ID: 170265190

Email: Adix5190@mylaurier.ca

__updated__ = "2018-10-18"

'''
n = int(input('Enter a number: '))
print()
count = n
for x in range(0, n):
    count -= 1
    # practice same for loops like the second part
    for y in range(1, n + 1, 1):
        if y <= count:
            print(' ', end="")
        else:
            print('#', end="")
    print()


for x in range(0, n):
    count += 1
    for y in range(1, x + 1, 1):
        print(' ', end="")
    # order of the numbers in range can be switched with the negative/positive
    # sign for the increment changes
    for y in range(n - x, 0, -1):
        print('#', end="")
    print()
