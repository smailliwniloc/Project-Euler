#PE 14
count_max = 0
num = 2
dic = {}
for n in range(2,1000001):
    count = 1
    while n != 1:
        if n%2 == 0:
            n = n/2
            count += 1
        else:
            n = 3*n + 1
            count += 1
    dic[count] = num
    num += 1
    if count > count_max:
        count_max = count

print(dic[count_max])
