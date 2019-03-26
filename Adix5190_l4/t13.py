'''
Lab 4, Task 13

Author: Laith Adi & Ashwin Balaje

ID: 170265190 & 180790110

Email: Adix5190@mylaurier.ca & bala0110@mylaurier.ca

__updated__ = "2018-10-04"

'''

fac_int = int(input('Enter an integer: '))
n = fac_int
answer = 1

print('{}! = '.format(n), end='')
while n > 1:
    answer *= n
    print("{} * ".format(n), end="")
    n -= 1

print("1 = {}".format(answer))