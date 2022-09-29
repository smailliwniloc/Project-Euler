# PE 607

import math
from scipy.optimize import minimize

theta = math.pi / 4

def f(arr):
    ans = 0
    h = 0
    for i in range(len(arr)):
        dist = d(i, arr[i])
        h += dist * math.sin(arr[i])
        ans += dist / (10 - i)

    eta = math.atan(h/(h + 50 - 25 * math.sqrt(2)))
    ans += d(6, eta)/10

    return ans

def d(idx, angle):
    ans = math.sqrt(2) / 2
    long = 50 - 25 * math.sqrt(2)
    short = 10*math.sqrt(2)
    if(idx == 0):
        ans *= long / math.sin(angle + theta)
    elif(1 <= idx and idx <= 5):
        ans *= short / math.sin(angle + theta)
    elif(idx == 6):
        ans *= long / math.sin(theta - angle)

    return ans

print(minimize(f, [0,0,0,0,0,0]))