#PE 34

def fact(n):
    product = 1
    for k in range(2,n+1):
        product *= k
    return product

winners = 0
for k in range(10,100000):
    num = 0
    for digit in range(len(str(k))):
        num += fact(int(str(k)[digit]))
    if num == k:
        winners += k

print(winners)
