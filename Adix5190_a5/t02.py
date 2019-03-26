'''
[program description]

Author: Laith Adi 

ID: 170265190

Email: Adix5190@mylaurier.ca

__updated__ = "2018-11-02"

'''
width = int(input("Width of diamond: "))
char = str(input("Printing character: "))

print()


if width % 2 == 0:
    for i in range(2, width, 2):
        print(" " * ((width - i) // 2), end="")
        print(char * i)
else:
    for i in range(1, width, 2):
        print(" " * ((width - i) // 2), end="")
        print(char * i)


for i in range(width, 0, -2):
    for j in range((width - i) // 2):
        print(" ", end="")
    for j in range(i):
        print(char, end="")
    print()