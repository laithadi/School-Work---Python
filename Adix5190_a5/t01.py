'''
[program description]

Author: Laith Adi 

ID: 170265190

Email: Adix5190@mylaurier.ca

__updated__ = "2018-11-02"

'''
penny_weight = 1.5552

print("Pennyweight to grams Conversion")
start = int(input("Start: "))
limit = int(input("Limit: "))
increment = int(input("Increment: "))

pennys = 0
grams = 0
counter = 0

pen = ("Pennyweight")
gram = ("Grams")
line = ("-----------")
line2 = ("---------")
print("")
print("{:>11}{:>10}".format(pen, gram))
print("{:>11}{:>10}".format(line, line2))
for i in range(start, limit + 1, increment):
    pennys = start + (increment * counter)
    counter += 1
    grams = pennys * penny_weight
    print("{:>11d}{:>10.4f}".format(pennys, grams))