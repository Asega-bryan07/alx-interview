#!/usr/bin/python3
'''
Example:
x = 3, nums = [4, 5, 1]
First round: 4
Maria picks 2 and removes 2, 4, leaving 1, 3
Ben picks 3 and removes 3, leaving 1
Ben wins because there are no prime numbers left for Maria
to choose
Second round: 5
Maria picks 2 and removes 2, 4, leaving 1, 3, 5
Ben picks 3 and removes 3, leaving 1, 5
Maria picks 5 and removes 5, leaving 1
Maria wins because there are no prime numbers left for Ben
to choose
Third round: 1
Ben wins because there are no prime numbers for Maria to choose
'''


def isWinner(x, nums):
    '''
    Return: name of the player that won the most rounds
    '''
    if not nums or x < 1:
        return None
    max_num = max(nums)

    my_filter = [True for _ in range(max(max_num + 1, 2))]
    for i in range(2, int(pow(max_num, 0.5)) + 1):
        if not my_filter[i]:
            continue
        for j in range(i * i, max_num + 1, i):
            my_filter[j] = False
            y = 0
            for i in range(len(my_filter)):
                if my_filter[i]:
                    y += 1
                my_filter[i] = y
            player_1 = 0
            for x in nums:
                player_1 += my_filter[x] % 2 == 1
            if player_1 * 2 == len(nums):
                return None
            if player_1 * 2 > len(nums):
                return "Maria"
            return "Ben"
