#PE 20

factorial = 1
for i in range(1,101):
    factorial *= i

digit_sum = 0
for num in range(len(str(factorial))):
    digit_sum += int(str(factorial)[num])

print(digit_sum)
