'''
[program description]

Author: Laith Adi 

ID: 170265190

Email: Adix5190@mylaurier.ca

__updated__ = "2018-10-16"

'''
import math

current_population = int(input('Current population: '))
growth_rate = int(input('Growth Rate (%): '))
target_population = int(input('Target Population: '))
years = math.ceil(math.log(target_population /
                           current_population) / math.log(1 + (growth_rate / 100)))
while (current_population >= 0 and growth_rate > 0 and target_population > 0):
    print('\nIt will take {} year(s) to reach the target population.'.format(years))
    break
