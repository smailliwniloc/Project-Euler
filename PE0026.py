#PE 26

coprime_ten = [i for i in range(2,1001) if i%2 != 0 and i%5 != 0]

recurring = []
for j in coprime_ten:
    for k in range(1,j):
        if (10**k)%j == 1:
            recurring.append(k)
            break

print(coprime_ten[recurring.index(max(recurring))])
