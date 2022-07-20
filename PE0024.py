#PE 24

nums = [i for i in range(10)]

i = 1
while i < 1000000:
    for j in range(1,len(nums)):
        if nums[len(nums)-1-j] < nums[len(nums)-j]:
            m = min([num for num in nums[(len(nums)-j):] if num > nums[len(nums)-1-j]])
            S = sorted([num for num in nums[(len(nums)-1-j):] if num != m])
            nums[(len(nums) - len(S) - 1)] = m
            for k in range(len(S)):
                nums[len(nums) - len(S) + k] = S[k]
            break
    i += 1

print(nums)
