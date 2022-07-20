#PE 28

diagonals = [1]

n = 1
while n < 501:
    for i in range(1,5):
        diagonals.append(diagonals[-1]+2*n)
    n += 1

print(sum(diagonals))
