#PE 700

euler = 1504170715041707
eulercoins = [euler]
mod = 4503599627370517
swap = 15806432

smallest = euler
inv = pow(smallest, -1, mod)

n = 2

while True:
    num = euler * n % mod
    if num < smallest:
        smallest = num
        eulercoins.append(num)
        print(n, num)
    if(smallest == swap):
        newCoin = 1
        currMax = mod
        while(newCoin != swap):
            num = (inv*newCoin) % mod
            if(num < currMax):
                currMax = num
                eulercoins.append(newCoin)
                print(num, newCoin)
            newCoin += 1
        break
    n += 1

print(sum(eulercoins))
