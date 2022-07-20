#PE 37

import sympy

total = 0
n = 10
answer = 0
while total < 11:
    flag = 0
    for i in range(len(str(n))):
        if sympy.isprime(int(str(n)[i:])) and sympy.isprime(int(str(n)[:len(str(n))-i])):
            continue
        else:
            flag = 1
    if flag == 0:
        total += 1
        answer += n
        print(n)
    n += 1

print(answer)
