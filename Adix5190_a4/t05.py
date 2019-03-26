'''
[program description]

Author: Laith Adi 

ID: 170265190

Email: Adix5190@mylaurier.ca

__updated__ = "2018-10-14"

'''
# Seniors
SENIOR_AGE = 65
SENIOR_PRICE = 4.0
# Adults
ADULT_AGE = 18
ADULT_PRICE = 5.0
# CHILDREN
INFANT_AGE = 3
INFANT_PRICE = 0
# Students
STUDENT_AGE_LO = 10
STUDENT_AGE_HI = 15
STUDENT_PRICE = 1.0
# kids pricing
KID_PRICE = 2.0

# must define variables in loop
ticket_price = 0
total_price = 0
# is there a ticket being purchased
purchase_ticket = str(input('Purchase a ticket (Y/N)? '))

# if the customer says YES to buying a ticket
while purchase_ticket == 'Y':
    # the age of the buyer
    age = float(input('How old are you? '))
    # adult ages
    if SENIOR_AGE >= age >= ADULT_AGE:
        # cost of one ticket for an adult
        ticket_price = ADULT_PRICE
        # total price of tickets
        total_price += ticket_price
        print('That ticket costs ${:.2f}'.format(ADULT_PRICE))
    # senior ages
    elif age >= SENIOR_AGE:
        # cost of one ticket for a senior
        ticket_price = SENIOR_PRICE
        # total price of tickets
        total_price += ticket_price
        print('That ticket costs ${:.2f}'.format())
    # kids and student ages
    elif INFANT_AGE <= age < ADULT_AGE:
        if STUDENT_AGE_LO <= age <= STUDENT_AGE_HI:
            # asking if they are a student
            student = str(input('Are you a student at this school? (Y/N): '))
            # student ages
            if student == 'Y':
                # cost per ticket
                ticket_price = STUDENT_PRICE
                # total cost of tickets
                total_price += ticket_price
                print('That ticket costs ${:.2f}'.format(STUDENT_PRICE))
            else:
                # cost of a ticket for kids
                ticket_price = KID_PRICE
                # total cost of tickets
                total_price += ticket_price
                print('That ticket costs ${:.2f}'.format(KID_PRICE))
        # kids age
        else:
            # cost of a ticket for kids
            ticket_price = KID_PRICE
            # total cost of tickets
            total_price += ticket_price
            print('That ticket costs ${:.2f}'.format(KID_PRICE))
    # children under 3
    else:
        ticket_price = 0
        total_price += ticket_price
    # ask the customer if he/she wants to buy another ticket
    purchase_another_ticket = str(input('Purchase another ticket (Y/N)? '))
    if purchase_another_ticket == 'N':
        break

# if the customer does not want to buy tickets
while purchase_ticket == 'N':
    break

print('\nTotal tickets price: ${:.2f}'.format(total_price))
