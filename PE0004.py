#PE 4
palindromes = []
for i in range(100,1000):
    for j in range (100, 1000):
        product = str(i*j)
        if product == product[::-1]:
            palindromes.append(int(product))
palindromes.sort()
print(palindromes[-1])
