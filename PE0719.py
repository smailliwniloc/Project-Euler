# PE 719

def partition(largest, *rest, ans=[]):
    ans.append([largest, *rest])
    min = rest[0] if rest else 1
    max = largest // 2
    for n in range(min, max+1):
        partition(largest-n, n, *rest)
    return ans

def getDigitSums(num):
    s = str(num)
    partitions = partition(len(s))
    allSums = []
    for split in partitions:
        digitSum = 0
        index = 0
        for i in split:
            digitSum += int(s[index: index + i])
            index += i
        allSums.append(digitSum)

    return allSums


if(__name__ == "__main__"):
    print(partition(5))
    print(getDigitSums(1234))

    