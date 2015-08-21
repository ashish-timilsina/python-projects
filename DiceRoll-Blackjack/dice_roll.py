__author__ = 'Ashish'

import random



#dice roll that gets a random number between 1 & 6 inclusive
def dice_roll():
    return random.randint(1,6)

#two players roll the dice to reach the goal of 21
def dice_game():
    playerOneTotal = 0
    playerTwoTotal = 0

    while (playerOneTotal & playerTwoTotal) <21:
        roll1 = dice_roll()
        roll2 = dice_roll()
        playerOneTotal = playerOneTotal + roll1
        playerTwoTotal = playerTwoTotal + roll2


    if playerOneTotal == 21:
        print("Player One got 21. Player One WINS!")

    elif playerTwoTotal == 21:
        print("Player Two got 21. Player Two WINS!")

    elif (playerOneTotal & playerTwoTotal) == 21:
        print("draw")

    else:
        print("Both players have exceeded total of 21. Player 1 got %d and player 2 got %d" % (playerOneTotal, playerTwoTotal))

        exit()

dice_game()


