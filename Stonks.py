from random import randint, seed
from datetime import datetime

dice1 = [1, 1, 6, 6, 8, 8]
dice2 = [2, 2, 4, 4, 9, 9]

seed(datetime.now())


def count_wins(dice1, dice2):
    assert len(dice1) == 6 and len(dice2) == 6
    dice1_wins, dice2_wins = 0, 0

    num_rounds = 10 ** 5

    assert len(dice1) == 6 and len(dice2) == 6

    num_dice1_wins = 0
    num_dice2_wins = 0

    for _ in range(num_rounds):
        dice1_result = dice1[randint(0, 5)]
        dice2_result = dice2[randint(0, 5)]

        if dice1_result > dice2_result:
            num_dice1_wins += 1
        elif dice2_result > dice1_result:
            num_dice2_wins += 1
        print(num_dice1_wins)

    if num_dice1_wins > num_dice2_wins:
        print("The dice {} is better than {}:\nout of {} rounds it won {} times more".format(dice1, dice2, num_rounds,
                                                                                             num_dice1_wins - num_dice2_wins))
    elif num_dice2_wins > num_dice1_wins:
        print("The dice {} is better than {}:\nout of {} rounds it won {} times more".format(dice2, dice1, num_rounds,
                                                                                             num_dice2_wins - num_dice1_wins))
    else:
        print("A tie")
    # write your code here
    print(num_dice1_wins)

    return (dice1_wins, dice2_wins)


count_wins(dice1, dice2)