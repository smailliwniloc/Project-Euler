#PE 12
factors = 0
num = 1
while factors < 500:
    factors = 0
    tri = int(num*(num+1)/2)
    if (int(tri**.5))**2 == tri:
        factors -= 1
    for i in range(1,int(tri**.5)+1):
        if tri%i == 0:
            factors += 2
    num += 1

print(tri)
