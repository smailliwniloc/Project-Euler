#PE 7
primes = []
for x in range(2, 1000000):
    composite = 0
    for i in range(2, int(x**.5)+1):
        if x%i == 0:
            composite = 1
        else:
            continue
    if composite == 0:
        primes.append(x)
print(primes[10000])
