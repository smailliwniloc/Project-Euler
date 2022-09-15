#PE 85

from xmlrpc.client import MAXINT


def numRects(n, m):
    count = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            count += i*j

    return count

minDiff = MAXINT
bestProd = 0
bestN = 0
bestM = 0

for m in range(100):
    for n in range(100):
        newDiff = abs(2000000 - numRects(n, m))
        if(newDiff < minDiff):
            minDiff = newDiff
            bestProd = m*n
            bestN = n
            bestM = m

print(bestProd, bestN, bestM, abs(2000000 - numRects(bestN, bestM)))