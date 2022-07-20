#PE 40

total = 0
n = 1
string = ""
while total < 1000000:
    total += len(str(n))
    string += str(n)
    n += 1

answer = 1
for i in range(7):
    answer *= int(string[10**i-1])

print(answer)
