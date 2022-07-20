#PE 23

dict = {}
def divisor_sum(n):
    divisors = [1]
    for i in range(2,int(n**.5)+1):
        if n%i == 0:
            if float(i) == n/i:
                divisors.append(i)
            else:
                divisors.append(i)
                divisors.append(n/i)
    num_sum = 0
    for num in divisors:
        num_sum += num
    dict[n] = num_sum

for i in range(1,28124):
    divisor_sum(i)

abundants = []
for i in dict:
    if dict[i] > i:
        abundants.append(i)

answer = 0
for i in range(28124):
    has_sum = False
    for j in abundants:
        if j < i:
            if i - j in abundants:
                has_sum = True
                break
        else:
            break
    if not has_sum:
        answer += i

print(answer)
