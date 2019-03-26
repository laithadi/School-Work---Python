'''
[program description]

Author: Laith Adi 

ID: 170265190

Email: Adix5190@mylaurier.ca

__updated__ = "2018-11-02"

'''
n = int(input("Number (>=1): "))

sum_a = 0

for i in range(1, n + 1):
    sum_a += 1 / (i**2)
print("Sum of inverse squares for {} = {}".format(n, sum_a))
