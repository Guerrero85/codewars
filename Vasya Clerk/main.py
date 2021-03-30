'''
The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a huge line. Each of them has a single 100, 50 or 25 dollar bill. An "Avengers" ticket costs 25 dollars.

Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.

Can Vasya sell a ticket to every person and give change if he initially has no money and sells the tickets strictly in the order people queue?

Return YES, if Vasya can sell a ticket to every person and give change with the bills he has at hand at that moment. Otherwise return NO.
Examples:

tickets([25, 25, 50]) # => YES 
tickets([25, 100]) # => NO. Vasya will not have enough money to give change to 100 dollars
tickets([25, 25, 50, 50, 100]) # => NO. Vasya will not have the right bills to give 75 dollars of change (you can't make two bills of 25 from one of 50)

'''
def tickets(people):
    cashier = {100:0,50:0,25:0}
    for pay in people:
        if pay == 25:
            cashier[25] += 1
        elif pay == 50:
            if cashier[25] == 0:
                return 'NO'
            cashier[50] += 1
            cashier[25] -= 1
        else:
            cashier[100] += 1
            if cashier[50] >= 1 and cashier[25] >= 1:
                cashier[50] -= 1
                cashier[25] -= 1
            elif cashier[25] >= 3:
                cashier[25] -= 3
            else:
                return 'NO'
    return 'YES'


print(tickets([25,25,25,100,25,50]))   
