#PE 41

import sympy

num = 7654321
while True:
    flag = 0
    for n in range(1, len(str(num))+1):
        if str(n) in str(num):
            continue
        else:
            flag = 1
            break
    if flag == 0:
        if sympy.isprime(num):
            print(num)
            break
    num -= 1
