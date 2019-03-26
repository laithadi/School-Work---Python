'''
[program description]

Author: Laith Adi 

ID: 170265190

Email: Adix5190@mylaurier.ca

__updated__ = "2018-10-16"

'''

# minimum percent
SPEND_ATLEAST = 90 / 100

# get budget and set minimum amount
party_budget = float(input('Party budget: $'))
min_amount = party_budget * SPEND_ATLEAST
# setting initial money left to spend
amount_left = party_budget
total_money_spent = 0

while party_budget > 0:
    # get price of item
    cost_item = float(input('Cost of item: $'))
    # total amount spent
    total_money_spent += cost_item
    # if there is not enough funds
    if cost_item > amount_left:
        print('Item costs too much: ${:.2f} remaining in budget'.format(
            amount_left))
        # remove the expensive item that cannot be afforded
        total_money_spent -= cost_item
    # if there is enough money and the user want to buy again
    else:
        amount_left -= cost_item
    # no more funds
    if amount_left == 0:
        print('There is no more funds available in the set budget')
        break
    else:
        pass
    # make request to buy more
    buy_again = str(input('Buy another item (Y/N): '))
    # did not reach acceptable spending amount
    if total_money_spent < min_amount and buy_again == "N":
        print(
            'Have not yet spent the minimum amount: ${:.2f}'.format(min_amount))
    elif buy_again == 'N' and total_money_spent > min_amount:
        break
    else:
        pass

# print total amount spent
print('\nTotal spent on items: ${:.2f}'.format(total_money_spent))
# print the amount remaining
print('Amount remaining: ${:.2f}'.format(amount_left))
