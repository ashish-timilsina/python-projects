__author__ = 'Ashish'


import random


def dice_roll():
    number = 0
    while number <21:
        roll = int(random.randint(1,6))
        print("dice roll: "+str(roll))
        number = number + roll

    if number == 21:
        print("you've won with total of: "+str(number))
    else:
        print("you've exceeded total of 21. Total is: "+str(number) )
        exit()



dice_roll()
