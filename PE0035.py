#PE 35

import sympy

total = 0
for k in range(2,1000000):
    circulars = []
    for i in range(len(str(k))):
        num = str(k)[i:] + str(k)[:i]
        circulars.append(int(num))
    flag = 1
    for j in circulars:
        if sympy.isprime(j):
            continue
        else:
            flag = 0
    if flag == 1:
        total += 1

print(total)
