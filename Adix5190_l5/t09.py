'''
[program description]

Author: Laith Adi 

ID: 170265190

Email: Adix5190@mylaurier.ca

__updated__ = "2018-10-18"

'''
gic_value = float(input('Enter the GIC purchase value: $'))
years = int(input('Enter the number of years invested: '))
rate = float(input('Enter the GIC interest rate (%): '))

print('''
Year       Value $
------------------
''')
for x in range(0, years + 1):
    print('{:2d}      {:,.2f}'.format(x, gic_value))
    gic_value += (rate / 100) * gic_value
