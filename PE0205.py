# PE 205

from random import random


def d(sides):
    return int(random()*sides) + 1

def roll(num, sides):
    ans = 0
    for _ in range(num):
        ans += d(sides)
    return ans

