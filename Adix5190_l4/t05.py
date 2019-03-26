'''
Lab 4, Task 5

Author: Laith Adi & Ashwin Balaje

ID: 170265190 & 180790110

Email: Adix5190@mylaurier.ca & bala0110@mylaurier.ca

__updated__ = "2018-10-04"

'''

budget = int(input('Enter budget: $'))
day = 1
expense = 0
total_expense = 0

while day < 8:
    expense = int(input('Expenses for day {}: $'.format(day)))
    total_expense += expense
    day += 1

net_budget = budget - total_expense

print()
print('Expenses: ${:,.2f}'.format(total_expense))

if total_expense > budget:
    print('Deficit: ${:,.2f}'.format(net_budget))
elif total_expense < budget:
    print('Surplus: ${:,.2f}'.format(net_budget))
else:
    print('Balance: ${:,.2f}'.format(net_budget))
