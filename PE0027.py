#PE 27

import sympy

def f(a,b,n):
    return (n**2 + a*n + b)

max_a = 0
max_b = 0
max_chain = 0
for a in range(-500,500):
    for b in sympy.sieve.primerange(2,1000):
        chain = 0
        for n in range(0,b):
            if sympy.isprime(f((2*a)+1,b,n)):
                chain += 1
            else:
                if chain > max_chain:
                    max_a = (2*a)+1
                    max_b = b
                    max_chain = chain
                break
print("a = ",max_a, "b = ", max_b, "chain = ",max_chain)
print(max_a*max_b)
