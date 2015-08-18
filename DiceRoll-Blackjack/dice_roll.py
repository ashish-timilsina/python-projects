__author__ = 'Ashish'


import random

def dice_roll():
    number = 0

    while number <21:
        roll = int(random.randint(1,6))
        print("dice roll: "+str(roll))
        number = number + roll
    if number == 21:
        print("you've won!!")
    else:
        print("you've exceeded total of 18")
        exit()
    print("total: "+str(number))

dice_roll()
