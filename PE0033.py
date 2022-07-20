#PE 33

import math

good_nums = []
for i in range(10,100):
    if "0" not in str(i):
        good_nums.append(i)

winners = []
for n in good_nums:
    big_nums = [m for m in good_nums if m > n]
    shared_digit1 = []
    shared_digit2 = []
    for m in big_nums:
        if str(n)[0] in str(m):
            shared_digit1.append(m)
        elif str(n)[1] in str(m):
            shared_digit2.append(m)
        else:
            continue
    for k in shared_digit1:
        if int(str(n)[1])/int(str(k).replace(str(n)[0],"",1)) == n/k:
            winners.append("{}/{}".format(n,k))
    for k in shared_digit2:
        if int(str(n)[0])/int(str(k).replace(str(n)[1],"",1)) == n/k:
            winners.append("{}/{}".format(n,k))

numerator = 1
denominator = 1
for num in winners:
    numerator *= int(num[:2])
    denominator *= int(num[3:])

print(denominator/math.gcd(numerator,denominator))
