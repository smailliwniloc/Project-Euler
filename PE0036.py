#PE 36

palindromes = []
for num in range(1,1000000):
    if num == int(str(num)[::-1]) and str(bin(num))[2:] == str(bin(num))[2:][::-1]:
        palindromes.append(num)

total = 0
for j in palindromes:
    total += j

print(total)
