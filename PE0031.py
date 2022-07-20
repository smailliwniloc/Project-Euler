#PE 31

coins = [1,2,5,10,20,50,100,200]

totals = [[] for i in range(201)]

for j in range(len(totals)):
    for k in range(len(coins)):
        if coins[k] == 1:
            totals[j].append(1)
        elif coins[k] > j:
            totals[j].append(totals[j][k-1])
        else:
            totals[j].append(totals[j][k-1] + totals[j-coins[k]][k])

print(totals[200])
