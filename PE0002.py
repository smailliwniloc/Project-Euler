#PE 2
fibonacci = [1,1]
while fibonacci[-1] < 4000000:
    fibonacci.append(fibonacci[-1]+fibonacci[-2])

print(fibonacci)

fib_sum = 0
for i in fibonacci:
    if i%2 == 0:
        fib_sum += i
print(fib_sum)
