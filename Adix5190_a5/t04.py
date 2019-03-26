'''
[program description]

Author: Laith Adi 

ID: 170265190

Email: Adix5190@mylaurier.ca

__updated__ = "2018-11-02"

'''
yrs_rainfall = int(input("Number of years of rainfall: "))
print()

print("Enter rainfall in cm.")

months = 12 * yrs_rainfall
total = 0

for i in range(1, yrs_rainfall + 1):
    print("Year ", i)
    for j in range(1, 13):
        rain = float(input("    Month {}: ".format(j)))
        total += rain

avg = total / months

print()
print("Number of months: {:d}".format(months))
print("Total rainfall: {:.1f} cm".format(total))
print("Average rainfall per month: {:.1f} cm".format(avg))
