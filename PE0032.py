#PE 32

good_nums = []
for n in range(1000,90000):
    flag = 0
    for num in range(len(str(n))):
        if str(n)[num] in str(n)[0:num] or str(n)[num] in str(n)[num+1:] or "0" in str(n):
            flag = 1
    if flag == 0:
        good_nums.append(n)

pandigitals = []
for n in good_nums:
    divisors = []
    for i in range(2,int(n**.5)+1):
        if n%i == 0:
            if i/1 == n/i:
                continue
            else:
                divisors.append(i)
    for d in divisors:
        string = "{}{}{}".format(d,int(n/d),n)
        if len(string) == 9 and "1" in string and "2" in string and "3" in string and "4" in string and "5" in string and "6" in string and "7" in string and "8" in string and "9" in string and n not in pandigitals:
            pandigitals.append(n)

answer = 0
for k in pandigitals:
    answer += k

print(answer)
