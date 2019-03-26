'''
[program description]

Author: Laith Adi 

ID: 170265190

Email: Adix5190@mylaurier.ca

__updated__ = "2018-10-18"

'''
age = int(input("Enter the worker's age: "))
salary = int(input("Enter the worker's salary: $"))
percent = float(input('Enter the yearly raise (%): '))

print('''
Age         Salary
------------------''')

for x in range(age, 66):
    print('{}        {:,.2f}'.format(x, salary))
    salary += (percent / 100) * salary
