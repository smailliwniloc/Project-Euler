# PE 205

from random import random


def d(sides):
    return int(random()*sides) + 1

def roll(num, sides):
    ans = 0
    for _ in range(num):
        ans += d(sides)
    return ans

wins = 0
totalRolls = 0
maxRolls = 10000
for i in range(maxRolls):
    colin = roll(6, 6)
    pete = roll(9, 4)
    if(pete > colin):
        wins += 1
    totalRolls += 1
    print(wins/totalRolls)