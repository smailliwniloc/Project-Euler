#PE 30

answer = 0
for num in range(10,295245):
    test = 0
    for i in range(len(str(num))):
        test += int(str(num)[i])**5
    if test == num:
        print(num)
        answer += num

print(answer)
