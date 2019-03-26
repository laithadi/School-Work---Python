'''
[program description]

Author: Laith Adi 

ID: 170265190

Email: Adix5190@mylaurier.ca

__updated__ = "2018-11-02"

'''
start = int(input("Starting value for table: "))
end = int(input("Ending value for table: "))

print()

val = 0

print("      ", end="")

for i in range(start, end + 1):
    print("{:>5d}".format(i), end="")

print()

print("       ", end="")

for i in range(start, end + 1):
    print("-----", end="")

print()

for i in range(start, end + 1):
    print("{:>4d}".format(i), end=" |")
    for j in range(start, end + 1):
        val = j * i
        print("{:>5d}".format(val), end="")
    print()