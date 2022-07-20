#PE 3
factors = []
for i in range(1, int(600851475143**0.5)+1):
    if 600851475143%i == 0:
        factors.append(i)

print(factors)
prime_factors = []
for num in factors:
    composite = 0
    for i in range(2, int(num**.5)+1):
        if num%i == 0:
            composite = 1
            break
        else:
            continue
    if composite == 0:
        prime_factors.append(num)

print(prime_factors)
