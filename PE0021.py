#PE 21

dict = {}

def divisor_sum(n):
    divisors = [1]
    for i in range(2,int(n**.5)+1):
        if n%i == 0:
            if i/1 == n/i:
                divisors.append(i)
            else:
                divisors.append(i)
                divisors.append(n/i)
    num_sum = 0
    for num in divisors:
        num_sum += num
    dict[n] = num_sum

size = 10000

for i in range(size):
    divisor_sum(i)

for k in range(size):
    if dict[k] > size:
        dict[dict[k]] = 0

amicables = []
for j in dict:
    if dict[dict[j]] == j and dict[j] != j:
        amicables.append(j)

total = 0
for num in amicables:
    total += num

print(total)
