#PE 206

# options = [10*x for x in range(101010101, 138902663)]

# for x in options:
#     y = str(x*x)
#     if(len(y) != 19):
#         continue
#     possible = True
#     for i in range(10):
#         if(y[2*i] != (i + 1)%10):
#             possible = False
#             break
#     if(possible):
#         print(x, y)
#         break

digits = [0, 0, 0, 0, 0, 0, 0, 0]

def makeNum(digits):
    ans = 0
    for i in range(len(digits)):
        ans += 10**(2*i + 3) * digits[len(digits) - 1 - i]
    for i in range(9):
        ans += 10**(2*i + 2) * (9-i)

    return ans

def isSquaure(num):
    if (num**.5 - int(num**.5) == 0):
        return True
    else:
        return False

def zfill(num, length):
    s = str(num)
    while(len(s) < length):
        s = "0" + s
    return [int(c) for c in s]

i = 1013091779
while i < 10**9:
    arr = zfill(i, 8)
    possible = makeNum(arr)
    if(isSquaure(possible)):
        print(possible)
        break
    else:
        i += 1


