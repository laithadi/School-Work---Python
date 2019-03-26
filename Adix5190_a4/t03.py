'''
[program description]

Author: Laith Adi 

ID: 170265190

Email: Adix5190@mylaurier.ca

__updated__ = "2018-10-14"

'''
# the amount i am cannot exceed with candy
moms_limit = int(input("Mom's limit on the number of candies: "))
print('')
# candy collected from the first house
first_house = int(input('Candies from the first household: '))
# adding up all candies together
total_candy = 0 + first_house

while first_house != moms_limit:
    # i changed the spelling from 'candes' to 'candies' assuming that it was a
    # typo in the task
    second_house = int(input('Candies from the next household: '))
    total_candy += second_house
    if total_candy >= moms_limit:
        break

print('')
# candy that exceed moms limit
extra_candy = total_candy - moms_limit

print("You gathered {} candies in total. \nYou have {} candies over Mom's limit.".format(
    total_candy, extra_candy))
