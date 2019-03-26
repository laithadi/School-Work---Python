'''
Lab 4, Task 9

Author: Laith Adi & Ashwin Balaje

ID: 170265190 & 180790110

Email: Adix5190@mylaurier.ca & bala0110@mylaurier.ca

__updated__ = "2018-10-04"

'''

start_temp = int(input("Starting Celsius temperature: "))
end_temp = int(input("Ending Celsius temperature: "))
current_temp = start_temp

print()
print("Celsius Fahrenheit")
print("------------------")
while (current_temp <= end_temp):
    fahrenheit = int(9 / 5 * current_temp + 32)
    print("{:>7}{:>11}".format(current_temp, fahrenheit))
    current_temp += 1
