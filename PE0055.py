#PE 54

def isPalindrome(num):
    s = str(num)
    for i in range(int(len(s)/2)+1):
        if(s[i] != s[len(s) - 1 - i]):
            return False

    return True

def addBackwards(num):
    return num + int(str(num)[::-1])

def becomesPalindromeInLessThan(limit, num):
    for i in range(limit+1):
        if(isPalindrome(num) and i > 0):
            return True
        else:
            num = addBackwards(num)

    return False


if(__name__ == "__main__"):
    count = 0
    for i in range(1, 10001):
        if(not becomesPalindromeInLessThan(50, i)):
            count += 1

    print(count)