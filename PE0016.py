#PE 16
big_num = str(2**1000)
total = 0
for i in range(len(big_num)):
    total += int(big_num[i])
print(total)
