#PE 22
f = open("PE0022_names.txt")
a = f.read()

names = a.split(",")
for i in range(len(names)):
    names[i] = names[i][1:-1]

names = sorted(names)

nums = []
for i in range(len(names)):
    let_sum = 0
    for letter in names[i]:
        let_sum += ord(letter)-64
    nums.append(let_sum)

answer = 0
for j in range(len(nums)):
    answer += nums[j]*(j+1)

print(answer)
