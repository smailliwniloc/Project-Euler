#PE 43


nums = [1,0,2,3,4,5,6,7,8,9]
permutations = [1111111111]


while permutations[-1] != 9876543210:
    for j in range(1,len(nums)):
        if nums[len(nums)-1-j] < nums[len(nums)-j]:
            m = min([num for num in nums[(len(nums)-j):] if num > nums[len(nums)-1-j]])
            S = sorted([num for num in nums[(len(nums)-1-j):] if num != m])
            nums[(len(nums) - len(S) - 1)] = m
            for k in range(len(S)):
                nums[len(nums) - len(S) + k] = S[k]
            break
    string = ""
    for num in nums:
        string += str(num)
    permutations.append(int(string))



total = 0
for num in permutations:
    if int(str(num)[1:4])%2 == 0 and int(str(num)[2:5])%3 == 0 and int(str(num)[3:6])%5 == 0 and int(str(num)[4:7])%7 == 0 and int(str(num)[5:8])%11 == 0 and int(str(num)[6:9])%13 == 0 and int(str(num)[7:10])%17 == 0:
        total += num

print(total)
