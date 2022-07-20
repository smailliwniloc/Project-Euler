#PE 50

from math import sqrt

def prime(a):
    if a < 2: return False
    for x in range(2, int(sqrt(a)) + 1):
        if a % x == 0:
            return False
    return True


def generate_primes(N):
    primes = [2]
    for x in range(3, N, 2):
        if(prime(x)):
            primes.append(x)
    return primes

if __name__ == "__main__":
    list = generate_primes(3940)
    temp_count = 1
    temp_sum = 0
    max_count = 0
    max_sum = 0
    while(temp_count < len(list)):
        for start in range(len(list) + 1 - temp_count):
            i = start
            while(i < start + temp_count):
                temp_sum += list[i]
                i += 1
            if(prime(temp_sum)):
                max_sum = temp_sum
                max_count = temp_count
            temp_sum = 0
        temp_count += 1
    print(max_sum)
