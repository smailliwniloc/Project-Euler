#PE 84

import random
import matplotlib.pyplot as plt

gameFreq = [[x, 0] for x in range(40)] # number of times landed on each square x
totalMoves = 0

commChest = [2, 17, 33]
chance = [7, 22, 36]

diceSize = 4
diceDistribution = [diceSize - abs(diceSize + 1 - x) for x in range(2, 2*diceSize + 1)]

commChestCards = [x for x in range(1, 17)]
chanceCards = [x for x in range(1, 17)]

commChestDrawnOrder = []
chanceDrawnOrder = []

def handleCommChest(pos):
    if(len(commChestCards) > 0):
        i = random.randint(1, len(commChestCards))
        idx = commChestCards[i-1]
        commChestCards.remove(idx)
    else:
        idx = commChestDrawnOrder.pop(0)

    commChestDrawnOrder.append(idx)
    
    if(idx == 1):
        return 0
    if(idx == 2):
        return 10
    return pos

def handleChance(pos):
    if(len(chanceCards) > 0):
        i = random.randint(1, len(chanceCards))
        idx = chanceCards[i-1]
        chanceCards.remove(idx)
    else:
        idx = chanceDrawnOrder.pop(0)

    chanceDrawnOrder.append(idx)
    
    if(idx == 1):
        return 0
    if(idx == 2):
        return 10
    if(idx == 3):
        return 11
    if(idx == 4):
        return 24
    if(idx == 5):
        return 39
    if(idx == 6):
        return 5
    if(idx == 7 or idx == 8):
        if(pos == 7):
            return 15
        if(pos == 22):
            return 25
        if(pos == 36):
            return 5
    if(idx == 9):
        if(pos == 7 or pos == 36):
            return 12
        if(pos == 22):
            return 28
    if(idx == 10):
        return pos - 3

    return pos



currPos = 0
doublesInARow = 0
for _ in range(10000000):
    d1 = random.randint(1, 4)
    d2 = random.randint(1, 4)
    if(d1 == d2):
        doublesInARow += 1
    else:
        doublesInARow = 0
    if(doublesInARow == 3):
        currPos = 10
        doublesInARow = 0
        totalMoves += 1
    else:
        roll = d1 + d2
        totalMoves += 1
        currPos += roll
        currPos %= 40
    if(currPos == 30):
        currPos = 10
    if(currPos in commChest):
        currPos = handleCommChest(currPos)
    if(currPos in chance):
        currPos = handleChance(currPos)
    gameFreq[currPos][1] += 1




x = [x for x in range(40)]
y = [gameFreq[x][1]/totalMoves for x in range(40)]

plt.bar(x, y)
plt.show()