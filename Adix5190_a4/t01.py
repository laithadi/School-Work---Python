'''
[program description]

Author: Laith Adi 

ID: 170265190

Email: Adix5190@mylaurier.ca

__updated__ = "2018-10-09"

'''
# hot days (temperatures 28 or higher)
# pleasant days (temperatures 18 - 27)
# cold days (temperatures 17 or lower)
hot_days = 0
pleasant_days = 0
cold_days = 0
day = 0
temperature = 0
temp = 0
while temperature != -500:
    temperature = int(input('Temperature C (-500 to stop): '))
    if temperature == -500:
        break
    elif temperature >= 28:
        hot_days += 1
        temp += temperature
    elif 18 < temperature < 27:
        pleasant_days += 1
        temp += temperature
    elif temperature <= 17:
        cold_days += 1
        temp += temperature


average_temp = (temp // (cold_days + pleasant_days + hot_days))

print('')

print('Cold days:            {}'.format(cold_days))
print('Pleasent days:        {}'.format(pleasant_days))
print('Hot days:             {}'.format(hot_days))
print('Average:              {} C'.format(average_temp))
