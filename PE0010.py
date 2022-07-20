#PE 10
prime_sum = 0
for x in range(2, 2000000):
    composite = 0
    for i in range(2, int(x**.5)+1):
        if x%i == 0:
            composite = 1
        else:
            continue
    if composite == 0:
        prime_sum += x
print(prime_sum)
