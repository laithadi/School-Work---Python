'''
[program description]

Author: Laith Adi 

ID: 170265190

Email: Adix5190@mylaurier.ca

__updated__ = "2018-10-17"

'''

# Imports
from random import randint

# number of correct answers
correct_answers = 0
# total questions asked
total_questions_asked = 0

# infinite loop since it breaks when the user says no
while correct_answers >= 0:
    # the first random number
    number = randint(0, 1000)
    # the second random number
    number_2 = randint(0, 1000)
    # variable for the correct number
    answer = number + number_2
    print('\t'  '{:>6}'.format(number))
    print('\t' '+{:>5}'.format(number_2))
    # this is where the user will input their attempt
    your_answer = int(input('\t=  '))
    # add up questions asked
    total_questions_asked += 1
    # correct answer
    if your_answer == answer:
        print('Congratulations!')
        # adding up correct answers
        correct_answers += 1
    # wrong answer
    else:
        print('Sorry, the correct answer is {}'.format(answer))
    print('')
    # ask if the user wants to keep playing
    continue_playing = str(input('Continue (Y/N): '))
    print('')
    # they dont want to play
    if continue_playing == 'N':
        # display score
        print('Your final score is {}/{}'.format(correct_answers, total_questions_asked))
        break
