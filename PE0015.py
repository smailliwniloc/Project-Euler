#PE 15
def choose(n,r):
    n_fact = 1
    for i in range(1,n+1):
        n_fact *= i
    r_fact = 1
    for j in range(1, r+1):
        r_fact *= j
    n_min_r_fact = 1
    for k in range(1, n-r+1):
        n_min_r_fact *= k
    print((n_fact)/(r_fact*n_min_r_fact))

choose(40,20)
